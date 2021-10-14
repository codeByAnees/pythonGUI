from tkinter import *

def openFile():
    print("The file has openend")

def saveFile():
    print("The file is saved")

def cut():
    print("You cut some text")

def copy():
    print("You copied something")

def paste():
    print("You pasted something")


window = Tk()

openImage = PhotoImage(file = 'icon.png')
saveImage = PhotoImage(file = 'icon.png')
exitImage = PhotoImage(file = 'icon.png')

menubar = Menu(window)
window.config(menu = menubar)

filemenu = Menu(menubar, tearoff=0, font = ("MV Boli", 15))
menubar.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = 'Open', command = openFile, image = openImage, compound = 'left')
filemenu.add_command(label = "Save", command = saveFile, image = saveImage, compound = "left")
filemenu.add_separator() # you can add it to separate different options
filemenu.add_command(label = 'Exit', command = quit, image = exitImage, compound = "left")

editMenu = Menu(menubar, tearoff= 0, font = ("MV Boli", 15))
menubar.add_cascade(label = "Edit", menu = editMenu)
editMenu.add_command(label = "Cut", command = cut)
editMenu.add_command(label = "Copy", command = copy)
editMenu.add_command(label = "Paste", command = paste)


window.mainloop()