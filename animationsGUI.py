from tkinter import *
import time


WIDTH = 500
HEIGHT = 500
xVelocity = 3
yVelocity = 2

window = Tk()


canvas = Canvas(window, width = WIDTH, height = HEIGHT)
canvas.pack()

back_imagge = PhotoImage(file = 'icon.png')
background_image = canvas.create_image(0, 0, image = back_imagge, anchor = NW)

imagge = PhotoImage(file = 'craftt.png')
my_image = canvas.create_image(0, 0, image = imagge, anchor = NW)

image_width = imagge.width()
image_height = imagge.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if (coordinates[0] >= (WIDTH - image_width)  or coordinates[0] < 0):
        xVelocity = -xVelocity
    if (coordinates[1] >= (HEIGHT - image_height)  or coordinates[1] < 0):
        yVelocity = -yVelocity
    # canvas.move(my_image, xVelocity, 0)
    # canvas.move(my_image, 0, yVelocity)
    canvas.move(my_image, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()