
from turtle import *

a = 1
b = 0
c = 0

def f(x):
    return a * x ** 2 + b * x + c

z = 20
tracer(0)

lst = [x / 100 for x in range(-3000, 3000)]

data = [(x / 1, f(x) / 1) for x in lst]

pu()
for i in data:
    goto(i[0] * z, i[1] * z)
    dot(7, "red")





pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * z, y * z)
        if x == 0 or y == 0:
            dot(6, "black")
        else:
            dot(4, "gray")






mainloop()


