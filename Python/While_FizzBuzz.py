#Implemented FuzzBuzz using while loop.
#Author : @sb19

n=1

#while loop for iterations
while(True):
    
    #to check that number is greater than 100  
    if(n>100):
        # break statement is used to come out of the while loop
        break   
    #to check if number is multiple of  both 3 & 5
    elif(n%3==0 and n%5==0):
        print("FizzBuzz")

    #to check if number is multiple of  3
    elif(n%3==0):
        print("Fizz")

    #to check if number is multiple of 5    
    elif(n%5==0):
        print("Buzz")
    
    else:
        print(n)
    
    n+=1                  #incresing number by 1 after each iteration
    
    
