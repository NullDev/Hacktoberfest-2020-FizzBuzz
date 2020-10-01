# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 19:24:26 2020

@author: Home
"""

print("".join(map((lambda x: ("fizzbuzz"+"\n") if x%15==0  else "fizz"+"\n" if x%3==0 else "buzz"+"\n" if x%5 ==0 else str(x)+"\n"),[x for x in range(100+1)])))

