from tkinter import *


def doSomething(event):
    #print("You pressed: " + event.keysym) # it will write every key you press in the console
    label.config(text = event.keysym)



window = Tk()
# bind(event, function)
window.bind("<Key>", doSomething)
label = Label(window, font = ("Arial", 100))
label.pack()


window.mainloop()