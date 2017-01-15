from tkinter import *
wert = 0.0
oper = 0.0

app = Tk()

def bla():
    va.set("blabla")

b = Button(app)
b.configure(text="Schalter")
b.configure(command=bla)
b.grid(column=1,row=1)

la = Label(app)
va = StringVar()
la.configure(textvariable=va)
la.grid(column=1,row=5,columnspan=3)


mainloop()
