# Python 2020 Algorithm

This python program was designed to solve the challenge given at the CSS Python Workshop.

The challenge was that, given a Data.txt file full of numbers, we would write a program that would find the pair(s) of numbers that would sum up to 2020.

I found this exercise very interesting, in particular the designing the algorithm.

My program is composed of two algorithms: One thought and designed by me, and the second one thought by my girlfriend.

## Usage

```python
# run the following to execute
python3 2020.py ./Resources/Data.txt
```
## Explanation

### First algorithm

the first algo works by going through the list of numbers and, for each number, adding the rest of the numbers on the list and checking if the sum equals our target value (which by default is 2020)


### Second algorithm

The second algo is quite clever and reduces the amount of steps and operations we need to execute.

First, it substracts the number from the target value. 
Once that is done, it checks if the result is a negative number, in which case there is no need to do anymore comparison.
If the result is not a negative number, then it searches through the file to see if we can find a match


## Additional Features

- Added user input interface that asks the user if he wants to input his own target value or go with the default one

- Added a step calculator that compares the two algorithms at each execution

- Added a time execution timer that calculates the time it took to execute both algorithms

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.