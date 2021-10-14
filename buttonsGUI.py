from tkinter import *
window = Tk()

count = 0
def click():
    global count
    count += 1
    print(count)



photo = PhotoImage(file = 'icon.png')
button = Button(window,
                text = "Click Me",
                command = click,
                font = ("Comic Sans", 30),
                fg = "green", 
                bg = "black",
                activeforeground = 'green',
                activebackground = 'black',
                state = ACTIVE,# change it to DISABLED and you will no longer be able to click it
                image = photo,
                compound = "bottom") 
button.pack()
window.mainloop()