#the simplest code possible for fizzbuzz (most-possibly) in python
#Author: Rajat Bansal (@rajat_1401)

for num in range(1,101):
    strr= ""
    if(num%3== 0):
        strr+= "Fizz"
    if(num%5== 0):
        strr+= "Buzz"
    if(strr== ""):
        strr= num
    print (strr)