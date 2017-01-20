from tkinter import *

class Taschenrechner(object):
    def __init__(self,app):
        screen = Label(app)
        val =StringVar()
        screen.configure(textvariable=val)
        screen.grid(row=6, column=1, columnspan=3)
        val.set(0)
        for index in [1,2,3,4,5,6,7,8,9,0]:
            b = Button(app)
            b.configure(text=str(index))
            b.configure(command=self.set_val(index))
            b.grid(column=(index-1)%3+1,row=(index-1)//3+1)
        b.grid(column=2,row=4)
        self.wert = 0

    def set_val(self,index):
        def protect():
            val.set(index)


app = Tk()
calc = Taschenrechner(app)
mainloop()
