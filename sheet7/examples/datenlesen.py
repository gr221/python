
f = open("data.dat", "r")

zeilen = f.readlines()
f.close()

for zeile in zeilen:
    worte = zeile.split()
    print("wort1:", worte[0], "wort2:", worte[1])
