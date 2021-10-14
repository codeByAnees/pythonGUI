# frame = a rectangular container to group and hold widgets
# if we do not use frame, the widgets will not appear togethar on window
from tkinter import *

window = Tk()

frame = Frame(window, bg = "pink", bd = 5, relief = SUNKEN)
#frame.pack() # you can use this to place frame on desired location inside window
frame.place(x = 0, y = 0) # it is also used to place frame on different location inside window using coordinates
Button(frame, text = "W", font = ("Consolas", 25), width = 3).pack(side = TOP)
Button(frame, text = "A", font = ("Consolas", 25), width = 3).pack(side = LEFT)
Button(frame, text = "S", font = ("Consolas", 25), width = 3).pack(side = LEFT)
Button(frame, text = "D", font = ("Consolas", 25), width = 3).pack(side = LEFT)

window.mainloop()
