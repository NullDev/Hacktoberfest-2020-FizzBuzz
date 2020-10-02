'''
Following the exact reverse order of solving this FizzBuzz problem.
That is, starting with 100 FizzBuzz string, instead of starting with the index, 
and working my way backwords.

Author: @saurabh618
'''

li = ["FizzBuzz" for i in range(1,101)]
for index, element in enumerate(li, 1):
    
    if index % 3 == 0 and index % 5 == 0:
        continue
    
    # Replacing all the FizzBuzz which are a multiple of 5, with "Buzz"
    if index % 5 == 0:
        li[index - 1] = "Buzz"
        
    # Replacing all the FizzBuzz which are a multiple of 3, with "Fizz"   
    elif index % 3 == 0:
        li[index - 1] = "Fizz"
    
    # Replacing all the remaining FizzBuzz, with its index   
    else:
        li[index - 1] = index

print(li)
