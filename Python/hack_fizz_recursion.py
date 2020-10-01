

def check_num(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


def print_fizz_nums(start, end):
    if start == end:
        return
    else:
        start += 1
        check_num(start)
        print_fizz_nums(start, end)


if __name__ == '__main__':
    end_number = 100
    start_number = 0
    print_fizz_nums(start_number, end_number)
