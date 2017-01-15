
def nofun():
    global monat
    monat = "November" # das ist schon
                       # der globale Monat
    print("innerhalb", monat)

monat = "gibtsnet"
nofun()
print("Monat ist", monat)
