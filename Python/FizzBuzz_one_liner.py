# My attempt on one liner python script for FizzBuzz solution
# Author: @galahad42

for i in range(1,101):
    print("Fizz"*(i%3 == 0) + (i%5 == 0)*"Buzz" or i)
