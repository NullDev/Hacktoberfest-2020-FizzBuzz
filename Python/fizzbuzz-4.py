# Author: @alexandrunst
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
        continue
    elif num % 3 == 0:
        print("fizz")
        continue
    elif num % 5 == 0:
        print("buzz")
        continue
    print(num)