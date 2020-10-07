#Fibonacci Series Without Recursion for those who can't seem to understand Recursion ^_^
def fibonacci(n):
    a=[]
    for i in range(n):
        if(i==0):
            a.append(0)#securing 1st and second element of the array
        elif(i==1):
            a.append(1)
        else:
            a.append(a[-1]+a[-2])
    return a
print(fibonacci(10)) #printing the returned Array
