from tkinter import *

class Taschenrechner(object):
    def __init__(self,app):
        screen = Label(app)
        self.user_input = 0
        val =StringVar()
        screen.configure(textvariable=val)
        screen.grid(row=6, column=1, columnspan=3)
        for index in [1,2,3,4,5,6,7,8,9,0]:
            b = Button(app)
            b.configure(text=index)
            b.configure(command=lambda index=index : self.set_val(index, val))
            # b.configure(command= self.set_val(index, val,user_input))
            b.grid(column=(index-1)%3+1,row=(index-1)//3+1)
        b.grid(column=2,row=4)
        self.wert = 0

    def set_val(self,index,val,):
        print(self.user_input)
        print(index)
        self.user_input = 10*self.user_input +index
        print(self.user_input)
        val.set(self.user_input)


app = Tk()
calc = Taschenrechner(app)
mainloop()
