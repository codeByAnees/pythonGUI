from tkinter import *


def doSomething(event):
    #print("You did a thing")
    print("Mouse coordinates: " + str(event.x) + "," + str(event.y)) # it will give us coordinates where we clicked on the window

window = Tk()

# window.bind("<Button-1>", doSomething) # left mouse click
# window.bind("<Button-2>", doSomething) # scroll wheel click
# window.bind("<Button-3>", doSomething) # right mouse click
# window.bind("<ButtonRelease>", doSomething) # if we are clicking on window and when we release that click, message will pop up
# window.bind("<Enter>", doSomething) # it will print when we Enter the window
# window.bind("<Leave>", doSomething) # leave the window
window.bind("<Motion>", doSomething) # where the mouse moved

window.mainloop()