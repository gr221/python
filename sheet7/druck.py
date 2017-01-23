import pylab as pl
tabelle = open("druckrack.txt", "r")
data = tabelle.readlines()
tabelle.close()

data = data[3:-2]
# for i in range(0,3):
#     data.pop(0)
# print(data)
messwerte = []
time = []
for zeile in range(0, len(data)):
    tmp = data[zeile].split()
    messwerte.append(tmp[3])
    time.append(zeile*30)

pl.xlabel("Zeit [m]")
pl.ylabel("Messwerte")
pl.title("Druckrack")
pl.plot(time, messwerte)
pl.show()

