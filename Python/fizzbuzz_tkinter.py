from tkinter import *
from PIL import ImageTk
root =Tk()
root.geometry('300x700+10+10')
root.title("FizzBuzz App")
root.resizable(False,False)
root.bg = ImageTk.PhotoImage(file="122.jpg")
root.bg_image=Label(root,image=root.bg).place(x=0,y=0)
for fizzbuzz in range(1,31):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        a="fizzbuzz"
    elif fizzbuzz % 3 == 0:
        a="fizz"
    elif fizzbuzz % 5 == 0:
        a="buzz"
    else:
        a=fizzbuzz
    labl = Label(root,text=a).pack(pady=1)
root.mainloop()