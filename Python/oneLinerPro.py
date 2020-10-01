# Using a lambda function
# Author: @GauravPoosarla
print(list(map(lambda i: "Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i), range(1,101))))
