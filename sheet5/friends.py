import time

class Mensch(object):
    def __init__(self,name, tag, monat):
        super().__init__()
        self.name = name
        self.tag = tag
        self.monat = monat

class Freund(Mensch):
    def __init__(self,name,tag,monat ):
        super().__init__(name,tag,monat)

class Verwandt(Freund):
    def __init__(self,name, tag, monat,  grad):
        super().__init__(name,tag,monat)
        self.grad = grad

menschen = list()
menschen.append(Mensch('Stefan', tag=1, monat=1))
menschen.append(Freund('Deine Mama', 4, 12))
menschen.append(Verwandt('Meine Mama', tag=19, monat=1, grad='Muada'))

day=time.localtime().tm_mday
month=time.localtime().tm_mon

for a in menschen:
    if  (a.tag == day) and (a.monat == month):
        print(a.name, " hat heute Geburtstag.")
