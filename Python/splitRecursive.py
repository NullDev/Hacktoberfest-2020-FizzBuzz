# Unnecessary split recursive FizzBuzz
# Author: @adam-94

def fizz(n):
    if n % 3 == 0:
        return True

def buzz(n):
    if n % 5 == 0:
        return True

def FizzBuzz(n):
    if n > 100:
        return 1
    if fizz(n) and buzz(n) == True:
        print('FizzBuzz')
    elif fizz(n) == True:
        print('Fizz')
    elif buzz(n) == True:
        print('Buzz')
    else:
        print(n)
    return n + FizzBuzz(n+1)

if __name__ == '__main__':
    FizzBuzz(1)