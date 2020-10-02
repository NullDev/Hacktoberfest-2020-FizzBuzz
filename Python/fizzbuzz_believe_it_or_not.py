'''#FizzBuzz #Hacktoberfest2020
#OneLiner 
#CrazyTupleSolution 
#Used 
#map_function 
#lambda_function 
#enumerate_function 
#LotOfFun'''
#  Author: @deathdater

for actual_num,fizzbuzz in enumerate(map(lambda num:'FizzBuzz' if  num%3 == 0 and  num%5 == 0 else 'Fizz' if num%3 == 0 else 'Buzz' if  num%5 == 0 else str(num),range(1,101)),start=1): print (str(actual_num) + ' --> ' + str(fizzbuzz))
