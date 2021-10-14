# Radio button = similar to checkbox, but you can only select one from a group
from tkinter import *

food = ["Pizaa", "Hamburger", "Hotdogs"]
def order():
    if x.get() == 0:
        print("You ordered Pizza")
    elif x.get() == 1:
        print("You ordered Hamburger")
    elif x.get() == 2:
        print("You ordered Hotdogs")
    else:
        print("Huh?")

window = Tk()
x = IntVar()
pizzaImage = PhotoImage(file = "icon.png")
hamburgerImage = PhotoImage(file = 'icon.png')
hotDogsImage = PhotoImage(file = 'icon.png')
foodImages = [pizzaImage, hamburgerImage, hotDogsImage]

for index in range(len(food)):
    radio_button = Radiobutton(window,
                text = food[index],
                variable = x, # group radiobuttons together if they share the same variable
                value = index,# assigns each radiobutton a different value
                padx = 25,
                font = ("Impact", 50),
                image = foodImages[index],
                compound = "left",# adds image and text
                indicatoron = 0, # eliminate circle indicator if you want
                width = 380, # sets width of radio buttons
                command = order) # sets command of rdio button to function
    radio_button.pack(anchor = W)

window.mainloop()