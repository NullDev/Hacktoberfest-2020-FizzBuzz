# A code for implement of FizzBuzz
# author @siddhant2155


def printFizzBuzz():
    count_3 = 0
    count_5 = 0
    for i in range(1,101):
        count_5 += 1
        count_3 += 1
        str = ""
        if count_3 == 3:
            str += "Fizz"
            count_3 = 0
        if count_5 == 5:
            str += "Buzz"
            count_5 =0
        if not str:
            print(i)
        else:
            print(str)

if __name__ == '__main__':
    printFizzBuzz()