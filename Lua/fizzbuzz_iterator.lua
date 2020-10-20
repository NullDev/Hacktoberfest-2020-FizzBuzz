-- The FizzBuzz iterator - pretty self-descriptive.
-- Author: @PotcFdk

local function fizzBuzzIterator (value, fin)
	value = value or 1
	assert (type (value) == "number")
	value = value - 1
	return function ()
		value = value + 1
		if not fin or value <= fin then
			return (value % 3 == 0 and "Fizz" .. (value % 5 == 0 and "Buzz" or "")) or (value % 5 == 0 and "Buzz") or value
		end
	end
end

for value in fizzBuzzIterator (1, 100) do
	print (value)
end
