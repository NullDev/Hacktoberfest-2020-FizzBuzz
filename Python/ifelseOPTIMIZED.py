# if-else optimized code for fizz buzz
# author - @aryamansinghk
l1 = int(input("lower linit of range to find fizz buzz"))
l2 = int(input("upper limit of range to find fizz buzz"))
for i in range(l1,l2+1):
    if i%3==0:
        if i%5==0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif i%5==0:
        print("Buzz")
