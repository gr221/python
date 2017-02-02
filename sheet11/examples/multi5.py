
import time
import random
import multiprocessing as m


ernie,bert = m.Pipe()

class Pro(m.Process):
    def run(self):
        global ernie
        for ding in [7, 3.14, ['arry',123], "nix"]:
            ernie.send(ding)
            x = ernie.recv()
            print('pro got', x)

class Con(m.Process):
    def run(self):
        global bert
        for ding in [2.7, "was?", "egal", {'d':1, 'c':7} ]:
            x = bert.recv()
            print('con got', x)
            bert.send(ding)

p = Pro()
c = Con()

print("---------------------")
p.start()
c.start()

c.join()
p.join()
print(".....................")
