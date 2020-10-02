-- A recursive solution to the fizzbuzz problem. 
-- Recursion is awesome. I love recursion :D
-- Author: @E-Almqvist

local fizzbuzzNums = { 15, 5, 3 }

local fizzbuzzWords = {
	[15] = "FizzBuzz", -- if something is divisible with 3 and 5 implies that it is divisible with 15 since 3*5=15 
	[5] = "Buzz",
	[3] = "Fizz"	
}

local function getDivisible( num, div ) -- function to check if num is divisible with div, if so then return div 
	if (num % div == 0) then
		return div
	end
end 

local function printFizzBuzz( num, i, fizzLen, wordBuff )
	i = i or 1
	fizzLen = fizzLen or #fizzbuzzNums
	
	numDiv = getDivisible( num, fizzbuzzNums[i] )
	wordBuff = wordBuff or fizzbuzzWords[ numDiv ] -- instead of a nasty for loop we could just index it via the tables
	
	if(wordBuff) then -- if we found one then print it and end
		print(wordBuff)
		return
	else
		if( i < fizzLen ) then
			i = i + 1
		else
			print(num) -- if we didn't find anything: end and print the number instead
			return
		end
	end
	return printFizzBuzz( num, i, fizzLen, wordBuff ) 
end

function recursiveFizzbuzz( count )
	count = count or 1 -- if count == nil then start at 1

	printFizzBuzz( count ) -- check if it is fizz or buzz etc, then print it

	if( count < 100 ) then -- if count is less than 100 then increment the count var
		count = count + 1
		return recursiveFizzbuzz( count ) -- do the recursion
	else
		return count
	end
end

recursiveFizzbuzz() -- actually run the function
