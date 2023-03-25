import tkinter
from tkinter import *
from PIL import Image, ImageTk
# from DiceRoller import diceroller
from DiceRoller import d20


# Create a window
window = Tk()

# Size window
window.geometry("500x500")

# Name a window
window.title("Dice Bag")

# create a button to destroy window
btn = Button(window, text='END', bd='5', command=window.destroy)
roll = Button(window, text= 'D20', bd='5', command=d20)

# set position of button to top of window
btn.pack(side='top')
roll.pack(side='top')

# Create a photo image object of the image in the path
image1 = Image.open("d20.png")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

# Position Image
label1.place(x=120, y=75)

window.mainloop()
