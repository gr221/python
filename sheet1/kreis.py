from turtle import *

#ht()
distance = 100
dotsize = 15
segment_breite = 30
begin_fill()
circle(dotsize, steps=100)
end_fill()
penup()
right(90)
forward(distance)
pendown()
left(90)

for i in range(0,3):
    begin_fill()
    circle(dotsize+distance, 60, steps=100)
    left(90)
    forward(segment_breite)
    right(90)
    circle(dotsize+distance-segment_breite, -60, steps = 100)
    right(90)
    forward(segment_breite)
    end_fill()
    penup()
    left(90)
    circle(dotsize+distance, 120, steps=100)
    pendown()
done()
