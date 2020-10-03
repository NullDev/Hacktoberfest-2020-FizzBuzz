# Author : Benjamin Parsons
# the fizz machine 300 takes a number and tells you
# the number of fizzes, buzzes, and fizzbuzzs for that numbers range!

def fizz_machine3000(number):
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0
    for nums in range(number):
        if nums % 3 == 0:
            fizz_count += 1
        if nums % 5 == 0:
            buzz_count += 1
        if nums % 3 == 0 and nums % 5 == 0:
            fizzbuzz_count += 1
    return 'The fizz machine300 has spoken: there are {} fizzes, {} buzzes, and {} fizzbuzzes in that number range.'.format(fizz_count, buzz_count, fizzbuzz_count)
print(fizz_machine3000(101))
