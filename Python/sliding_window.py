""" This code is developed by Sombit Bose

This is sliding windows and modular logic. 
Two sliding windows are maintained with length of 3,5.
The fizzbuzz occurs when the end point of two windows meet.
otherwise they are either fizz or buzz.
modular is used for checking for the buzz number.
"""

slide_3 = [1, 3]
slide_5 = [1, 5]
fizz = set()
buzz = set()
fizz_buzz = set()
while (slide_3[-1] < 100 and slide_5[-1] < 100):
    if slide_3[-1] == slide_5[-1]:
        fizz_buzz.add(slide_3[-1])
    else:
        fizz.add(slide_3[-1])
        if slide_5[-1] % 15 != 0:
            buzz.add(slide_5[-1])
    slide_3[0] += 3
    slide_3[1] += 3
    if slide_3[-1] > slide_5[-1]:
        slide_5[0] += 5
        slide_5[1] += 5
print("The FizzBuzz numbers are")
print(sorted(fizz_buzz))
print("\nThe Fizz numbers are")
print(sorted(fizz))
print("\nThe Buzz numbers are")
print(sorted(buzz))
