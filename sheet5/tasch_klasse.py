from tkinter import *
import operator

class Taschenrechner(object):
    def __init__(self,app):
        self.user_input = 0
        self.value = 0
        self.tmp_value = 0
        self.operator = None
        self.operators={"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

        screen = Label(app)
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

        i=0
        for sign in ['+', '-', '*', '/', '=']:
            button = Button(app, text=sign, command=lambda sign=sign: self.set_operator(sign,val)) 
            i = i+1
            if i == 5:
                button.grid(column=3, row = i-1)
            else:
                button.grid(column=4, row =i)

        b = Button(app, text = 'clear', command=lambda: self.clear_stuff(val))
        b.grid(column=1, row =4)

    def set_val(self,index,val):
        self.user_input = 10*self.user_input +index
        val.set(self.user_input)

    def set_operator(self, sign,val):
        if not self.operator:
            self.value = self.user_input
            self.user_input = 0
            self.operator= self.operators[sign]

        elif sign == '=':
            self.value = self.operator(self.value, self.user_input)
            val.set(self.value)
            self.user_input=0

        else:
            self.value = self.operator(self.value, self.user_input)
            self.user_input = 0
            self.operator = self.operators[sign]
            val.set(sign)

    def clear_stuff(self,val):
        self.user_input = 0
        self.value = 0
        self.tmp_value = 0
        self.operator = None
        val.set(self.value)

app = Tk()
calc = Taschenrechner(app)
mainloop()
