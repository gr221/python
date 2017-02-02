
import time
import threading as th

wert = 0
class Pro(th.Thread):
    def run(self):
        global wert
        buf = wert
        time.sleep(0.0001)
        wert = buf + 1


pros = [ ]
for n in range(0,100):
    pros.append(Pro())

for p in pros:
    p.start()

for p in pros:
    p.join()

print('value', wert)


