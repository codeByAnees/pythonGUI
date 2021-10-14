from tkinter import *
from tkinter import filedialog

def openFile():
    # it will return a string containing filepath where file is located
    # if you pass an argument of intialdir inside askopenfilename(), then it will open that directory that you pass in instead of some random directory
    filepath = filedialog.askopenfilename(initialdir = "D:\\Visual Studio\\Python\\test.txt",
                                          title = "Open File",
                                          filetypes = (("Text files", "*txt"), # text files
                                          ("All files", "*.*")) # all kind of files
                                          )
    # print(filepath)
    file = open(filepath, 'r')
    print(file.read())
    file.close()



window = Tk()

button = Button(window, text = "Open", command = openFile)
button.pack()

window.mainloop()