#  [The ordinary FizzBuzz but with emoticon 😉 - my first PR na Hacktoberfest 😨]
#  Author: @LivSith

i = 0
for i in range(100):
    i += 1
    if i % 3 == 0 and i % 5 == 0:
        print ('FizzBuzz 🤘')
    elif i % 3 == 0:
        print ('Fizz 😃')
    elif i % 5 == 0:
        print ('Buzz 😁')
    else:
        print (i)