# Author : Utsav Ramchandra Khatu
# FizzBuzz Completion
"""Every Number wants to be FizzBuzz Number but all numbers are lazy
so they want the minimum no. of moves to become a FizzBuzz Number"""

n = int(input())
if n <= 15 :
    print(15-n)
else :
    x = 15*(n//15)
    y = 15*(n//15) + 15
    print(min(n-x,y-n))
