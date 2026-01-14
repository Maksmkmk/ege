#------------1------------
"""
from turtle import *

data = [list(map(float, x.replace(",", ".").split())) for x in open("27_B.txt")]

tracer(0)

z = 30

pu()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * z, y * z)
        if x == 0 or y == 0:
            dot(6, "black")
        else:
            dot(3, "gray")

pu()

c1 = []
c2 = []
c3 = []

for i in data:
    goto(i[0] * z, i[1] * z)
    if i[1] < 12:
        dot(8, "green")
        c1.append(i)
    elif i[0] < 17:
        dot(8, "blue")
        c2.append(i)
    else:
        dot(8, "red")
        c3.append(i)

answ = []
for i in c3:
    r = 0
    for j in c3:
        r += ((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2) ** 0.5
    answ.append([r, i])

print(max(answ))

# c1 [0.1663069, 16.1520663]
# c2 [3.4435388, 6.1127361]
print((0.1663069 + 3.4435388) / 2 * 10000)
print((16.1520663 + 6.1127361) / 2 * 10000)

# for i in a:
#     goto(i[0] * z, i[1] * z)
#     dot(10, "purple")

print((18.1424701 + 14.747434 + 19.4524463) / 3 * 10000)
print((6.1934274 + 21.5194643 + 14.961161) / 3 * 10000)

screensize(2000, 2000)
mainloop()
"""
#--------------------2--------------------

from turtle import *
from math import *

data = [list(map(float, x.replace(",", ".").split())) for x in open("27_B.txt")]

pu()
z = 20
tracer(0)
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * z, y * z)
        if x == 0 or y == 0:
            dot(4, "black")
        else:
            dot(3, "gray")

c1, c2, c3 = [], [], []
for i in data:
    if i[1] < 5:
        goto(i[0] * z, i[1] * z)
        dot(4, "red")
        c1 += [i]
    elif i[1] > 12:
        goto(i[0] * z, i[1] * z)
        dot(4, "green")
        c2 += [i]
    else:
        goto(i[0] * z, i[1] * z)
        dot(4, "blue")
        c3 += [i]

# def center(c):
#     yy = []
#     xx = []
#     for i in c:
#         xx += [i[0]]
#         yy += [i[1]]
#
#     return [min(xx) + (max(xx) - min(xx)) / 2, min(yy) + (max(yy) - min(yy)) / 2]
# centers
# c1 [6.795413845000001, 12.83044891]
# c2 [4.348127079999999, 6.0716400875000005]

answ = []
for i in c2:
    r = 0
    for j in c2:
        r += ((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2) ** 0.5
    answ += [[r, i]]

print(min(answ))
# A
# c1 [84.13898162520212, [6.66792676, 12.74236299]]
# c2 [68.8015003940668, [4.29949916, 6.22951182]]
# print(abs(6.66792676 - 4.29949916) * 10_000)
# print(abs(12.74236299 - 6.22951182) * 10_000)

# B
# c1 red
# c2 [18.21600372, 14.36225718] green
# c3 [12.21724979, 10.31689525] blue

# min green blue
# max green red

print(dist([18.21600372, 14.36225718], [12.21724979, 10.31689525]) * 10_000)
print(dist([18.21600372, 14.36225718], [19.52793365, 1.3306858]) * 10_000)















screensize(5000, 5000)
mainloop()


































