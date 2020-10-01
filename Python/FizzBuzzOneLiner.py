# One Liner Solution for FizzBuzz
# Author: @rowan2702

for i in range(1,100,1) :
	print('FizzBuzz' if (i%15) == 0  else 'Fizz' if (i%3)  == 0 else 'Buzz' if (i%5)  == 0 else i)
