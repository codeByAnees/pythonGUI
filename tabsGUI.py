from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window) # widget that manages a collection of windows and displays

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text = "Tab 1")
notebook.add(tab2, text = "Tab 2")
notebook.pack(expand = True, fill = "both") # it expands to fill any space not otherwise used
                                            # fill func will fill space on x and y axis and tabs will remain on top left corner

# adding some text to tabs
Label(tab1, text = "This is Tab 1", width = 50, height = 25).pack()
Label(tab2, text = "This is Tab 2", width = 50, height = 25).pack()


window.mainloop()