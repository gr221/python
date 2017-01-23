grundgesetz = open("grundgesetz.txt","r")
text = grundgesetz.readlines()
zeilen = len(text)
woerter = 0
zeichen = 0
for i in range(0,zeilen):
    woerter += len(text[i].split())
    for j in text[i]:
        if j != ' ':
            zeichen += 1

print("Das Grundgesetz hat ", zeilen, " Zeilen,  ", woerter, " Wörter und ", zeichen, " Zeichen.")

grundgesetz.close()
