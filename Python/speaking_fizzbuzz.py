//Speaking Reversed FizzBuzz Program
//Author: @gautambagla

import pyttsx3

def fizzbuzz(n):
    engine = pyttsx3.init()
    if n == 1:
        engine.say(n)
        print(n)
        engine.runAndWait()
        return
    elif n % 15 == 0:
        engine.say('FizzBuzz')
        print('FizzBuzz')
        engine.runAndWait()
    elif n % 3 == 0:
        engine.say('Fizz')
        print ('Fizz')
        engine.runAndWait()
    elif n % 5 == 0:
        engine.say('Buzz')
        print ('Buzz')
        engine.runAndWait()
    else:
        engine.say(n)
        print (n)
        engine.runAndWait()
    return fizzbuzz(n - 1)


fizzbuzz(100)

