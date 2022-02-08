from tkinter import *


def button_press():
    product = float(input.get()) * 1.6
    number.config(text=f'{product}')


window = Tk()
window.title('Miles to KM converter')
window.minsize(200, 100)

blank = Label(text= '')
blank.grid(column= 0, row=0)

equal = Label(text='is equal to', font=('Arial', 12))
equal.grid(column=0, row=1)
equal.grid(padx=1)

number = Label(text = 0)
number.grid(column = 1, row = 1)

km = Label(text = 'KM')
km.grid(column=2, row= 1)
km.grid(padx=1)

button = Button(text='Calculate', command=button_press)
button.grid(column=1, row=2)

input = Entry(width=9)
input.get()
input.grid(column=1, row=0)

miles = Label(text = 'miles')
miles.grid(column=2,row = 0)


window.mainloop()
