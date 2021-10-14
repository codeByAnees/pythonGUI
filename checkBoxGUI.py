from tkinter import * 

def display():
    if (x.get() == 1):
        print("You agree!")
    else:
        print("You don't agree :)")


window = Tk()
x = IntVar() # StringVar, BooleanVar
photo = PhotoImage(file = 'icon.png')
check_button = Checkbutton(window,
            text = "I agree to this",
            font = ("Arial", 20),
            variable = x, # you can also use string or boolean value here
            onvalue = 1,
            offvalue = 0,
            command = display,
            fg = '#00ff00',
            bg = 'black',
            activeforeground = '#00ff00',
            activebackground = 'black',
            padx = 25,
            pady = 10,
            image = photo,
            compound = 'left')
check_button.pack()

window.mainloop()