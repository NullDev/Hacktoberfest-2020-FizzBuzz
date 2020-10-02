import random

numbers_retrieved = 0

# Randomly retrieve numbers until you get them in order of 1-100
while True:
    curr_int = random.randint(1, 100)
    if curr_int != numbers_retrieved + 1:
        continue
    else:
        print("Fizz"*(curr_int%3==0)+"Buzz"*(curr_int%5==0) or curr_int)
        numbers_retrieved += 1
    if numbers_retrieved == 100:
        break