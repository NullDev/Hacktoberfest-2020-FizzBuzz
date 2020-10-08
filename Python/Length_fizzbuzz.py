# Author: Chidu2000
# length python object oriented code to implement fizzbuzz

class Solution(object):

   // function creation
   def fizzBuzz(self, n):
      """
      :type n: int
      :rtype: List[str]
      """
      
      // creating an empty list to store the values to be appended
      result = []
      
      // iterating over the values
      for i in range(1,n+1):
         if i% 3== 0 and i%5==0:
            result.append("FizzBuzz")
         elif i %3==0:
            result.append("Fizz")
         elif i% 5 == 0:
            result.append("Buzz")
         else:
            result.append(str(i))
      return result
      
 // calling function     
ob1 = Solution()
print(ob1.fizzBuzz(30))
