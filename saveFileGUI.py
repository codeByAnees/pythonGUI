from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir = "D:\\Visual Studio\\Python",
                                defaultextension = '.txt', 
                                filetypes = [
                                    ("Text file", ".txt"),
                                    ("HTML files", ".html"),
                                    ("All files", "*.*")
                                ])
    if file is None:
        return
    # we can also use console to write into file by commenting the line below
    # fileText = str(text.get("1.0", END))
    fileText = input("Enter some text: ")
    file.write(fileText)
    file.close()


window = Tk()

button = Button(window, text = "Save", command = saveFile)
button.pack()
text = Text(window)
text.pack()

window.mainloop()