
f = open("meins", "r")

zeilen = f.readlines()
f.close()

print(zeilen)

nummer = 1
for zeile in zeilen:
    print(nummer, zeile, end='')
    nummer = nummer + 1

    
