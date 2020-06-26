"""
program:  project.py
author:  Lisa Kilmer
last modified:  June 26, 2020
This is a GUI project that uses tkinter builtin Python.  It is a box called Favorite Meal with
4 check boxes.  Breakfast, Second Breakfast, Lunch and Dinner.  It says 'Waiting' till a box
is checked then changes to the message for the box checked.  It has an exit button in row 6.
"""

import tkinter

def pick_Breakfast(): # for the Breakfast choice
    label.config(text="Nice choice")

def pick_SecondBreakfast():  #for the second breakfast choice
    label.config(text="Something special!")

def pick_Lunch():  #for Lunch choice
    label.config(text="Are you sure?")

def pick_Dinner():  #for Dinner choice
    label.config(text="so good!")

m = tkinter.Tk() # where m is the name of the main window object
m.title('Favorite Meal')
label = tkinter.Label(m, text="Waiting")
label.grid(row=5)
var1 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Breakfast", variable=var1, command=pick_Breakfast).grid(row=0)
var2 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Second Breakfast", variable=var2, command=pick_SecondBreakfast).grid(row=1)
var3 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Lunch", variable=var3, command=pick_Lunch).grid(row=2)
var4 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Dinner", variable=var4, command=pick_Dinner).grid(row=3)
exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=6)
m.mainloop()  # infinite loop that waits for events to happen




