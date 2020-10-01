# Using divisibility rule to determine what line to print
# Author: @veotani
def divisibility_rule_3(number):
    if number < 10:
        return number in {0, 3, 6, 9}
    return divisibility_rule_3(sum([int(digit) for digit in str(number)]))

def divisibility_rule_5(number):
    return int(str(number)[-1]) in {0, 5}

def divisibility_rule_15(number):
    return divisibility_rule_5(number) and divisibility_rule_3(number)

for number in range(1, 101):
    if divisibility_rule_15(number):
        print('FizzBuzz')
    elif divisibility_rule_3(number):
        print('Fizz')
    elif divisibility_rule_5(number):
        print('Buzz')
    else:
        print(number)