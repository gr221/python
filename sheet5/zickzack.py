import turtle
class Schildkroete(turtle.Turtle):
    def __init__(self):
        super().__init__()

    def zickzack(self, length,height, number):
        for i in range(0, number):
            self.fd(length/number)
            self.lt(90)
            self.fd(height)
            self.rt(90)
            self.fd(length/number)
            self.rt(90)
            self.fd(height)
            self.lt(90)

s = Schildkroete()
s.fd(100)
s.zickzack(100, 20, 50 )
s.done()


