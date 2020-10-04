# Go Euler or Go Home
# Author: @godspeed5

import numpy as np
for i in range(1,101):
	a3 = np.exp(2j*np.pi*i/3)
	a5 = np.exp(2j*np.pi*i/5)
	if (np.isclose(a3.imag, 0,0.001) and np.isclose(a5.imag, 0,0.001)) :
		print('FizzBuzz')
	elif np.isclose(a3.imag, 0,0.001):
		print('Fizz')
	elif np.isclose(a5.imag, 0,0.001):
		print('Buzz')
	else:
		print(i)


