from tkinter import *
wert = 0.0
oper = 0.0

app = Tk()

def tuwas(i):
    def anon():
        global wert, va
        wert = wert * 10 + i
        va.set(str(wert))
    return anon

def tuwasc():
    global wert, oper
    wert = 0
    oper = 0
    va.set(str(wert))

def tuwasp():
    global wert, oper
    oper = oper + wert
    wert = 0
    va.set(str(oper))
    print(oper)

for index in [1,2,3,4,5,6,7,8,9,0]:
    b = Button(app)
    b.configure(text=str(index))
    b.configure(command=tuwas(index))
    b.grid(column=(index-1)%3+1,row=(index-1)//3+1)
b.grid(column=1,row=4)


bc = Button(app)
bc.configure(text="c")
bc.configure(command=tuwasc)
bc.grid(column=2,row=4)

bp = Button(app)
bp.configure(text="p")
bp.configure(command=tuwasp)
bp.grid(column=3,row=4)

la = Label(app)
va = StringVar()
la.configure(textvariable=va)
la.grid(column=1,row=5,columnspan=3)

mainloop()
