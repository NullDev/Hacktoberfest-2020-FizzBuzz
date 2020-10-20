-- The FizzBuzz metatable - configurable on any table!
-- Just add the special FizzBuzzMetaTable (tm) to the table and if you try to index a non-existing
-- numeric key, it will default to FizzBuzz instead of returning boring nil values.
-- Author: @PotcFdk

local META = {
	__index = function (tab, key)
		if not tonumber (key) then return end
		return key % 15 == 0 and "FizzBuzz" or key % 3 == 0 and "Fizz" or key % 5 == 0 and "Buzz" or key
	end
}

local FizzBuzz = setmetatable ({}, META)

for i = 1, 100 do
	print (FizzBuzz [i])
end
