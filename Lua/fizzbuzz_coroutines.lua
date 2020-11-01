-- Fizzbuzz using Lua Coroutines. Beautifully over-complicated! Reference: https://www.tutorialspoint.com/lua/lua_coroutines.htm 
-- Author: @darrenkearney

function getFizzBuzz()
   local function getFizzHelper()
      co = coroutine.create(function ()
      coroutine.yield('')
      coroutine.yield('')
      coroutine.yield('Fizz')
      end)
      return co
   end
   
   local function getBuzzHelper()
      co = coroutine.create(function ()
      coroutine.yield('')
      coroutine.yield('')
      coroutine.yield('')
      coroutine.yield('')
      coroutine.yield('Buzz')
      end)
      return co
   end
   
   if(fizzHelper) then
      status, fizz = coroutine.resume(fizzHelper);
		
      if coroutine.status(fizzHelper) == "dead" then
         fizzHelper = getFizzHelper()
         status, fizz = coroutine.resume(fizzHelper);
      end
		
   else
      fizzHelper = getFizzHelper()
      status, fizz = coroutine.resume(fizzHelper);
   end

   if(buzzHelper) then
      status, buzz = coroutine.resume(buzzHelper);
		
      if coroutine.status(buzzHelper) == "dead" then
         buzzHelper = getBuzzHelper()
         status, buzz = coroutine.resume(buzzHelper);
      end
		
   else
      buzzHelper = getBuzzHelper()
      status, buzz = coroutine.resume(buzzHelper);
   end

   return fizz..buzz
end

for index = 1, 100 do
	fizzbuzz = getFizzBuzz()
	if fizzbuzz == '' then
		print( index )
	else
		print( fizzbuzz )
	end
end
