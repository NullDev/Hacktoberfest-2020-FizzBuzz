
# FUNCTION DEFINITIONS

def fizz_buzz(lst: list) -> str:
    """
    Returns Fizz if the number is divisible by 3, 
    Buzz if the number is divisible by5,
    and FizzBuzz if the number is divisible by both 3 and 5.
    """

    print("\nThis is the Fizz Buzz for your Fibonacci Sequence\n")
    print(lst)
    print("\n")

    for i in lst:
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 ==0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(i)
    return "\nThank you for playing Fibonacci Fizz Buzz"

def fibonacci(n: int) -> list:
    """
    Returns a list of the Fibonacci Sequence
    up to the n'th number (input)
    """

    lst = []
    for i in range(n + 1):
        if i == 0:
            lst.append(0)
        elif i == 1:
            lst.append(1)
        elif i > 1:
            x = lst[-1] + lst[-2]
            lst.append(x)
    return lst

# SCRIPTING

print(fizz_buzz(fibonacci(int(input("Please enter a number:")))))