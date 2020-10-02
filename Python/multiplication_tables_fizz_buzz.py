five_table = {i * 5: True for i in range(1, 21)}
three_table = {i * 3: True for i in range(1, 34)}

fizz_buzz = []
for i in range(1, 101):

    if i in three_table and i in five_table:
        fizz_buzz.append('FizzBuzz')
        continue

    if i in three_table:
        fizz_buzz.append('Fizz')
        continue

    if i in five_table:
        fizz_buzz.append('Buzz')
        continue

    fizz_buzz.append(i)

print(fizz_buzz)
