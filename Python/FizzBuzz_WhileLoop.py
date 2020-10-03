# FizzBuzz using a while loop, beginners edition
# Author @ kayne103

# This is python 3, dont run using python 2 interpreter.
index = 1

while index <= 100:       
    if index%3!=0 and index%5!=0:
        print(index)
    elif index%3==0 and index%5==0:
        print("FizzBuzz")
    else:
        if index%3 == 0:
            print ("Fizz")
        if index%5 == 0:
            print ("Buzz")
    index = index + 1