from turtle import *

def calc_schwer(points):
    x_schwer=float(points[0][0])
    y_schwer=float(points[0][1])
    for i in range(1,len(points)):
        x_schwer = (x_schwer+float(points[i][0]))/2
        y_schwer = (y_schwer+float(points[i][1]))/2

    schwerpunkt = x_schwer, y_schwer
    return schwerpunkt

def print_points(points, schwerpunkt):
    for i in range(0, len(points)):
        pu()
        setpos(float(points[i][0]),float( points[i][1]))
        pd()
        dot(5)

    pu()
    setpos(float(schwerpunkt[0]), float(schwerpunkt[1]))
    dot(5,"red")
    

def main():
    # while (True):
    points=[]
    for i in range(0,3):
        x = input("Gib eine x-Koordinate ein: ")
        y = input("Gib eine y-Koordinate ein: ")
        coordinate = x,y
        points.append(coordinate) 
        print(points)
        weiter=input("Möchtest du einen weiteren Punkt hinzufügen?(y/n)") 
        if weiter != 'y':
            break

    print(points)
    schwerpunkt = (calc_schwer(points))
    print(schwerpunkt)
    print_points(points, schwerpunkt)
    done()

if __name__=="__main__":
    main()
