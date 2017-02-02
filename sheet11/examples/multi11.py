
import time
import multiprocessing as m

#wert = 0
wert = m.Value('i', 0)
#wert.value = 0

class Pro(m.Process):
    def run(self):
        global wert
        wert.value = wert.value + 1


pros = [ ]
for n in range(0,100):
    pros.append(Pro())

for p in pros:
    p.start()

for p in pros:
    p.join()

print('value', wert.value)
#print wert


