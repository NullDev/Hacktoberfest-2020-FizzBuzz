//fizzbuzz python programming
// Author: @Chamudi
i=1
while i <= 100:
    if i%3==0:
        print("Fizz", end="")
        if i%5==0:
            print("Buzz", end="")
    elif i%5==0:
        print("Buzz", end="")
    else:
        print(i, end="")
    print()
    i+=1