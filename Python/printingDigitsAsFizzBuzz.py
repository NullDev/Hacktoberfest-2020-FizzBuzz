# For a given two numbers a and b <100, the program will print the numbers from 01 to 99
#       replacing the number "a" with "Fizz" and "b" with "Buzz".
# For example, a=1, b=2 Output: 0Fizz, 0Buzz, 03,04,05,06,07,08,09,Fizz0,FizzFizz,Fizz2,...,Fizz9,Buzz0,Buzz1,... and so on
# author : GnathMath

def specialPrint(a,b):
    shift={0:"0",
           1:"1",
           2:"2",
           3:"3",
           4:"4",
           5:"5",
           6:"6",
           7:"7",
           8:"8",
           9:"9"}
    shift[a]="Fizz"
    shift[b]="Buzz"
    for i in range(1,100):
        tens=int(i/10)
        ones=i%10
        print(shift[tens]+shift[ones])
def main():
    print("Number for Fizz:")
    a=int(input())
    print("Number for Buzz:")
    b=int(input())
    specialPrint(a,b)
main()
