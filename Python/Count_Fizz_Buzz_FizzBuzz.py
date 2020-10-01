# Author : Utsav Ramchandra Khatu
# Print number of Fizz , Buzz and Fizzbuzz
# from 1 to n both inclusive where n is the user input


# Function to count words
def count_fizz_buzz(n) :
    temp = n
    fizz,buzz,fizzbuzz = n//3,n//5,n//15
    fizz -= fizzbuzz
    buzz -= fizzbuzz
    print(f"No. of times theword 'Fizz' occurs from 1 to n both inclusive : {fizz}")
    print(f"No. of times theword 'Buzz' occurs from 1 to n both inclusive : {buzz}")
    print(f"No. of times theword 'FizzBuzz' occurs from 1 to n both inclusive : {fizzbuzz}")

# Main function
def main() :
    n = int(input())
    count_fizz_buzz(n)

main()
