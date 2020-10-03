# Python script for Fizzbuzz problem
# Author: @akash19x

class Answer(object):
   def fizzBuzz(self):
      result = []
      for i in range(1,101):
         if i% 3== 0 and i%5==0:
            result.append("FizzBuzz")
         elif i %3==0:
            result.append("Fizz")
         elif i% 5 == 0:
            result.append("Buzz")
         else:
            result.append(str(i))
      return result
obj = Answer()
print(obj.fizzBuzz(30))
