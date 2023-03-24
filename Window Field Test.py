import tkinter as tk
import random
from tkinter import *
from PIL import Image, ImageTk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()


# Definitions
def d100():
    x0 = random.randint(1, 100)

    label0 = tk.Label(root, text=x0, font=80)
    canvas1.create_window(200, 150, window=label0)


def d20():
    x1 = random.randint(1, 20)

    #image1 = Image.open("d20.png")
    #dice = ImageTk.PhotoImage(image1)
    label1 = tk.Label(root, text=x1, font=80)
    canvas1.create_window(200, 150, window=label1)


def d12():
    x2 = random.randint(1, 12)

    label2 = tk.Label(root, text=x2, font=80)
    canvas1.create_window(200, 150, window=label2)


def d10():
    x3 = random.randint(1, 10)

    label3 = tk.Label(root, text=x3, font=80)
    canvas1.create_window(200, 150, window=label3)


def d8():
    x4 = random.randint(1, 8)

    label4 = tk.Label(root, text=x4, font=80)
    canvas1.create_window(200, 150, window=label4)


def d6():
    x5 = random.randint(1, 4)

    label5 = tk.Label(root, text=x5, font=80)
    canvas1.create_window(200, 150, window=label5)


def d4():
    x6 = random.randint(1, 4)

    label6 = tk.Label(root, text=x6, font=80)
    canvas1.create_window(200, 150, window=label6)


# Dice Buttons
button0 = tk.Button(text='D100', command=d100)
button0_window = canvas1.create_window(10, 10, anchor=NW, window=button0)

button1 = tk.Button(text='D20', command=d20)
button1_window = canvas1.create_window(10, 50, anchor=NW, window=button1)

button2 = tk.Button(text='D12', command=d12)
button2_window = canvas1.create_window(10, 90, anchor=NW, window=button2)

button3 = tk.Button(text='D10', command=d10)
button3_window = canvas1.create_window(10, 130, anchor=NW, window=button3)

button4 = tk.Button(text='D8', command=d8)
button4_window = canvas1.create_window(10, 170, anchor=NW, window=button4)

button5 = tk.Button(text='D6', command=d6)
button5_window = canvas1.create_window(10, 210, anchor=NW, window=button5)

button6 = tk.Button(text='D4', command=d4)
button6_window = canvas1.create_window(10, 250, anchor=NW, window=button6)

# Close Button
btn = tk.Button(root, text='Close', bd='5', command=root.destroy)
btn.pack(side='top')

root.mainloop()
