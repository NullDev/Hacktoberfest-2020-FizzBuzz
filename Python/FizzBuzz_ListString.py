"""
Creating a fizzbuuz that returns a list of strings with the values of each iteration.
"""


def fizzbuzz(n):
    list_fizzbuzz = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            list_fizzbuzz.append('fizzbuzz')
        elif i % 3 == 0:
            list_fizzbuzz.append('fizz')
        elif i % 5 == 0:
            list_fizzbuzz.append('buzz')
        else:
            list_fizzbuzz.append(i)

        list_fizzbuzz = list(map(str, list_fizzbuzz))

    return list_fizzbuzz


if __name__ == '__main__':
    n = int(input('n = '))

    print(fizzbuzz(n))
