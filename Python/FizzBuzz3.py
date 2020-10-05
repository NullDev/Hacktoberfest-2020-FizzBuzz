def _3x(lst):
    for i in range(0,101,3):
        lst[i]="Fizz"
    return lst    

def _5x(lst):
    for i in range(0,101,5):
        lst[i]="Buzz"
    return lst    

def _15x(lst):
    for i in range(0,101,15):
        lst[i]="FizzBuzz"   
    return lst
#Driver Program

a = []
for i in range(101):
    a.append(i)
b = _3x(a)
c = _5x(b)
print(_15x(c))