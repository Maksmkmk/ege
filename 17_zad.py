#------------1------------
"""
f = open("17.txt")

data = [int(x) for x in f]

answs = []

for i in range(len(data) - 1):
    el1 = data[i]
    el2 = data[i + 1]
    if abs(el1 + el2) % 11 == 0:
        answs.append(el1 + el2)

print(len(answs), max(answs))
"""
#---------------------2----------------------
"""
f = open("17.txt")

data = [int(x) for x in f]

answs = []

for i in range(len(data) -1):
    e1 = data[i]
    e2 = data[i + 1]
    if (abs(e1) + abs(e2)) > 17043 and (abs(e1) + abs(e2)) % 3 == 0:
        answs += [e1 + e2]

print(len(answs), min(answs))
"""
#------------------3-------------------------
"""
f = open("17.txt")

data = [int(x) for x in f]
max_kr22 = max([x for x in data if x % 22 == 0])
answs = []

for i in range(len(data) - 1):
    el1 = data[i]; el2 = data[i + 1]
    if el1 > max_kr22 or el2 > max_kr22:
        answs += [el1 + el2]

print(len(answs), min(answs))
"""
#--------------------4------------------------
"""
f = open("17.txt")

data = [int(x) for x in f]
max_kr11 = max([x for x in data if x % 11 == 0])
answs = []

for i in range(len(data) - 1):
    el1 = data[i]
    el2 = data[i + 1]
    if (el1 % 11 == 0 or el2 % 11 == 0) and (el1 + el2) <= max_kr11:
        answs.append(el1 + el2)

print(len(answs), max(answs))
"""
#-------------------------5--------------------------
"""
f = open("17.txt")

data = [int(x) for x in f]
answs = []

for i in range(len(data) - 1):
    el1 = data[i]; el2 = data[i + 1]
    if (el1 + el2) >= 100 and (el1 < 0 or el2 < 0):
        answs.append(el1 * el2)
print(len(answs), max(answs))
"""
#------------------6--------------------
"""
f = open("17.txt")

data = [int(x) for x in f]
max_kr11 = max([x for x in data if x % 11 == 0])
answs = []

for i in range(len(data) - 1):
    el1 = data[i]; el2 = data[i + 1]
    if el1 > max_kr11 or el2 > max_kr11:
        answs += [el1 + el2]
print(len(answs), min(answs))
"""
#--------------7----------------
"""
f = open("17.txt")

data = [int(x) for x in f]
min_kr25 = min(x for x in data if x % 25 == 0)
answs = []

for i in range(len(data) - 1):
    el1 = data[i]; el2 = data[i + 1]
    if (el1 % 2 == 0 or el2 % 2 == 0) and ((el1 + el2) % min_kr25 == 0):
        answs.append(el1 + el2)

print(len(answs), max(answs))
"""
#--------------8----------------
"""
f = open("17.txt")

def s(n):
    n = abs(n)
    a = [int(x) for x in str(n)]
    return sum(a)

data = [int(x) for x in f]
cub_max_3znach = max([x for x in data if len(str(x)) == 3]) ** 3
answs = []

for i in range(len(data) - 1):
    e1 = data[i]; e2 = data[i + 1]
    usl1 = s(e1) % 5 == 0 and s(e2) % 5 != 0
    usl2 = s(e2) % 5 == 0 and s(e1) % 5 != 0
    if (usl1) or (usl2):
        if abs(e1**2 - e2**2) >= cub_max_3znach:
            answs.append(e1 + e2)
print(len(answs), max(answs))
"""



















