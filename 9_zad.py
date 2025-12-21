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

f = open("9.txt")

data = [list(map(int, s.split())) for s in f]

c = 0
for i in data:
    cntr = [i.count(x) for x in i]
    if cntr.count(1) == 6:
        if 5 * (min(i) + max(i)) >= 3 * (sum(i) - max(i) - min(i)):
            c += 1
            print(c, i)


























