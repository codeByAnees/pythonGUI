# canvas is a wdget used to draw graphs, plots, images in a window

from tkinter import *

window = Tk()

canvas = Canvas(window, height = 500, width = 500)
# blueline = canvas.create_line(0, 0, 500, 500, fill = "blue", width = 5)
# redline = canvas.create_line(0, 500, 500, 0, fill = "red", width = 5)
# canvas.create_rectangle(50,50,250,250, fill = 'purple')
# canvas.create_polygon(250,0,500,500,0,500, fill = 'pink', outline = 'black', width = 5)
# you can also predefine points in a variable
#points = [250, 0, 500, 500, 0, 500]
#canvas.create_polygon(points, fill = 'purple', outline = 'black', width = 5)
# canvas.create_arc(2,2,500,500, fill = 'green')
# canvas.create_arc(2,2,500,500, fill = 'green', style = CHORD)
# canvas.create_arc(2,2,500,500, fill = 'green', style = ARC)
# canvas.create_arc(2,2,500,500, fill = 'green', style = PIESLICE, start = 90, extent = 180) # we can change the angle of arc using start
canvas.create_arc(3,3,500,500, fill = 'red', extent = 180, width = 10)
canvas.create_arc(3,3,500,500, fill = 'white', extent = 180,start = 180, width = 10)
canvas.create_oval(190,190,310,310, fill = 'white', width = 10)



canvas.pack()

window.mainloop()