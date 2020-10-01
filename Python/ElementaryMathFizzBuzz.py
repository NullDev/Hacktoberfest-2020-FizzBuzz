# Used elementary math techniques for checking if divisible by 3 and 5
# Added digits to check if it will be divisible by 3
# checked last digit if 0 or 5 to be divisible by 5
# author : @mikenmo
def checkThree(digits):
    digitSum = 0
    for i in digits:
        digitSum = digitSum + i
    if(digitSum > 9):
        digitSumDigits = list(map(int, list(str(digitSum))))
        return(checkThree(digitSumDigits))
    else:
        if(digitSum == 3 or digitSum == 6 or digitSum == 9):
            return True
        else:
            return False

def checkFive(digits):
    if(digits[len(digits)-1] == 0 or digits[len(digits)-1] == 5):
        return True
    else:
        return False
        

for i in range(1,101):
    ans = []
    digits = list(map(int, list(str(i))))
    if(checkThree(digits)):
        ans.append("Fizz")
    if(checkFive(digits)):
        ans.append("Buzz")
    if not ans:
        ans.append(i)
    print(''.join(str(i) for i in ans))