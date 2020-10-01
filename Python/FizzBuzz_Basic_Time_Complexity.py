# FizzBuzz in python using nested if else
# Author - @hritikchaturvedi11

for i in range(1,100):
    if(i % 3 == 0 and i % 5 == 0):
        print('FizzBuzz')
    elif(i % 3 == 0):
        print('Fizz')
    elif(i % 5 == 0):
        print('Buzz')
    else:
        print(i)
# Now we will find the time complexity of the above code. In simple words, how many times the operations are performed on the variable. So we are using a for loop once and that have if and else condition so. It will have time complexity of O(n). 
