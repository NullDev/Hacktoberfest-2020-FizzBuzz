import requests
import re

response = requests.get('https://raw.githubusercontent.com/NLDev/Hacktoberfest-2020-FizzBuzz/master/README.md').text
response = re.sub('[!,*)@#%(&$_?.]', '', response).split()

def fizzBuzz():
    for i in range(1,101):
        if i%3==0 and i%5==0:
            getStrings('FB')
        elif i%3==0:
            getStrings('F')
        elif i%5 == 0:
            getStrings('B')
        else:
            print(i)

def getStrings(yep):
    fizzBuzzDict = {'FB': '“FizzBuzz”', 'F': '“Fizz”', 'B': '“Buzz”'}

    for word in response:
        if word == fizzBuzzDict[yep]:
            return print(word[1:-1])

if __name__ == '__main__':
    fizzBuzz()