# TO EXECUTE --> python3 2020.py ./Ressources/Data.txt

from datetime import datetime
import sys

# setting the fileName variable to the input file we gave
fileName = sys.argv[1]

# setting the myFile var to openning our file as read only
myFile = open(fileName, "r")

# creating a list where we'll sort the content of our file
fileValueList = []

# creating a list where will be stored all the found values (first algo)
resultList = []

# creating a second list that will store the values found (for second algo)
resultDiffList = []

# creating two counters for our two algo to check which one has the most amount of steps
counterHugo = 0
counterLucile = 0

# Getting user input on what sum he is looking for:
targetValue = int(input("What is your sum target value ? --> "))

# Openning the file and creating a loop that goes through each element of the file and adds it to our list
with myFile as f:
    for x in myFile:
        fileValueList.append(int(x))

# Explanation of algorithm used here:
# Take the list --> [1,2,3,4,5]
# The lenght of the list is 5
# We go through each elements one by one and for each, we sum the other element to it
# Example --> 1+2, 1+3, 1+4, 1+5
# we know that we have to sum up lenght-(index of number + 1)

# starting timer
startTimeHugo = datetime.now()

# loop that goes through each number of the list
for number in fileValueList:
    # loop that does lenght-(number.index+1) amount of otherNumber
    for otherNumber in range(len(fileValueList) - (fileValueList.index(number) + 1)):
        sum = number + otherNumber
        counterHugo += 1
        if sum == targetValue:
            counterHugo += 1
            format = str(number) + " & " + str(otherNumber)
            resultList.append(format)

# stopping timer
finalTimeHugo = datetime.now() - startTimeHugo

# printing the result list
print('\n')

if bool(resultList) == False:
    print("No numbers in the list sum up to " + str(targetValue))
else:
    print("Here are the pair of numbers that sum up to " + str(targetValue) + " :")

for result in resultList:
    print(result)

# However, when speaking with my <3, she thought of a different algo which could be interesting.
# for each element of our list, we are gonna substract it's value from our target value
# if the substraction result is negative, we can directly go to the next value

# starting timer
startTimeLucile = datetime.now()

# loop that goes through each number of the list
for number in fileValueList:
    # getting the difference between our target value and the number we are testing
    subValue = float(targetValue - number)
    counterLucile += 1
    # checking if the difference is positive. If negative, sure it's not what we want and next num
    if subValue >= 0:
        counterLucile += 1
        # loop that does lenght-(number.index+1) amount of otherNumber
        for otherNumber in range(len(fileValueList) - (fileValueList.index(number) + 1)):
            if otherNumber == subValue:
                counterLucile += 1
                format = str(number) + " & " + str(otherNumber)
                resultDiffList.append(format)

# stopping timer and storing variable
finalTimeLucile = datetime.now() - startTimeLucile

# printing the result list
print('\n')

if bool(resultList) == False:
    print("No numbers in the list sum up to " + str(targetValue))
else:
    print("Here are the pair of numbers that sum up to " + str(targetValue) + " :")

for result in resultList:
    print(result)

# printing the number of elements in both lists to see if they both give the same results
print('\n')
if set(resultList) == set(resultDiffList):
    print("Both list have "+ str(len(resultList)) +" elements !(which hopefully means they have they are identical)")
else:
    print("The lists are not identical !")

# printing the number of steps for each algo
print('\n')
print("Hugo's algorithm amount of steps for " + str(targetValue) +" target value is " + str(counterHugo))
print("Lucile's algorithm amount of steps for " + str(targetValue) +" target value is " + str(counterLucile))

# printing the execution time for each algo
print('\n')
print("Hugo's algorithm execution time is -->" + str(finalTimeHugo))
print("Lucile's algorithm execution time is -->" + str(finalTimeLucile))

print('\n')
if finalTimeHugo >= finalTimeLucile:
    print("Lucile's algrithm is FASTER !")
else:
    print("Hugo's algorithm is FASTER !")

# another way of calculating the time that uses concatenation and better formating
# import time
# start_time = time.time()
# print("Helllllllllo Worlddddd !")
# print("--- %s seconds ---" % (time.time() - start_time))