# This is meant to be a simple FizzBuzz-Quiz
import random
number = 0
while number % 3 != 0 and number % 5 != 0 or number == 0:
    number = random.randint(0, 1000)

print("Your number is: " + str(number))
user_input = input("Fizz, Buzz or FizzBuzz? Please input!\n")

if number % 3 == 0 and number % 5 == 0:
    print("Right solution is: FizzBuzz.")
    if user_input.lower() == "fizzbuzz":
        print("You are right!")
    else:
        print("You are wrong!")
elif number % 3 == 0:
    print("Right solution is: Fizz")
    if user_input.lower() == "fizz":
        print("You are right!")
    else:
        print("You are wrong!")
elif number % 5 == 0:
    print("Right solution is Buzz")
    if user_input.lower() == "buzz":
        print("You are right!")
    else:
        print("You are wrong!")

