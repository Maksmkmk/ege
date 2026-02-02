#------------1-------------
"""
a = 200
for A in range(a):
    c = 0
    for x in range(a):
        for y in range(a):
            if ( (3 * y - x > 12) or (2 * x + 6 * y >= 72) or (x > 24) or (x * y < A) ) == 1:
                c += 1
    if c == a ** 2:
        print(A)
        break
"""
#---------2---------
"""
for a in range(1000):
    if all(((x | 42 > 64) and (x | 34 <= 102)) <= (x | a >= 70) for x in range(1000)):
        print(a)
        break

for a in range(1000):
    fl = True
    for x in range(1000):
        if not(  ((x | 42 > 64) and (x | 34 <= 102)) <= (x | a >= 70)  ):
            fl = False
            break
    if fl:
        print(a)
        break
"""
#-----------------3-----------------
"""
def Del(n, m):
    return n % m == 0


for A in range(1, 10_000):
    A_podoshel = True
    for x in range(1, 10_000):
        if ((not (Del(x, A))) <= ((not (Del(x, 18))) or (not(Del(x, 42))))) == 0:
            A_podoshel = False
            break
    if A_podoshel == True:
        print(A)
"""
#---------------4---------------
"""
# porazryadnayz kon'unkzia
# def f(n, m):
#     n = bin(n)[2:]
#     m = bin(m)[2:]
#     mxl = max(len(n), len(m))
#     n = n.zfill(mxl)
#     m = m.zfill(mxl)
#     r = ""
#     for i in range(mxl):
#         if n[i] == m[i]:
#             r += n[i]
#         else:
#             r += "0"
#     return r

for A in range(1, 1000):
    for x in range(1, 1000):
        if not ((x & 34 != 0) <= ((x & 41 == 0) <= (x & A != 0))):
            break
    else:
        print(A)
"""
#-----------------5-----------------
"""
# for A in range(1, 1000):
#     A_podoshel = True
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if not(((y + 5 * x != 31) or (A > x - 2)) and (A < y + 37)):
#                 A_podoshel = False
#                 break
#         if A_podoshel == False:
#             break
#     if A_podoshel:
#         print(A)
#         break

# for A in range(1, 1000):
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if not(((y + 5 * x != 31) or (A > x - 2)) and (A < y + 37)):
#                 break
#         if not (((y + 5 * x != 31) or (A > x - 2)) and (A < y + 37)):
#             break
#     else:
#         print(A)
#         break

for A in range(1, 1000):
    if all(((y + 5 * x != 31) or (A > x - 2)) and (A < y + 37) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)
        break
"""
#--------------6-------------
"""
R = list(range(12, 31 + 1))
Q = list(range(6, 15 + 1))
P = list(range(17, 23 + 1))
A = list()

for x in range(1, 100):
    if (((x in A) or (x in P)) or ((x in Q) <= (x in R))) == 0:
        A += [x]
print(A)

# 6 -> 6 # 6 есть в условии
# 11 -> 12 # 11 нет в условии
# 12 - 6 = 6 # макс - мин = длина
"""
#--------------7-------------
"""
Q = list(range(8, 17 + 1))
P = list(range(3, 11 + 1))
A = list(range(1, 100 + 1))

for x in range(1, 100 + 1):
    if (((x in A) <= (x in P) or (x in Q))) == 0:
        A.remove(x)
print(A)
# 3 -> 3 # 3 есть в условии
# 17 -> 17 # 17 нет в условии
# 17 - 3 = 14 # макс - мин = длина
"""
#----------------8----------------
"""
P = [x / 10 for x in range(320, 1250 + 1)]
O = [x / 10 for x in range(320, 1250 + 1)]
T = [x / 10 for x in range(320, 1250 + 1)]
A = list()

print(P)

for x in range(1, 1000):
    if ((x not in A) <= ((x in P) or (x not in O) or (x not in T))) == 0:
        A += [x]
print(A)
print(125 - 32)
"""
#--------------9--------------
"""
A = list(range(100, 200 + 1))
B = [11]


def dels(n):
    a = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return sorted(a)

for y in range(1000_000):
    C = dels(y)
    if len(C) == 0:
        continue
    if (all((x in C) <= ((x in A) and (x not in B)) for x in range(1000_000))):
        print(y)
        break
"""
#-----------16----------
"""
P = list(range(25, 64 + 1))
Q = list(range(40, 115 + 1))
A = list()

for x in range(10_000):
    if not( (x in P) <= (((x in Q) and (not(x in A))) <= (not(x in P))) ):
        A += [x]

print(A)
print(64 - 40)
"""
#---------------17---------------
"""
def dell(n, m):
    return n % m == 0

for A in range(1, 100_000):
    if all(((x % 128 == 0) <= ((x % A != 0) <= (x % 80 != 0))) for x in range(1, 10_0000)):
        print(A)
"""
#---------------18---------------
"""
for A in range(1000):
    if all( ((201 != y + 2 * x) or (A > x) or (A > y)) for x in range(1000) for y in range(1000)):
        print(A)
        break
"""
#-------------19-------------
"""
def f(x, A):
    return ((x % 2 == 0) <= (x % 5 != 0)) or (x + A >= 70)

for A in range(1, 1000):
    if all(f(x, A) for x in range(1, 1000)):
        print(A)
        break
"""
#-----------20-----------
"""
B = list(range(23, 37 + 1))
C = list(range(41, 73 + 1))
A = list()

def f(x, A, B, C):
    return not (((x not in B) <= (x in C)) <= (x in A))

for x in range(1000):
    if f(x, A, B, C):
        A.append(x)

print(A)
print(73 - 23)
"""
#----------------21----------------
"""
P = [x / 10 for x in range(30, 870 + 1)]
Q = [x / 10 for x in range(500, 720 + 1)]
A = [x / 10 for x in range(10_000)]

# инверсия кон диз импликация эквиваленция

def f(x, A, P, Q):
    return (x in P) and (not((x in A) == (x in Q))) or (not((x in Q) or (x in A)))


for x in range(10_000):
    x = x / 10
    if f(x, A, P, Q) == 0:
        A.remove(x)

print(A)
print(50 - 3)
"""
#--------------------22--------------------
"""
B = [x / 10 for x in range(100, 210 + 1)]
A = []

def f(x, B, A):
    return (x not in B) or (x in A)

for x in range(1000):
    x = x / 10
    if f(x, B, A) == 0:
        A += [x]

print(A)
print(21 - 10)
"""
#-----------------23---------------
"""
P = [2,4,6,8,10,12,14,16,18,20]
Q = [3,6,9,12,15,18,21,24,27,30]
R = [12,24,36,48,60]
A = []

def f(x, A, P, Q, R):
    return (x not in A) <= (((x in P) and (x in Q)) <= (x in R))

for x in range(1000):
    if f(x, A, P, Q, R) == 0:
        A += [x]

print(A)
print(6 * 18)
"""
#---------------24--------------
"""
A = []

for x in range(1000):
    if ((x in [14,31,40,1,12,94]) <= (x not in [40,12,10,1,13])) == 0:
        A += [x]

print(A)
"""
#-------------25--------------
"""
data = []

for i in range(256):
    data.append(bin(i)[2:].zfill(8))

P = [x for x in data if x.count("1") % 2 == 0]
Q = [x for x in data if x[:2] == "10"]
R = [x for x in data if x[-3:] == "101"]
B = []

def f(x, P, Q, R, B):
    return (x not in R) <= (((x in P) or (x not in B) and (x in Q)) <= ((x in B) or (x not in Q) and (x in P)))

for x in data:
    if f(x, P, Q, R, B) == 0:
        B += [x]

print(B)
print(len(B))
"""
#----------------26-----------------
"""
for A in range(1000):
    if all((  ((x & 49 != 0) <= ((x & A != 0) <= (x & 108 != 0))) <= ((x & 92 == 0) and (x & A != 0) and (x & 49 != 0))  ) == 0 for x in range(1000)):
        print(A)
"""
#-----------------27-------------------
"""
def f(x, A):
    return not((x | 41 == 0) or (x & 128 != 0)) and (x & A == 0) and ((x | A == 0) or (x & A == 0))

for A in range(1, 1000):
    if all(f(x, A) for x in range(10, 100)):
        print(A)
        break
"""
#-------------28-------------
"""
M = int("100100111", 2)
K = int("1100110010", 2)

print(bin(M & K)[2:].count("1"))
"""
#----------------29----------------
"""
def f(x, y, A):
    return (x >= 8) or (A < (x * y)) or (y <= 7)

for A in range(1000):
    if all(f(x, y, A) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)
"""
#---------------30-------------
"""
for A in range(1000):
    if all( (x > 78) or (A > x) for x in range(1000)):
        print(A)
        break
"""
#------------------31-----------------
"""
data = [x / 10 for x in range(1, 100)]

def f(x, y, A):
    return (- (x - 2) ** 2 + 3 < y) or ((x - 1) ** 2 + y ** 2 < 7) or (5 * x + A > y)


for A in range(-1000, 1000):
    if all(f(x, y, A) for x in data for y in data):
        print(A)
        break
"""
#----------------32----------------
"""
for A in range(1, 1000):
    if all( ((x % A != 0) and (x % 24 == 0)) <= ((x % 16 != 0) or (x % 24 != 0)) for x in range(1, 1000)):
        print(A)
"""
#--------------33-------------
"""
for x in range(2, 1000):
    if x % 30 == 0 or 15 % x == 0:
        print(x)
        break
"""
#------------------34-------------------
"""
def dl(x, A):
    return x % A == 0

def f(x, A):
    return ((dl(x, A) and dl(x, 45)) <= dl(x, 162)) and (A > 200)

for A in range(1, 1000):
    if all(f(x, A) for x in range(1, 100000)):
        print(A)
        break
"""
#-----------------35-----------------
"""
def dl(n, m):
    return n % m == 0

def f(x, A):
    return ((dl(x, 36) and dl(x, 42)) <= dl(x, A)) and (A * (A - 25) < 25 * (A + 200))

for A in range(1, 1000):
    if all(f(x, A) for x in range(1, 1000)):
        print(A)
"""
#-----------------36-----------------
"""
B = list(range(20, 47 + 1))

A = [a for a in range(-1000, 1000) if all((x & 45 != 0) <= ((x & 21 == 0) <= (x & a != 0)) for x in range(1, 1000))]

for x in range(1, 1000):
    if ((x in A) <= (x in B)) == 0:
        print(x)
        break
"""
#---------------37---------------
"""
B = list(range(142, 252 + 1))

for A in range(1, 10_000):
    if all(((x % 6 == 0) <= (x % 15 != 0)) or (x + A not in B) for x in range(1, 1000)):
        print(A)
        break
"""
#--------------------38----------------------






