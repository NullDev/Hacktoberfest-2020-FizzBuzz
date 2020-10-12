// It is a GUI based Sudoku game 
//Developed with tkinter library.

// Author: @azus2000

import random
import time
import os
import tkinter.tix
import pickle
from tkinter import *
from tkinter.constants import *
from tkinter.tix import FileSelectBox, Tk

random.seed(time.time())


# There are probably a few bugs in this class, and it could be implemented
# better I think.
class SudokuBoard:
    """
    Data structure representing the board of a Sudoku game.
    """


    def __init__(self):
        self.clear()

    def clear(self):
        """
        Empty the board.
        """
        self.grid = [[0 for x in range(9)] for y in range(9)]
        self.locked = []

    def get_row(self, row):
        return self.grid[row]

    def get_cols(self, col):
        return [y[col] for y in self.grid]

    def get_nearest_region(self, col, row):
        """
        Regions are 3x3 sections of the grid.
        """
        def make_index(v):
            if v <= 2:
                return 0
            elif v <= 5:
                return 3
            else:
                return 6
        return [y[make_index(col):make_index(col)+3] for y in
                self.grid[make_index(row):make_index(row)+3]]

    def set(self, col, row, v, lock=False):
        if v == self.grid[row][col] or (col, row) in self.locked:
            return
        for v2 in self.get_row(row):
            if v == v2:
                raise ValueError()
        for v2 in self.get_cols(col):
            if v == v2:
                raise ValueError()
        for y in self.get_nearest_region(col, row):
            for x in y:
                if v == x:
                    raise ValueError()
        self.grid[row][col] = v
        if lock:
            self.locked.append((col, row))

    def get(self, col, row):
        return self.grid[row][col]

    def __str__(self):
        strings = []
        newline_counter = 0
        for y in self.grid:
                strings.append("%d%d%d %d%d%d %d%d%d" % tuple(y))
                newline_counter += 1
                if newline_counter == 3:
                    strings.append('')
                    newline_counter = 0
        return '\n'.join(strings)

def sudogen_1(board):
    """
    Algorithm:
        Add a random number between 1-9 to each subgrid in the
        board, do not add duplicate random numbers.
    """
    board.clear()
    added = [0]
    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            if len(added) == 10:
                return
            i = 0
            while i in added:
                i = random.randint(1, 9)
            try:
                board.set(random.randint(x, x+2), random.randint(y, y+2), i, lock=True)
            except ValueError:
                print("Board rule violation, this shouldn't happen!")
            added.append(i)

def rgb(red, green, blue):
    """
    Make a tkinter compatible RGB color.
    """
    return "#%02x%02x%02x" % (red, green, blue)

