#!/bin/bash
# :Simple bash script to print Fizz for multiples of 3, Buzz for multiples of 5 and FizzBuzz for numbers 
# which is a multiple of both 3 and 5, for numbers in range of 1 to 100.
# @author - radvin1378

printf "%s\n" "FizzBuzz"

for i in {1..99};do
	if [ $(($i % 3)) -eq 0 ] && [ $(($i % 5)) -eq 0 ]; then
		printf "%s," "FizzBuzz"
	
	elif [ $(($i % 5)) -eq 0 ]; then
		printf "%s," "Buzz"

	elif [ $(($i % 3)) -eq 0 ]; then
		printf "%s," "Fizz"
	else
		printf "%d," "$i"

	fi
done

printf "%s\n" "Buzz"
