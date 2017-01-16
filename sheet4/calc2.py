from tkinter import *
import operator

wert = 0
op = 0
calculator = Tk()
operators={"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

screen = Label(calculator)
val =StringVar()
# variables=[]
screen.configure(textvariable=val)
screen.grid(row=6, column=1, columnspan=3)
val.set(0)

def set_val(num):
    if val.get() in ['+', '-', '*', '/', '=']:
        val.set(0)
    zahl=float(val.get())
    zahl=zahl*10+num
    val.set(zahl)
    # variables.append(val)

def set_operation(sign):
    if op != 0:
        wert = op(wert, float(val.get()))
        print(wert)

    if sign == '=':
        val.set(wert)

    else:
        global op
        global wert
        wert = float(val.get())
        val.set(sign)
        op = operators[sign]
        print(op)
j=1

for sign in ['+', '-', '*', '/', '=']:
    button = Button(calculator, text=sign, command=lambda sign=sign: set_operation(sign))
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
