from tkinter import *

def drag_start(event):
    # this is going to get the widget of the event we are dealong with
    # without this line we will not be able to move more than one widgets
    widget = event.widget
    # getting coordinates of where we click
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    # 1) top left x-coordinate of widget. 2) place where we click within label. 3) this is where we begin dragging widget
    x = widget.winfo_x() - widget.startX + event.x 
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x = x, y = y)


window = Tk()


label = Label(window, bg = "red", width = 10, height = 5)
label.place(x = 0, y = 0)

label_2 = Label(window, bg = "blue", width = 10, height = 5)
label_2.place(x = 100, y = 100)

label.bind("<Button-1>", drag_start)
label.bind("<B1-Motion>", drag_motion)

label_2.bind("<Button-1>", drag_start)
label_2.bind("<B1-Motion>", drag_motion)

window.mainloop()