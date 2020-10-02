# SimpleSolution-Lambda-function
# Author: @JananiPN19
# <Happy Coding/> :)


fizz_func = lambda x: x%3 == 0
buzz_func = lambda x: x%5 == 0
fizzbuzz_func = lambda x: x%15 == 0
for i in range(0,101):
    if fizz_func(i): print('Fizz')
    elif buzz_func(i): print('Buzz')
    elif fizzbuzz_func(i): print('FizzBuzz')
    else: print(i)