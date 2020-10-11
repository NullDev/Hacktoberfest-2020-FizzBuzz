extends Node2D

func _ready():
	for i in range(0, 100, 1):
		if !i % 15:
			print("FizzBuzz")
		elif !i % 5:
			print("Buzz")
		elif !i % 3:
			print("Fizz")
		else:
			print(i)
