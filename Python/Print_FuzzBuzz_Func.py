# Author : @Moglten
# Fizz , Buzz and Fizzbuzz
# from 1 to 100


def printFizzBuzz(n) :
    for x in range(1,n+1) : print(x) if print_FizzBuzz(x) else None

def print_FizzBuzz(n):
    if n % 5 == n % 3 == 0:
        print( "FizzBuzz" )
        return False

    else: return print_Buzz( n )

def print_Buzz(n) :
    if n % 5 == 0:
        print( "Buzz" )
        return False

    else : return print_Fizz(n)

def print_Fizz(n) :
    if n % 3 == 0:
        print( "Fizz" )
        return False

    else : return True



if __name__ == '__main__':
    n = 100
    printFizzBuzz(n)


