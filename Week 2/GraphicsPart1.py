# Graphics in Tkinter Part 1
# Create an Empty Canvas

from tkinter import *

def draw(canvas, width, height):
    # create_line (x1, y1, x2, y2) draws a line 
    #   from (x1, y1) to (x2, y2)
    canvas.create_line(25, 50, width/2, height/2)

def runDrawing(width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("bye!")

runDrawing(400, 200)

from tkinter import *

def draw(canvas, width, height):
    pass # replace with your drawing code!

def runDrawing(width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()
    print("bye!")

runDrawing(400, 200)
