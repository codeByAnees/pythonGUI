from tkinter import *

def create_window():
    # new_window = Toplevel() # it creates a 'new window' on top of other window, usually linked to a 'bottom window'
    new_window = Tk() # it creates a new independant window which is not relied on bottom window
    window.destroy() # close out of old window



window = Tk()

Button(window, text = "Create New Window", command = create_window).pack()

window.mainloop()