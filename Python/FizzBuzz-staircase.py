l=[*range(1,101)]
for i in range(2,99,3): l[i]="Fizz"
for i in range(4,100,5): l[i]="Buzz"
for i in range(14,90,15): l[i]="FizzBuzz";k=2;i=0
while i<99:
    print(*l[i:i+k+1])
    k+=1;i+=k


'''The output creates a hilly(uneven) staircase but with a coincidence(not really!!) that 
the entire first column does not contain any "Fizz" or "Buzz"(not even "FizzBuzz" itself) 
and is a two level arithmetic progression i.e., the difference between two consecutive 
numbers are in progression'''
