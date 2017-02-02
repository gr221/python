
import time
import multiprocessing as m

wert = m.Value('i', 0)
l = m.Lock()
wert.value = 0

class Pro(m.Process):
    def run(self):
        global value
        time.sleep(0.1)
        l.acquire()
        wert.value = wert.value + 1
        l.release()


pros = [ ]
for n in range(0,100):
    pros.append(Pro())

for p in pros:
    p.start()

for p in pros:
    p.join()

print('value', wert.value)


