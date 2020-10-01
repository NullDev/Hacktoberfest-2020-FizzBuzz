class FizzBuzz:

	def __init__(self, start, end):
		self.start = start
		self.end = end
		self.fizz = []
		self.buzz = []
		self.fizzbuzz = []

	def solver(self):
		for val in range(self.start, self.end):
			if val % 3 == 0 and val % 5 == 0:
				self.fizzbuzz.append(val)
				print(str(val) + " --> FizzBuzz")
			elif val % 5 == 0:
				self.buzz.append(val)
				print(str(val) + " --> Buzz")
			elif val % 3 == 0:
				self.fizz.append(val)
				print(str(val) + " --> Fizz")

		print("-------------------FIZZ NUMBERS-----------------\n")
		self.draw_pattern(self.fizz, 7)
		print("-------------------BUZZ NUMBERS------------------\n")
		self.draw_pattern(self.buzz,5)
		print("-------------------FIZZ-BUZZ NUMBERS------------------\n")
		self.draw_pattern(self.fizzbuzz, 4)



	def draw_pattern(self, arr, level):
		k = 0
		for i in range(1, level):
			for j in range(1, i+1):
				print(arr[k], end="	")
				k += 1
			print()
		print("Leftover numbers = ", arr[k:], "\n")

if __name__ == "__main__":
	fizz_buzz = FizzBuzz(1, 101)
	fizz_buzz.solver()