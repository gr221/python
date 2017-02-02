
import time
import threading as th

wert = 0
mtx = th.Lock()
class Pro(th.Thread):
    def run(self):
        global wert, mtx
        mtx.acquire()
        buf = wert
        time.sleep(0.1)
        wert = buf + 1
        mtx.release()


pros = [ ]
for n in range(0,100):
    pros.append(Pro())

for p in pros:
    p.start()

for p in pros:
    p.join()

print('value', wert)


