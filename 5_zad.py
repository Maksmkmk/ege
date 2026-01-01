#--------------1---------------
"""
for n in range(100, 100000):
    lst = []
    for i in range(len(str(n)) - 2):
        lst.append(int(str(n)[i:i + 3]))
    res = max(lst) - min(lst)
    if res == 415:
        print(n)
        break
"""
#-------------2----------------
"""
def f7(n):
    res = ""
    while n > 0:
        res += str(n % 7)
        n = n // 7
    return res[::-1]

for n in range(1000000, 1, -1):
    r = f7(n)
    if r.count("2") % 2 == 0:
        r += "555"
    else:
        r = "1" + r
    r = int(r, 7)
    # print(n, r)
    if r < 3799:
        print(n)
        break
"""
#------------3--------------
"""
def f3(n):
    res = ""
    while n:
        res += str(n % 3)
        n //= 3
    return res[::-1]

for n in range(2, 10000):
    r = f3(n)
    if r[0] == r[-1]:
        r += r[0]
    else:
        r += str(max(int(r[0]), int(r[-1])))
    r = int(r, 3)
    if r > 49:
        print(n)
        break
"""
#-------------4---------------
"""
for n in range(1000):
    r = bin(n)[2:]
    if int(r) % 2 == 0:
        r = r + "0" * r.count("0")
    else:
        r = "1" * r.count("1") + r
    if int(r, 2) > 2000:
        print(n, int(r, 2))
        break
"""
#------------5------------
"""
def r(n):
    r = bin(n)[2:]
    if n % 2 == 0: r += r[-2:]
    else: r = "1" + r + "0"
    return int(r, 2)

for n in  range(1000, 0, -1):
    if r(n) < 100:
        print(n)
        break
"""
#------------6-------------
"""
def r(n):
    r = bin(n)[2:]
    if n % 3 == 0: r = r.replace("0", "11")
    else: r = r.replace("1", "10")
    return int(r, 2)

answs = []
for n in range(1000, 0, -1):
    if r(n) <= 161:
        answs += [r(n)]
print(max(answs))
"""
#------------7------------
"""
def f4(n):
    r = ""
    while n:
        r += str(n % 4)
        n //= 4
    return r[::-1]

def ser0(s):
    return s[:len(s)//2] + "0" + s[len(s)//2:]

def r(n):
    r = f4(n)
    if len(r) % 2 == 0: r = ser0(r)
    return int(r)

for n in range(1000, 0, -1):
    if r(n) <= 180:
        print(n)
        break
"""

