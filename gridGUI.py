from tkinter import *

# grid() = geometry manager that organizes widgets in a table like structure
window = Tk()

titleLabel = Label(window, text = "Enter your Info", font = ("Arial", 30)).grid(row = 0, column = 0, columnspan = 2)

firstNameLabel = Label(window, text = "First Name", width = 20, bg = "green").grid(row = 1, column = 0)
firstNameEntry = Entry(window).grid(row = 1, column = 1)

lastNameLabel = Label(window, text = "Last Name", bg = "blue").grid(row = 2, column = 0)
lastNameEntry = Entry(window).grid(row = 2, column = 1)

emailLabel = Label(window, text= "Email", bg = "red").grid(row = 3, column = 0)
emailEntry = Entry(window).grid(row = 3, column = 1)

Button(window, text = "Submit").grid(row = 4, column = 0, columnspan = 2)






window.mainloop()













