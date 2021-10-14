from tkinter import *
# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets


window = Tk()   # instantiate an instance of a window
window.geometry("520x520")
window.title("Anees first GUI Program")
icon = PhotoImage(file='C:\\Users\\DELL\\Downloads\\icon.png')
window.iconphoto(True, icon)
window.config(background='#5cfcff') # you can use any hex color value to change the background color
window.mainloop()   # place window on computer screen