#Do Fizzbuzz using lcm function in python.
#Author: @punnattnp

def lcm(x, y):
    if x > y:
        greater_number = x
    else:
        greater_number = y
    
    while(True):
        if((greater_number % x == 0) and (greater_number % y == 0)):
            lcm = greater_number
            break
        greater_number += 1
    return lcm

for i in range(1,101):
    if(i % lcm(3,5) == 0):
        print('fizzbuzz')
    elif(i % 3 == 0):
        print('fizz')
    elif(i % 5 == 0):
        print('buzz')
    else:
        print(i)