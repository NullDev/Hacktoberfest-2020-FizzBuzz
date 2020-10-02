# Author : @AnushkaThakkar

# It uses turtle module in python
# turtle shape used in this program is 'arrow'

import turtle

turtle.pencolor("black")
turtle.shape("arrow")
turtle.penup()
x = -700
y = 380
turtle.goto(x, y)
            
for num in range(1,101):
    if(num == 40):
        x = -200
        y = 380
        turtle.goto(x, y)
    elif(num == 79):
        x = 300
        y = 380
        turtle.goto(x, y)
    if(num % 15 == 0):
        turtle.write("FizzBuzz", move = True, font=("Verdana", 10, "italic"))
    elif(num % 3 == 0):
        turtle.write("Fizz", move = True, font=("Verdana", 10, "italic"))
    elif(num % 5 == 0):
        turtle.write("Buzz", move = True, font=("Verdana", 10, "italic"))
    else:
        turtle.write(num, move = True, font=("Verdana", 10, "italic"))
    y = y - 20
    turtle.penup()
    turtle.goto(x, y)
    
turtle.exitonclick()