class SudokuGUI(Frame):
    board_generators = {"SudoGen v1 (Very Easy)":sudogen_1}
    board_generator = staticmethod(sudogen_1)

    def new_game(self):
        self.board.clear()
        self.board_generator(self.board)
        self.sync_board_and_canvas()

    def make_modal_window(self, title):
        window = Toplevel()
        window.title(title)
        window.attributes('-topmost', True)
        window.grab_set()
        window.focus_force()
        return window

    def load_game(self):
        def _load_game(filename):
            with open(filename, 'rb') as f:
                board = pickle.load(f)
                if not isinstance(board, SudokuBoard):
                    # TODO: Report bad file
                    return
                self.board = board
            self.sync_board_and_canvas()
            window.destroy()
        window = self.make_modal_window("Load Game")
        fbox = FileSelectBox(window, command=_load_game)
        fbox.pack()
        window.mainloop()

    def save_game(self):
        def _save_game(filename):
            with open(filename, 'wb') as f:
                pickle.dump(self.board, f, protocol=2)
            window.destroy()
        window = self.make_modal_window("Save Game")
        fbox = FileSelectBox(window, command=_save_game)
        fbox.pack()
        window.mainloop()

    def query_board(self):
        window = self.make_modal_window("Set Board Algorithm")

        scroll = Scrollbar(window)
        scroll.pack(side='right', fill='y')

        listbox = Listbox(window, yscrollcommand=scroll.set)

        scroll.config(command=listbox.yview)

        bframe = Frame(window)

        for s in self.board_generators.keys():
            listbox.insert(-1, s)

        def do_ok():
            self.board_generator = self.board_generators[listbox.get(ACTIVE)]
            window.destroy()

        def do_cancel():
            window.destroy()


        cancel = Button(bframe, command=do_cancel, text="Cancel")
        cancel.pack(side='right', fill='x')

        ok = Button(bframe, command=do_ok, text="Ok")
        ok.pack(side='right', fill='x')

        listbox.pack(side='top', fill='both', expand='1')
        bframe.pack(side='top', fill='x', expand='1')

        window.mainloop()

    def make_grid(self):
        c = Canvas(self, bg=rgb(128,128,128), width='512', height='512')
        c.pack(side='top', fill='both', expand='1')

        self.rects = [[None for x in range(9)] for y in range(9)]
        self.handles = [[None for x in range(9)] for y in range(9)]
        rsize = 512/9
        guidesize = 512/3

        for y in range(9):
            for x in range(9):
                (xr, yr) = (x*guidesize, y*guidesize)
                self.rects[y][x] = c.create_rectangle(xr, yr, xr+guidesize,
                                                      yr+guidesize, width=3)
                (xr, yr) = (x*rsize, y*rsize)
                r = c.create_rectangle(xr, yr, xr+rsize, yr+rsize)
                t = c.create_text(xr+rsize/2, yr+rsize/2, text="SUDO",
                                  font="System 15 bold")
                self.handles[y][x] = (r, t)

        self.canvas = c
        self.sync_board_and_canvas()

    def sync_board_and_canvas(self):
        g = self.board.grid
        for y in range(9):
            for x in range(9):
                if g[y][x] != 0:
                    self.canvas.itemconfig(self.handles[y][x][1],
                                           text=str(g[y][x]))
                else:
                    self.canvas.itemconfig(self.handles[y][x][1],
                                           text='')

    def canvas_click(self, event):
        print("Click! (%d,%d)" % (event.x, event.y))
        self.canvas.focus_set()
        rsize = 512/9
        (x,y) = (0, 0)
        if event.x > rsize:
            x = int(event.x/rsize)
        if event.y > rsize:
            y = int(event.y/rsize)
        print(x,y)
        if self.current:
            (tx, ty) = self.current
            #self.canvas.itemconfig(self.handles[ty][tx][0], fill=rgb(128,128,128))
        self.current = (x,y)

        # BUG: Changing the color of the background of a tile erases parts of
        #      the thick gridlines
        #self.canvas.itemconfig(self.handles[y][x][0], fill=rgb(255,255,255))

    def canvas_key(self, event):
        print("Clack! (%s)" % (event.char))
        if event.char.isdigit() and int(event.char) > 0 and self.current:
            (x,y) = self.current
            #self.canvas.itemconfig(self.handles[y][x][0], fill=rgb(128,128,128))
            try:
                self.board.set(x, y, int(event.char))
                self.sync_board_and_canvas()
            except ValueError:
                # TODO: I'd rather set the erroneous value anyway and simply
                #       not consider it valid, and perhaps set the text color
                #       to red.
                pass

    def __init__(self, master, board):
        Frame.__init__(self, master)

        if master:
            master.title("SudokuGUI")

        self.board = board
        self.board_generator(board)
        bframe = Frame(self)

        self.ng = Button(bframe, command=self.new_game, text="New Game")
        self.ng.pack(side='left', fill='x', expand='1')

        self.sg = Button(bframe, command=self.save_game, text="Save Game")
        self.sg.pack(side='left', fill='x', expand='1')

        self.lg = Button(bframe, command=self.load_game, text="Load Game")
        self.lg.pack(side='left', fill='x', expand='1')

        self.query = Button(bframe, command=self.query_board, text="Set Board Algorithm")
        self.query.pack(side='left', fill='x', expand='1')

        bframe.pack(side='bottom', fill='x', expand='1')
        self.make_grid()
        self.canvas.bind("<Button-1>", self.canvas_click)
        self.canvas.bind("<Key>", self.canvas_key)
        self.current = None
        self.pack()

if __name__ == '__main__':
    board = SudokuBoard()
    tk = Tk()
    gui = SudokuGUI(tk, board)
    gui.mainloop()
