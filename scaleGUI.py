from tkinter import *


def submit():
    print("The temperature is", scale.get(), "degree C")
window = Tk()
hotImage = PhotoImage(file = 'icon.png')
hotLabel = Label(window, image = hotImage)
hotLabel.pack()
scale = Scale(from_= 100,
            to = 0,
            length = 300,
            orient = VERTICAL, # orientation of scale
            font = ("Calibri", 20),
            tickinterval = 10, # adds numeric indicators for value
            #showvalue = 0, # hide current value
            #resolution = 5, # increament of slider
            troughcolor = '#69EAFF', # color of slider
            fg = 'red',
            bg = "#111111")

# the function will set the nob at the desired location i.e. in the center
# if you use any range, by using this formula the nob will always present at the center
scale.set(((scale['from'] - scale['to']) / 2) + scale['to'])
scale.pack()
# coldImage = PhotoImage(file = 'icon.png')
# coldLabel = Label(window, image = coldImage)
# coldLabel.pack()

immmage = PhotoImage(file = "icon.png")
submit_button = Button(window,
                text = "Submit",
                image = immmage,
                command = submit,
                compound = "bottom")
submit_button.pack()


window.mainloop()