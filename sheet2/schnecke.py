from turtle import *
from math import *

for i in range(1,51):
    setx(0)
    sety(0)
    a = sqrt(1000*i)
    g = sqrt(1000)
    h = sqrt(1000*(i+1))
    # print(g)
    # print(h)
    # print(g/h)
    winkel = 90- asin(g/h) *180 /pi
    fd(a)
    rt(270)
    fd(g)
    lt(180 - winkel)
    fd(h)
    lt(180)

done()
