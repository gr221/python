from math import *

print("Programm zur Lösung einer Gleichung der From a*x*x+b*x+c = 0.")
a = float(input("Gib den Paramter a ein: "))
b = float(input("Gib den Paramter b ein: "))
c = float(input("Gib den Paramter c ein: "))
determinant = b*b - 4*a*c

if determinant == 0:
    x = -b/(2*a)
    print("Die Lösung ist ", x)

elif determinant > 0:
    x = (-b + sqrt(determinant)) / (2*a)
    y = (-b - sqrt(determinant)) / (2*a)
    print("Die Lösungen sind: ", x, " und ", y)

else:
    root = sqrt(-determinant)/(2*a)
    x = -b/(2*a)
    print("Die Lösungen sind: ", x, "+i*", root, " und ", x, "-i*", root)


