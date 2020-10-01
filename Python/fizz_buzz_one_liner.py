# Author Abhishek Dobliyal

# FizzBuzz One Liner

def fizz_buzz() -> str:
    return ["FizzBuzz" if not i%3 and not i%5 else "Fizz" if not i%3 else "Buzz"
            if not i%5 else i for i in range(1, 101)]

if __name__ == '__main__':
    print(*fizz_buzz(), sep=",")
