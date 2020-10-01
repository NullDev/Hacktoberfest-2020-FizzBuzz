#ShobhitRathi

def fizzbuzz():
    for i in range(101):
        if i<3:
            print(i)
        elif i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        else:
            print(i)
fizzbuzz()
