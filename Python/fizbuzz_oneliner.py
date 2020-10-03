for n in range(100):
    print("Fizz"*(not n % 3) + "Buzz"*(not n % 5) or n)