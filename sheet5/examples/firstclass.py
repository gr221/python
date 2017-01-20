
class Person(object):
    def __init__(self, name='foo',wiealt=0):
        self.name = name
        self.alter = wiealt

    def pension(self):
        return 67 - self.alter

    def sagwas(self, satz):
        return self.name+'sagt '+satz

class Student(Person):
    def __init__(self,heisst='bar',istalt=18,
            matrikel=0):
        super(Student,self).__init__(
                name=heisst,
                wiealt=istalt)
        self.matno = matrikel

ich = Person("Stefan", 38)
er = Person("Robert", 30)
jemand = Person()
print()
print(ich.name, ich.alter)
print(er.name, er.alter)
print(jemand.name, jemand.alter)
print()
print(ich.name,'pension in', ich.pension())
print(er.name, 'pension in', er.pension())
print(ich.sagwas("heute ist Freitag"))
print()
peter = Student('Peter',23, 12345)
print(peter.sagwas("fast zu Ende"))
print()
print( type(peter) )
print( type(ich)   )
if type(peter) == type(ich):
    print('gleich')
else:
    print('ungleich')
print()
if isinstance(peter, Person):
    print("peter ist Person")
else:
    print("peter ist keine Person")
print()
