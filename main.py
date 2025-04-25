import math
from turtle import *
def hearta(k):
    return 16*math.sin(k)**3
def heartb(k):
    return 12*math.cos(k)-3*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
    math.cos(4*k)
speed(10000)
bgcolor("black")
for i in range(6000):
    goto(hearta(i)*25,heartb(i)*25)
    for j in range(5):
        color("red")
    goto(0,0)
done()    
