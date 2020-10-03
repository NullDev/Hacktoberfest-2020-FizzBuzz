import sys

inputs = sys.argv
inputs.pop(0)
coke='fizz'
sound='buzz'

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print (coke+sound)
    elif n % 3 == 0:
        print (coke)
    elif n % 5 == 0:
        print (sound)
    else:
        print(n)

# inputs = input().split()
for input in inputs:
    input = int(input)
    fizzbuzz(input)
