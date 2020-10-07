""" FizzBuzz is a program that prints the numbers from 1 to 100. But for multiples of three it prints “Fizz” 
instead of the number and for the multiples of five, it prints “Buzz”. For numbers which are multiples of both 
three and five it prints “FizzBuzz”. """
for i in range(1,101):
    
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

print("SAVE THE AMAZON \nhttps://www.savingtheamazon.org/")