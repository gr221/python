def fib_rekursiv(ordnung):
    if (ordnung == 2) or (ordnung == 1):
        return 1
    zahl = fib_rekursiv(ordnung-1) + fib_rekursiv(ordnung-2)
    return zahl

def main():
    ordnung = int(input("Gib die letzte zu berechnende Fibonacci Zahl ein: "))
    for i in range (1, ordnung+1):
        print(fib_rekursiv(i))

if __name__=="__main__":
    main()
