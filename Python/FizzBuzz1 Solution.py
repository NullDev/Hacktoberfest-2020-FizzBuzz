def FizzBuzz(val):
    """
    A beginner's Solution to the FizzBuzz problem
    """

    if (val % 3 == 0) and (val % 5 == 0):
        return "FizzBuzz"
    elif (val % 3 == 0):
        return "Fizz"
    elif (val % 5 == 0):
        return "Buzz"
    return val

for i in range(101):
    print("Value:", i, "\t", "Output:", FizzBuzz(i))