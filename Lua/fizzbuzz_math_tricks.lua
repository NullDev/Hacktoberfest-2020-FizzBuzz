-- A fizzbuzz module. Usage: `fb = require 'fizzbuzz_math_tricks'` then try `; fb:run_without_modulus()` optional counter limits :run_without_modulos(x,y) 
-- Author: @darrenkearney

local fizzbuzz = {}

function fizzbuzz.fizz(self, x) 
   -- use math trick for finding numbers divisible by 3
   local sum = self:sum_digits(x)

   -- repeat and reduce the sum of digits to one digit
   while #tostring(sum) > 1 do
      sum = self:sum_digits(sum)
   end

   local lookup = {
      [3]=true,
      [6]=true,
      [9]=true
   }

   -- if final digit is divisible by three, it is fizz
   if lookup[sum] then
      return "Fizz"
   else
	  return x
   end
end

function fizzbuzz.buzz(self, x)
   -- use math trick, if last digit is 5 or 0, number is divisible by 5
   -- array lookup method
   local s = tostring(x)
   local lookup = {
      ['5']=true,
      ['0']=true
   }

   -- edge case
   if #tostring(x) == 1 and x == 0 then
      return x
   end

   if lookup[string.sub(s,#s)] or lookup[string.sub(s,#s)] then
      return "Buzz"
   else
      return x
   end
end

function fizzbuzz.sum_digits(self, x)
   if #tostring(x) == 1 then
      return x
   end

   -- sum all of the digits in the number
   local sum = 0
   for i=1, #tostring(x) do
      sum = sum + tonumber(string.sub(tostring(x),i,i)) 
   end

   return sum
end

function fizzbuzz.exec(x)
   local x, s = tonumber(x), ''
   if (x % 3 == 0) then s = s..'Fizz' end
   if (x % 5 == 0) then s = s..'Buzz' end
   if s == '' then s = x end
   return s
end

function fizzbuzz.exec_without_modulo(self, x)
   local x, s = tonumber(x), ''
   if self:fizz(x) == 'Fizz' then s = s..'Fizz' end
   if self:buzz(x) == 'Buzz' then s = s..'Buzz' end
   if s == '' then s = x end
   return s
end

function fizzbuzz.run(self, x1, x2)
   local x1 = tonumber(x1) or 1
   local x2 = tonumber(x2) or 100
   for i=x1, x2, 1 do
      print( self.exec(i) )
   end
end

function fizzbuzz.run_without_modulo(self, x1, x2)
   local x1 = tonumber(x1) or 1
   local x2 = tonumber(x2) or 100
   for i=x1, x2, 1 do
      print( self:exec_without_modulo(i) )
   end
end

return fizzbuzz
