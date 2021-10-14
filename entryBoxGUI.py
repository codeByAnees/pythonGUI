from tkinter import *

def Submit():
    username = entry.get() # it will return string that you enter
    print("Hello", username)
    # we can also disable entry box after entring name
    #entry.config(state = DISABLED)

def delete():
    entry.delete(0, END)
    
def backspace():
    entry.delete(len(entry.get())-1, END)


window = Tk()
entry = Entry(window,
        font = ('Calibri', 30),
        fg = "green",
        bg = 'black',
        show = "*" # it will not show the text we are entring but instead will show the character we put in here
        ) 
# we can insert default text
# entry.insert(0, "Anees")
entry.pack(side = LEFT)


submit_button = Button(window,
                text = "Submit",
                command = Submit)
submit_button.pack(side = RIGHT)


delete_button = Button(window,
                text = "Delete", 
                command = delete)
delete_button.pack(side = RIGHT)


backspace_button = Button(window,
                text = "Backspace", 
                command = backspace)
backspace_button.pack(side = RIGHT)
















window.mainloop()