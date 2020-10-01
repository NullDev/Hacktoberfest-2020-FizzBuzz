
#A efficient Python code to implement FizzBuzz
#Author @sumitgsh

for val in range(1,101):
    if val%3 ==0:
        if(val%5==0):
            print("FizzBuzz")
        else:
            print("Fizz")
    elif val%5 ==0:
         print("Buzz")
    else:
        print(val)