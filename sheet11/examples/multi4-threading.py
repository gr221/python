
import time
import random
from threading import Condition, Thread

condi = Condition()

class Pro(Thread):
    def __init__(self,name,*args,**kwargs):
        super(Pro,self).__init__(*args, **kwargs)
        self.name = name

    def run(self):
        global condi
        while True:
            condi.acquire()
            print(self.name, 'waits')
            condi.wait()
            print(self.name, 'done waiting')

class Con(Thread):
    def run(self):
        while True:
            s = random.randint(5,15)
            print("...sleeing", s, "seconds")
            time.sleep(s)
            condi.acquire()
            condi.notify()
            condi.release()


pros = [ ]
for n in range(0,10):
    pros.append(Pro('Pro-%d' % (n,)))

for p in pros:
    p.start()

time.sleep(1)

x = Con()
x.start()


x.join()


for p in pros:
    p.join()

print('value', wert.value)


