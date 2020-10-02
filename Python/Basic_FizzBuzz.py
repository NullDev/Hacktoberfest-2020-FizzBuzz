def isMultiple(numerator,denominator):
    is_multiple=False
    if(numerator%denominator==0):
        is_multiple=True
    return is_multiple

for i in range(1,101):
    if((isMultiple(i,3)==True)and(isMultiple(i,5)==True)):
        print('FizzBuzz')
    elif(isMultiple(i,3)==True):
        print('Fizz')
    elif(isMultiple(i,5)==True):
        print('Buzz')
    else:
        print(i)
