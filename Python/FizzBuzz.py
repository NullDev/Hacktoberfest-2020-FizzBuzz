
def fizzBuzz(maximumNo):
    count_3 = count_5 = 0
    for i in range(1, maximumNo + 1):
        count_3 += 1   
        count_5 += 1
        if count_3 == 3 and count_5 == 5:
            print('fizzbuzz')
            count_3 = count_5 = 0
        elif count_3 == 3:
            print('fizz')
            count_3 = 0
        elif count_5 == 5:
            print('buzz')
            count_5 = 0
        else:
            print(i)

maxNo = input("Enter range: ")
fizzBuzz(maximumNo)
