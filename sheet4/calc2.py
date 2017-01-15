from tkinter import *


calculator = Tk()

screen = Label(calculator)
val =StringVar()
screen.configure(textvariable=val)
screen.grid(row=6, column=1, columnspan=3)

def set_val(num):
    val.set(num)

j=1

for sign in ['+', '-', '*', '/']:
    button = Button(calculator, text=sign, command=lambda sign=sign: set_val(sign))
    button.grid(row=1, column=j)
    j+=1

i=2
j=1
for num in range(1,10):
    button = Button(calculator)
    button.configure(text=num) 
    button.configure(command=lambda num=num: set_val(num))
    button.grid(row=i, column=j)
    if j==3:
        i += 1
        j=1
    else:
        j += 1

button = Button(calculator)
button.configure(text="0")
button.configure(command=lambda: set_val(0))
button.grid(row=5, column=2)


mainloop()
