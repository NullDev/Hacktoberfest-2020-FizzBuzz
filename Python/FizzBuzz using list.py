a=[]
for x in range(1,101):
    if x%3==0:
        a.append('Fizz')
    elif x%5==0:
        a.append('Buzz')
    elif x%3==0 and x%5==0:
        a.append("FizzBuzz")
    else:
        a.append(x)
print(*a)        
    
    
