
f = open("meins", "w")

f.write("bla\n")
f.write("bla\n")
print("ohaa", file=f)
print(7.0, file=f)
#f.write(7.0)  # so  nicht!

f.write(str(7.0)) # so schon,
# Konstruktur der Klasse str wird aufgerufen.

f.flush()
f.close()

