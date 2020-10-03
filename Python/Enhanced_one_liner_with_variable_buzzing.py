# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 14:57:22 2020

@author: strad
"""
[print('Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or i) for i in range(int(input('How much fizz would a fizz buzz fizz if a fizzbuzzer could fizz buzzes?')))]
