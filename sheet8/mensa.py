import matplotlib.pyplot as plt
import numpy as np
f = open("mensaplan50.csv", "r")
essen = f.readlines()
f.close()
#Dicts für die Wwerte
zahl_essen={'Mo': 0, 'Di': 0, 'Mi': 0, 'Do': 0, 'Fr': 0}
zahl_veggie={'Mo': 0, 'Di': 0, 'Mi': 0, 'Do': 0, 'Fr': 0}
essen.pop(0)
#Zähle wie viele essen es gibt und wie viele veggie essen
for i in range(0,len(essen)):
    zahl_essen[essen[i].split(';')[1]] +=1
    if essen[i].split(';')[4] == 'V' or essen[i].split(';')[4]=='VG':
        zahl_veggie[essen[i].split(';')[1]] +=1

#Plotten
index = ['Mo', 'Di', 'Mi', 'Do', 'Fr']
left= np.linspace(0,4,5)
bar_width=0.4
rect1 = plt.bar(left-bar_width/2, zahl_essen.values(),width=bar_width, label='Essen',color='y')
rect2 = plt.bar(left+bar_width/2, zahl_veggie.values(),width=bar_width, label='Veggie', color='g')
plt.xticks(range(len(zahl_essen)), index)
plt.legend()
plt.show()
