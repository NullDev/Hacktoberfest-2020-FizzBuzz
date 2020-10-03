'''
    Have you got what it takes to be the fuzzbizzard..."

    A number will be displayed you have to guess if in a FizzBuzz 
    the number will be displayed normally or will it show Fizz, Buzz or FizzBuzz! 
    
    Enter 0 for normal number
    Enter 1 for Fizz
    Enter 2 for Buzz
    Enter 3 for FizzBuzz

    You will have 7 seconds per number

    Guess all 10 to become the FUZZBIZZARD



'''

import random
import threading
import _thread as thread
from os import system,name

def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def display_instructions():
    clear()
    print("Have you got what it takes to be the fuzzbizzard...\n")
    print("A number will be displayed you have to guess if in a FizzBuzz the number will be displayed normally or will it show Fizz, Buzz or FizzBuzz! \n")
    print("Enter 0 for normall number")
    print("Enter 1 for Fizz")
    print("Enter 2 for Buzz")
    print("Enter 3 for FizzBuzz\n")
    print("You will have 7 seconds per number")
    print("Guess all 10 to become the FUZZBIZZARD")
    print("Press ENTER to play")
    _ = input()


def input_with_timeout(timeout=7):
    timer = threading.Timer(timeout, thread.interrupt_main)
    astring = None
    try:
        timer.start()
        astring = input()
    except KeyboardInterrupt:
        pass
    timer.cancel()
    return astring



def game(x):
    if x % 15 == 0:
        return 3
    elif x % 3 == 0:
        return 1
    elif x % 5 == 0:
        return 2
    else:
        return 0


fizzbuzz = {0:"Normal", 1:"FiZz!", 2:"BuZz!", 3:"FiZzBuZz!!!"}
points = 0

def check():
    clear()
    global points
    x = random.randint(1,100)
    print("The Number is... ",x)
    print("Enter your answer in 7 seconds")
    answer = input_with_timeout()
    if answer != None:
        if game(x) == int(answer):
            print("Correct")
            print(fizzbuzz[game(x)])
            points = points + 1
            print("Press Enter")

        
        else:
            print("Wrong")
            print(fizzbuzz[game(x)])
            print("Press Enter")
    
    else:
        print("Too Slow")
        print(fizzbuzz[game(x)])
        print("Press Enter")
        

display_instructions()

for i in range(10):   
    answer = None
    check()
    _ = input()
    
clear()
print("Your Score:",points)
if points == 10:
    print("Wow!!! you are a fuzzbizzard!!!")
else:
    print("Maybe Next Time")
