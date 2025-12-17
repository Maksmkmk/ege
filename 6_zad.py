#-----------1-------------
"""
from turtle import*

tracer(0)

screensize(5000, 5000)

z = 25

for i in range(3):
    goto(pos()[0] + 15 * z, pos()[1] + 37 * z)
    goto(pos()[0] - 40 * z, pos()[1] - 35 * z)
    goto(pos()[0] - 22 * z, pos()[1] + 32 * z)
    goto(pos()[0] + 47 * z, pos()[1] - 34 * z)

pu()

for x in range(150):
    for y in range(150):
        pu()
        goto(x * z - 2000, y * z)
        pd()
        dot(3)
"""
#------------------2-----------
"""
from turtle import*

k = 50
speed(1000)
lt(90)

for i in range(3):
    fd(2 * k)
    rt(90)
    fd(3 * k)
    lt(90)
rt(180)
fd(6 * k)
rt(90)
fd(9 * k)

pu()

backward(3 * k)
rt(90)

pd()

for i in range(2):
    fd(1 * k)
    rt(90)
    fd(2 * k)
    lt(90)

rt(180)
fd(3 * k)
rt(90)
fd(4 * k)
rt(90)
fd(1 * k)

tracer(1)

for x in range(-10, 10):
    for y in range(-10, 10):
        pu()
        goto(x * k, y * k)
        dot(5)
        pd()

mainloop()
#12
"""
#----------------------------3-------------
"""
from turtle import*

k = 20
speed(1000)
lt(90)


for i in range(7):
    fd(9 * k)
    rt(90)
    fd(16 * k)
    rt(90)

pu()

fd(3 * k)
rt(90)
fd(4 * k)
lt(90)

pd()

for i in range(4):
    fd(7 * k)
    rt(90)
    fd(13 * k)
    rt(90)

tracer(1)
speed(0)
for x in range(-3, 20):
    for y in range(-3, 10):
        pu()
        goto(x * k, y * k)
        dot(5)
        pd()

mainloop()
"""
#---------4------------
from turtle import*

speed(10000)
lt(90)
k = 50

for i in range(7):
    fd(5 * k)
    lt(72)
pu()

for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x * k, y * k)
        pd()
        dot(5)
        pu()

mainloop()


















