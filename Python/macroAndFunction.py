FB="FizzBuzz"
F="Fizz"
B="Buzz" 

def gR(x,y):
    return x%y

for i in range(1,101):
    if gR(i,15)==0:
        print(i,FB) 
    elif gR(i,5)==0:
        print(i,B) 
    elif gR(i,3)==0: 
        print(i,F) 
    else: 
        print(i)
