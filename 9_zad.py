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

def krat_3(a):
    for i in a:
        if i % 3 == 0:
            return True
    return False

f = open("9.txt")

data = [list(map(int, s.split())) for s in f]

c = 0



