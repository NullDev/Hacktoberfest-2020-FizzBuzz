# simple fizzbuzz solution
# author @fl0werdance | entry point for hacktoberfest

for fizzbuzz in range(101):
    if fizzbuzz%3 == 0 and fizzbuzz%5 == 0:
        print("fizzbuzz")
    elif fizzbuzz%3 == 0:
        print("fizz")
        continue
    elif fizzbuzz%5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)