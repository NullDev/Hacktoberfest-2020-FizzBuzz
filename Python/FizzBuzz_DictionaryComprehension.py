#Implemented fizzbuzz using the concept of "Dictionary Comprehension"
#Author:@deekshithanand (github)

def findVal(x):
    if x%3==0:
        if x%5==0:
            return 'Fizzbuzz'
        else:
            return 'Fizz'
    elif x%5 == 0:
        return 'Buzz'
    else:
        return x
    
# using dictionay comprehension here
results = {i:findVal(i) for i in range(1,101)}    
for i in results:
    print(results[i])