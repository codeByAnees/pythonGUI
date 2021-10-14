from tkinter import *
# labels = an area widget that holds text and/or an image within a window
window = Tk()
photo = PhotoImage(file = 'icon.png')
label = Label(window, 
        text = "Anees GUI's",
        font = ("Calibri", 30, "bold"),
        fg = '#00FF00',         # font color
        bg = "black",           # text background color (hex color value can also be used)
        relief = RAISED,        # adding border style (SUNKEN is another type)
        bd = 10,                # border width
        padx = 20,              # add some space on the two sides between text and border
        pady = 20,              # add some space above and below between text and border
        image = photo,
        compound = 'bottom' 
        ) 
label.pack()                    # this function will add text text to window and by default in center of window
# label.place(x = 0, y = 0)     # it will place the text according to defined coordinates pixels
window.mainloop()
