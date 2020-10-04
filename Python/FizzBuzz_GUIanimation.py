def main():
    import tkinter as tk
    import math
    import time

    root = tk.Tk()
    root.title('FizzBuzz')
    canvas = tk.Canvas(root, width=500, height=500, bg='#d6fce3')
    canvas.pack()

    def create_circle(x, y, r):
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvas.create_oval(x0, y0, x1, y1, fill='blue')

    stepSize = 0.0628319 #3.6 deg in rads
    positions = []

    t = 0
    while t < 2 * math.pi:
        positions.append((200 * math.cos(t), 200 * math.sin(t)))
        t += stepSize

    for i in positions:
        create_circle(i[0]+250, i[1]+250, 3)
     
    for pos in range(100):
        pointer = canvas.create_oval(positions[pos][0]+245, positions[pos][1]+245, positions[pos][0]+255, positions[pos][1]+255, fill='#148416')
        text = canvas.create_text(250, 250, text="Fizz"*((pos+1)%3 == 0) + ((pos+1)%5 == 0)*"Buzz" or pos+1)  
        time.sleep(1)
        root.update()
        canvas.delete(pointer, text)

    root.mainloop()

if __name__ == '__main__':
    main() 