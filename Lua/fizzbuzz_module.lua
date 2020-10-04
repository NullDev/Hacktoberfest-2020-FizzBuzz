-- A fizzbuzz module. Usage: `fb = require 'fizzbuzz_module'; fb:run()` optional counter limits :run(x,y) 
-- Author: @darrenkearney

local fizzbuzz = {}

function fizzbuzz.exec(x)
   local x, s = tonumber(x), ''
   if (x % 3 == 0) then s = s..'Fizz' end
   if (x % 5 == 0) then s = s..'Buzz' end
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

return fizzbuzz
