class Collatz(object):
    def __init__(self, start):
        self.numbers = [start]

    def sequence(self):
        while self.numbers[-1] != 1:
            if (self.numbers[-1] % 2 == 0):
                self.numbers.append(self.numbers[-1] /2)
            else:
                self.numbers.append(self.numbers[-1]*3 +1)

        return self.numbers

    # def length(self):
    #     print(len(self.numbers))

def main():
    longest =[]
    length = 0
    tmp =[]
    for i in range(1, 10000):
        collatz_sequence = Collatz(i)
        tmp = collatz_sequence.sequence()
        print("Start: ", i, " Length: ", len(tmp))
        if (len(tmp) > len(longest)):
            longest.clear()
            longest = tmp

    print("Die Längste Sequenz beginnt bei: ", longest[0], " und ist ", len(longest), " lang.")
    print("Sie ist: ", longest)

if __name__=="__main__":
    main()

