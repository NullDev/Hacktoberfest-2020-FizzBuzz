-- Fizzbuzz using a finite state machine / automata-based approach. Makes use of Lua 1-indexed tables and global variables scope.
-- Author: @darrenkearney

STATE = 0

function fsm (case)
	if case % 3 == 0 and case % 5 == 0 then
		STATE = 3
		return STATE
	elseif case % 3 == 0 then
		STATE = 1
		return STATE
	elseif case % 5 == 0 then 
		STATE = 2
		return STATE
	else
		STATE = 0
		return STATE
	end
end

fizzbuzz = {}
fizzbuzz[1] = 'Fizz'
fizzbuzz[2] = 'Buzz'
fizzbuzz[3] = 'FizzBuzz'

for i=1,100 do
	print( fizzbuzz[ fsm(i) ] or i )
end
