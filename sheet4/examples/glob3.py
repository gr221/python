
def nofun():
    monat = "November" # das ist nicht
                       # der globale Monat
    print("innerhalb", monat)

monat = "gibtsnet"
nofun()
print("Monat ist", monat)
