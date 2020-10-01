#This code prints fizzbuzz for 1 to 100 numbers
#Author : @yashpawar394

n = 0
while True:
	n +=1
	if n%3 ==0 and n%5 ==0:
		print("fizzbuzz")
	if n %3 == 0:
		print("fizz")
	elif n%5 == 0:
		print("buzz")
		
	else:
		print(n)
	if n == 100:
		break