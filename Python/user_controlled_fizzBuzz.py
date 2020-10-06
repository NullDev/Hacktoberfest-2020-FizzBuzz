"""
Fizz Buzz Solution
Author: Simmi Parmar
"""
import sys

allterms = {}
number_of_terms = int(input("Enter number of terms you want from 2 to 10: "))
if not (2 <= number_of_terms <= 10):
    print("Please enter terms within number limit.")
    sys.exit(1)

for i in range(number_of_terms):
    number = int(input("Enter number: "))
    value = input("Enter string for number: ")
    allterms[number] = value

stoppingNumber = int(input("Enter the stopping number : "))
for j in range(1, stoppingNumber+1):
    result = ""
    for k in allterms:
        if j % k == 0:
            result += allterms[k]
    
    print(result or j)


