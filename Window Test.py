import tkinter
from tkinter import *
from PIL import Image, ImageTk

# Create a window
window = Tk()

# Size window
window.geometry("500x500")

# Name a window
window.title("Dice Bag")

# create a button to destroy window
btn = Button(window, text='Click Me!', bd='5', command=window.destroy)

# set position of button to top of window
btn.pack(side='top')

# Create a photo image object of the image in the path
image1 = Image.open("d20.png")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

# Position Image
label1.place(x=120, y=75)

window.mainloop()
