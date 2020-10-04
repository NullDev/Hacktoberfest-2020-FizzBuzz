# This solution counts how many times the words "fizz" and "buzz" appear in a range provided by the user
# The input has to be a valid positive integer
# The current count of the word is shown each time the word appears, and a random expression for FizzBuzz

# Author: @moisesjsalmeida

import random

fizz = 0
buzz = 0
fizzbuzz = 0
fb_range = False
interjections = [
    "Wow! ",
    "Yay! ",
    "Ooh-la-la! ",
    "Whoa! ",
    "Yeah! ",
    "Eureka! ",
    "Voila! ",
    "Yipee! ",
    "Boo-ya! ",
]

while not fb_range or fb_range < 1:
    try:
        fb_range = int(input("Type the range of the fizzbuzz count: "))
        if fb_range < 1:
            raise ValueError
    except ValueError:
        print("\nEnter a valid positive integer!")
        continue

for i in range(1, int(fb_range)):
    if i % 3 == 0 and i % 5 == 0:
        fizzbuzz += 1
        i = random.choice(interjections) + "It's a FizzBuzz! #" + str(fizzbuzz)
    elif i % 3 == 0:
        fizz += 1
        i = "Fizz #" + str(fizz)
    elif i % 5 == 0:
        buzz += 1
        i = "Buzz #" + str(buzz)

    print(i)

print("\n")
print("Total Fizzes: " + str(fizz))
print("Total Buzzes: " + str(buzz))
print("Total FizzBuzzes: " + str(fizzbuzz))
