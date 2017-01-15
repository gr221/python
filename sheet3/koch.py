from turtle import *

def koch_kurve(ordnung,length):
    if ordnung == 0:
        fd(length)
        # fd(length/3)
        # lt(60)
        # fd(length/3)
        # rt(120)
        # fd(length/3)
        # lt(60)
        # fd(length/3)
        return

    koch_kurve(ordnung-1, length/ordnung)
    lt(60)
    koch_kurve(ordnung-1, length/ordnung)
    rt(120)
    koch_kurve(ordnung-1, length/ordnung)
    lt(60)
    koch_kurve(ordnung-1, length/ordnung)
    

def main():
    ordnung = int(input("Gib die Ordnung der Kurve ein: "))
    length = float(input("Gib die Länge der Kurve ein: "))
    koch_kurve(ordnung, length)
    done()

if __name__=="__main__":
    main()
