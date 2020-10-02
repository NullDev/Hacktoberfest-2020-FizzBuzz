# Recursive FizzBuzz without loops
# author : karn21

def fizzbuzz(n):
	if n == 101:
		return
	if n%3 == 0 and n%5 == 0:
		print("fizzbuzz")
		return fizzbuzz(n+1)
	if n%3 == 0:
		print("Fizz")
		return fizzbuzz(n+1)
	if n%5 == 0:
		print("Buzz")
		return fizzbuzz(n+1)
	print(n)
	return fizzbuzz(n+1)

fizzbuzz(1)
