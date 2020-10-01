# A simple Python code to implement the Hacktober-2020-FizzBuzz program
# Author @Deephacks619

try:                                #try block tests a block of code for errors
    for i in range(1,100+1):         #loop runs from 1 to 100
        if i%3==0 and i%5==0:        #checks whether i is divisible by 3 and 5
            print("FizzBuzz")
            continue
        elif i%3==0:
            print("Fizz")            #checks whether i is divisible by 3
            continue
        elif i%5==0:                 #checks whether i is divisible by 5
            print("Buzz")
            continue
except:                             #except block lets you handle the errors
    print("There was an error in code")