from tkinter import messagebox
from tkinter import *


def click():
    #messagebox.showinfo(title = "Message Box", message = "You're a Person!")
    #messagebox.showwarning(title = "WARNING", message = "You've a virus!")
    #messagebox.showerror(title = "ERROR", message = "Something went WRONG!")
    # if messagebox.askokcancel(title = "ASK OK CANCEL", message = "Do youw want to do the thing!"):
    #     print("You did a thing")
    # else:
    #     print("You canceled a thing")
    # if messagebox.askretrycancel(title = "Ask ok cancel", message = "Do you want to retry the thing!"):
    #     print("You retried a thing")
    # else:
    #     print("You canceled a thing")]
    # if messagebox.askyesno(title = "Ask yes or No", message = "Do you like cake!"): # return boolean value
    #     print("I like cake too!")
    # else:
    #     print("Why do you not like the cake?")
    # answer = (messagebox.askquestion(title = "Ask Question", message = "Do you like pie?"))
    # if answer == 'yes':
    #     print("I l ike pie too!")
    # else:
    #     print("Why do you not like the pie?")
    answer = messagebox.askyesnocancel(title = "Yes No Cancel", message = "Do you like to code?", icon = 'error') # can change the icons like warning, erroe, info etc
    if answer == True:
        print("I also like to code!")
    elif answer == False:
        print("Then why are you watching a coding lesson?")
    else:
        print("You doged the question ")

window = Tk()

button = Button(window, text = "Click Me", command = click)
button.pack()



window.mainloop()

