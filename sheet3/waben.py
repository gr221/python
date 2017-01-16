from turtle import *
from math import *
def zeichne_wabe(pos_x, pos_y, length):
    pu()
    setx(pos_x)
    sety(pos_y)
    pd()
    fd(length)
    rt(60)
    fd(length)
    rt(60)
    fd(length)
    rt(60)
    fd(length)
    rt(60)
    fd(length)
    rt(60)
    fd(length)
    rt(60)

def main():
    pos_x = 0
    pos_y = 0
    start_y = 0
    length = float(input("Gib die Länge der Waben ein: "))
    number_horizontal = int(input("Gib die Anzahl der Waben in horizontaler Richtung ein: "))
    number_vertical = int(input("Gib die Anzahl der Waben in vertikaler Richtung ein: "))
    for j in range(0, number_vertical):
        for i in range(0, int(number_horizontal/2)):
            zeichne_wabe(pos_x, pos_y, length)
            pos_x = pos_x + sqrt(3)*length*cos(330*pi/180)
            pos_y = pos_y + sqrt(3)*length*sin(330*pi/180)
            zeichne_wabe(pos_x, pos_y, length)
            pos_x = pos_x + sqrt(3)*length*cos(30*pi/180)
            pos_y = pos_y + sqrt(3)*length*sin(30*pi/180)

        if (number_horizontal % 2 != 0):
            zeichne_wabe(pos_x, pos_y, length)

        pos_x=0
        start_y = start_y + sqrt(3)*length*sin(270*pi/180)
        pos_y = start_y
        
    done()

if __name__ == "__main__":
    main()
