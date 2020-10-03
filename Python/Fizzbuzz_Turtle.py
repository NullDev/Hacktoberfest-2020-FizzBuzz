#FizzBuzz program using turtle library
#blue color Turtle if number multiple of 5
#red color Turtle if number multiple of 3
#purple color Turtle if number id =s multiple of both 3and 5
#Author : @shashankseth01

from turtle import *

shape('turtle')
penup()
setpos(0,60)
pendown()
distance = 25
angle = 15
for i in range(1,101):
    pendown()
    if(i%15==0):
        color('purple')
        stamp()
    elif(i%5==0):
        color('blue')
        stamp()
    elif(i%3==0):
        color('red')
        stamp()
    else:
        color('black')
        write(i)      
    penup()
    forward(distance)
    right(angle)
    distance+=0.8
hideturtle()    
exitonclick()