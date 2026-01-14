#--------------1--------------
"""
f = open("9.txt")
data = [list(map(int, s.split())) for s in f]

c = 0
for i in data:
    c += 1
    if len(i) == len(set(i)):
        i = sorted(i)
        if (i[0] + i[-1]) * 2 == (i[1] + i[2] + i[3]) * 3:
            last = c
print(last)
"""
import shlex

#-------------2-----------------
"""
f = open("9.txt")

data = [list(map(int, s.split())) for s in f]

c = 0
for i in data:
    cntr = [i.count(x) for x in i]
    if cntr.count(3) == 3 and cntr.count(2) == 2 and cntr.count(1) == 2:
        pov = [x for x in i if i.count(x) > 1]
        nepov = [x for x in i if i.count(x) == 1]
        if max(pov) > max(nepov):
            c += 1
            print(c, i)
"""
#-----------3----------------
"""
f = open("9.txt")

data = [list(map(int, s.split())) for s in f]

c = 0
for i in data:
    cntr = [i.count(x) for x in i]
    if cntr.count(1) == 5:
        i = sorted(i)
        if i[-1] + i[-2] <= i[0] + i[1] + i[2]:
            c += 1
            print(c, i)
"""
#---------------4-------------
"""
def krat_3(a):
    for i in a:
        if i % 3 == 0:
            return True
    return False

f = open("9.txt")

data = [list(map(int, s.split())) for s in f]

c = 0
for i in data:
    if krat_3(i):
        i = sorted(i)
        if (i[0] + i[1]) > i[-2]:
            c += 1
print(c)
"""
#----------5-----------
'''
f = open("9.txt")

data = [list(map(int, s.split())) for s in f]

c = 0
for i in data:
    c += 1
    cntr = [i.count(x) for x in i]
    if cntr.count(2) == 2 and cntr.count(1) == 4:
        if i.count(min(i)) == 1:
            last = c
print(last)
'''
#-------------6------------
"""
f = open("9.txt")

data = [list(map(int, s.split())) for s in f]

c = 0
for i in data:
    c += 1
    cntr = [i.count(x) for x in i]
    if cntr.count(2) == 4 and cntr.count(1) == 3:
        nepov = [x for x in i if i.count(x) == 1]
        pov = [x for x in i if i.count(x) > 1]
        sr_pov = sum(pov) / len(pov)
        if sr_pov < max(nepov):
            print(c)
            break
"""
#----------7--------------
"""
f = open("9.txt")

data = [list(map(int, s.split())) for s in f]

c = 0
for i in data:
    cntr = [i.count(x) for x in i]
    if cntr.count(1) == 6:
        if 5 * (min(i) + max(i)) >= 3 * (sum(i) - max(i) - min(i)):
            c += 1
            print(c, i)
"""
#-------------8--------------
"""
f = open("9.txt")

data = [list(map(int, s.split())) for s in f]

c = 0
for i in data:
    if (sum(i) - min(i) - max(i)) / 3 >= 8:
        c += 1
        print(i, c)
print(c)
"""
#-------------9--------------
"""
f = open("9.txt")

data = [list(map(int, s.split())) for s in f]

c = 0
for i in data:
    if max(i) < sum(i) - max(i):
        if i[0] + i[1] == i[2] + i[3] or i[0] + i[2] == i[1] + i[3] or i[0] + i[3] == i[2] + i[1]:
            c += 1
print(c)
"""
#-------------10------------
"""
f = open("9.txt")

data = [list(map(int, s.split())) for s in f]
last = 0
c = 0
for i in data:
    c += 1
    cntr = [i.count(x) for x in i]
    if cntr.count(3) == 3 and cntr.count(1) == 4:
        pov = [x for x in i if i.count(x) > 1]
        nepov = [x for x in i if i.count(x) == 1]
        if sum(nepov) / len(nepov) <= pov[0]:
            last = sum(i)
print(last)
"""
#--------------11-------------
"""
f = open("9.txt")

data = [list(map(int, s.split())) for s in f]

c = 0
for i in data:
    cntr = [i.count(x) for x in i]
    if cntr.count(2) == 2 and cntr.count(1) == 3:
        i = sorted(i)
        if (i[0] + i[-1]) ** 2 < i[1] ** 2 + i[2] ** 2 + i[3] ** 2:
            c += 1
print(c)
"""
#----------------12----------------
"""
f = open("9.txt")
data = [list(map(int, x.split())) for x in f]

c = 0
answ = []
for i in data:
    c += 1
    cntr = [i.count(x) for x in i]
    nepov = [x for x in i if i.count(x) == 1]
    pov = [x for x in i if i.count(x) > 1]
    if cntr.count(3) == 3 and cntr.count(1) == 4 and sum(nepov) > sum(pov):
        answ += [[c, i]]
print(max(answ))
"""
#----------------13----------------
"""
f = open("9.txt")

data = [list(map(int, s.split())) for s in f]

c = 0
answ = []
for i in data:
    c += 1
    cntr = [i.count(x) for x in i]
    pov = [x for x in i if i.count(x) > 1]
    nepov = [x for x in i if i.count(x) == 1]
    if cntr.count(3) == 3 and cntr.count(1) == 4:
        if sum(nepov) / len(nepov) <= pov[0]:
            answ += [[c, sum(i)]]
print(max(answ))
"""
#-----------------14----------------
"""
f = open("9.txt")

data = [list(map(int, x.split())) for x in f]

a = []

for i in data:
    cntr = [i.count(x) for x in i]
    if cntr.count(2) == 2 and cntr.count(1) == 4:
        pov = [x for x in i if i.count(x) > 1]
        nepov = [x for x in i if i.count(x) == 1]
        if pov[0] > sum(nepov):
            a += i
print(sum(a) / len(a))
"""
#----------15----------

data = [list(map(int, x.split())) for x in open("9.txt")]

c = 0
for i in data:
    if i[0] % 2 == 0 and i[1] % 2 == 0 and i[2] % 2 == 0 and i[3] % 2 == 0:
        i = sorted(i)
        if i[0] ** 2 <= i[1] + i[2] + i[3]:
            c += 1

print(c)





























