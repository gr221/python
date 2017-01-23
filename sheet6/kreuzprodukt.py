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

    def __mod__(self, other):
        ergebnis = Vektor(0,0,0)
        if isinstance(other, Vektor):
            ergebnis.data[0] = self.data[1]*other.data[2] - self.data[2]*other.data[1]
            ergebnis.data[1] = self.data[2]*other.data[0] - self.data[0]*other.data[2]
            ergebnis.data[2] = self.data[0]*other.data[1] - self.data[1]*other.data[0]
            return ergebnis
        else:
            print("Kreuzprodukt ist nur für Vektoren definiert.")

    def spatprodukt(self, other, third):
        if isinstance(other, Vektor) and isinstance (third,Vektor):
            spat=0
            tmp = self.__mod__(other)
            print(tmp.data)
            print(other.data)
            spat= tmp.__mul__(third)
            return spat
        else:
            print("Brauche 3 Vektoren")


if __name__=="__main__":
    a = Vektor(1,2,3)
    b = Vektor(1,1,1)
    c = Vektor(2,2,1)
    s = a%b
    print("Kreuzprodukt von ", a.data, " und ", b.data, " ist ", s, ".")

    volumen = a.spatprodukt(b,c)
    print("Volumen: ", volumen)

