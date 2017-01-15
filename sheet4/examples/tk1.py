from tkinter import * 

def tuwas():
    print('ahaha')

def wasanderes():
    print("ohohoh")

root = Tk()
b = Button(root)
b.configure(text="mein Schalter")
b.configure(command=tuwas)
#b.pack()
b.grid(column=1,row=1)
c = Button(root)
c.configure(text="noch einer",
        command=wasanderes)
#c.pack()
c.grid(column=2,row=1)

root.mainloop()

