from tkinter import *

def submit():
    # print("You have ordered " + list_box.get(list_box.curselection()))
    # if you want to select multiple items
    food = []
    for index in list_box.curselection():
        food.insert(index, list_box.get(index))

    print("You have ordered: ")
    for i in food:
        print(i)

def add():
    list_box.insert(list_box.size(), entry_box.get())
    list_box.config(height = list_box.size())


def delete():
    #list_box.delete(list_box.curselection())
    # if you want to delete multiple items
    for index in reversed(list_box.curselection()):
        list_box.delete(index)
    list_box.config(height = list_box.size())


window = Tk()

list_box = Listbox(window,
                   bg = "#f7ffde",
                   font = ("Constantia", 25),
                   width = 12,
                   selectmode = MULTIPLE)
list_box.pack()

list_box.insert(1, "Pizza")
list_box.insert(2, "Pasta")
list_box.insert(3, "Garlic Bread")
list_box.insert(4, "Soup")
list_box.insert(5, "Salad")

list_box.config(height = list_box.size())

entry_box = Entry(window)
entry_box.pack()

add_button = Button(window, text = "Add", command = add)
add_button.pack()

del_button = Button(window, text = "Delete", command = delete)
del_button.pack()

submit_button = Button(window, text = "Submit", command = submit)
submit_button.pack()


window.mainloop()