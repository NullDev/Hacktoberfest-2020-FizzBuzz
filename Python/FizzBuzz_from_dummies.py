// FizzBuzz Hacktoberfest 2020
// Author: @jessilude

x = range(1,101)

for n in x:
	is3x = n % 3 == 0
	is5x = n % 5 == 0
	if is3x and is5x:
		n = "FizzBuzz"
	elif is3x:
		n = "Fizz"
	elif is5x:
		n = "Buzz"
	print(n)