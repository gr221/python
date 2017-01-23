
class Vektor(object):
    def __init__(self,a,b,c):
        self.data = [a,b,c]
    def __mul__(self,other):
        if isinstance(other, Vektor):
            ergebnis = 0.0
            for i in range(0,3):
                ergebnis = ergebnis + \
                        self.data[i] * other.data[i]
            return ergebnis
        else:
            return Vektor(other*self.data[0],
                    other*self.data[1],
                    other*self.data[2])
    def __rmul__(self,other):
        return self.__mul__(other)

if __name__ == '__main__':
    # wird igoriert, wenn Datei "vektoren.py"
    # nur importiert wird.
    #
    a = Vektor(1,2,3)
    b = Vektor(0.1, 0.01, 0.001)

    x = 3*a           #so nicht!
    # x = 3.__mul__(a)  so nicht!
    y = a*3           #so nicht!
    #y = a.__mul__(3)  #so nicht!
    print(y.data)
    s = a * b
    #s = a.__mul__(b)
    print("Skalarprodukt ist:", s)
    print()
