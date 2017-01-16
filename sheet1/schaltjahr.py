print("Gib eine Jahreszahl ein: ")
year = input()
print(year)
if (int(year) % 4 == 0):
    if (int(year) % 100 == 0):
        if(int(year) % 400 == 0):
            print(year, "ist ein Schaltjahr\n")
        else:
            print(year, "ist kein Schaltjahr\n")
    else:
        print(year, "ist ein Schaltjahr\n")
else:
    print(year, "ist kein Schaltjahr\n")
