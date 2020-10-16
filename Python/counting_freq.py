from collections import Counter, defaultdict

def fizz_buzz_counter():
    values = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            values.append("fizzbuzz")
        elif i % 3 == 0:
            values.append("fizz")
        elif i % 5 == 0:
            values.append("buzz")
        else:
            values.append("int")

    return Counter(values)


def fizz_buzz_defaultdict():
    values = defaultdict(int)
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            values["fizzbuzz"] += 1
        elif i % 3 == 0:
            values["fizz"] += 1
        elif i % 5 == 0:
            values["buzz"] += 1
        else:
            values["int"] += 1

    return values


print(dict(fizz_buzz_counter()))
print(dict(fizz_buzz_defaultdict()))