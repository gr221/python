# https://de.wikipedia.org/wiki/Collatz-Problem
class Collatz(object):
    def __init__(self, n):
        self.start = n
        self.seq= [ ]
        i = n
        self.lg = 0
        while i != 1:
            self.seq.append(i)
            self.lg += 1
            if i % 2 == 0:
                i = i//2
            else:
                i = 3*i+1

    def sequence(self):
        return self.seq

    def length(self):
        return self.lg

if __name__ == '__main__':
    maxlen = 0
    maxwert = 0
    for j in range(1,10001):
        folge = Collatz(j)
        if folge.length() > maxlen:
            maxlen = folge.length()
            maxwert = j

    print('maximale laenge:', maxlen)
    print('folge:', Collatz(maxwert).sequence())
    print(Collatz(7).sequence())
