# A simple Tkinter GUI application which checks for FIZZ/BUZZ on given input
#Author: @SakshamSingh-v2

from tkinter import *

root = Tk()

status = StringVar()
status.set("Input a Number")

root.title("FIZZBUZZ")
root.geometry("400x200")
root.minsize(400, 200)

def fizzbuzz(inp):
    
    try: 
        num = int(inp.get())
        if num % 3 == 0 and not num % 5 == 0 :
            status.set("FIZZ")  
        elif num % 5 == 0 and not num % 3 == 0:
            status.set("BUZZ")
        elif num % 3 == 0 and num % 5 == 0:
            status.set("FIZZBUZZ")
        else:
            status.set(num)
                   
    except:
        status.set("Invalid Number")    

#Title
Label(root, text = "FIZZ OR BUZZ", font = "arialblack 20 bold").pack(fill = "x")
Label(root, text = "Enter the Number", font = "arial 10").pack(fill = "x")

#Input
inp = StringVar()
Entry(root, textvariable = inp).pack()


#Button
Button(root, text = "Check",font = "arial 15", command = lambda:fizzbuzz(inp)).pack()

#bottombar
f2 = Frame(root, bg = "green", height = 20)
f2.pack(side = "bottom", fill = "x")
l2 = Label(f2, textvariable = status, font = "arial 10 bold")
l2.pack()


root.mainloop()

