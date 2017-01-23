import pylab as pl

phys = {
        'm': [87, 166, 41, 127, 27, 89, 13, 34, 18],
        'f': [38,  43, 12,  15,  4, 14,  2,  3,  0]
        }
labels = 'Male', 'Female'

for i in range(1,10):
    x=330+i
    sizes = [phys['m'][i-1], phys['f'][i-1]]
    pl.subplot(x)
    title = "Semster " +str(i)
    pl.title(title)
    pl.pie(sizes, labels = labels,autopct='%.2f%%', radius = 1)

pl.show()
