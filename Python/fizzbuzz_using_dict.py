#fizzbuzz from 1 to 100
dict_fizzbuzz = {}
dict_fizzbuzz['fizz'] = list(range(0,101,3))
dict_fizzbuzz['buzz'] = list(range(0,101,5))
dict_fizzbuzz['fizzbuzz'] = list(range(1,101,15))

for i in range(1,100):
    if i in dict_fizzbuzz['fizzbuzz']:
        print('fizzbuzz')
    elif i in dict_fizzbuzz['fizz']:
        print('fizz')
    elif i in dict_fizzbuzz['buzz']:
        print('buzz')
    else:
        print(i)
