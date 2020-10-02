# Author: @carol975
# Shout the fizz buzz word using python speech to text
# The numbers preceding a fizz, buzz or fizzbuzz number add up 
# to the volume of saying the word.
# Make sure to adjust the audio volume level of your device!!
# You need to install pyttsx3: https://pypi.org/project/pyttsx3/

import pyttsx3

engine = pyttsx3.init()

def shout(word, volume):
    engine.say(word)
    engine.setProperty('volume', volume)
    engine.runAndWait()

curr_volume = 0
for i in range(1,101):
    word = ""
    if i % 3 == 0:
        word += "fizz"
    if i % 5 == 0:
        word += "buzz"
    if word:
        shout(word, round(curr_volume/100, 2))
        curr_volume = 0
    else:
        curr_volume += i