import collatz
import pylab as pl

startwert =[]
length=[]
for i in range(1,10001):
    folge = collatz.Collatz(i)
    startwert.append(i)
    length.append(folge.length())

pl.xlabel('Startwert')
pl.ylabel('Länge')
pl.title('Lände der Collatz Sequenzen')
pl.plot(startwert,length,'ro', markersize=4 )
pl.show()


