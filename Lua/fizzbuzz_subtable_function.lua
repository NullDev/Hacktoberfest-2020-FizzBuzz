-- This one creates a table with a metatable attached that allows to unconditionally insert text fragments.
-- It then uses that table to insert Fizz/Buzz fragments at the correct positions.
-- Finally, a function is generated that uses this table to concat the fragments, if any.
-- Author: @PotcFdk

local META = {
	__index = function (tab, key)
		tab [key] = rawget (tab, key) or {}
		return rawget (tab, key)
	end
}

local function makeFizzBuzz (start, fin)
	local output = setmetatable({}, META)
	for i = start, fin do
		if i % 3 == 0 then table.insert (output [i], "Fizz") end
		if i % 5 == 0 then table.insert (output [i], "Buzz") end
	end
	return function (key)
		return rawget (output, key) and table.concat (rawget (output, key), "") or key
	end
end

local FizzBuzz = makeFizzBuzz (1, 100)

for i = 1, 100 do
	print (FizzBuzz (i))
end
