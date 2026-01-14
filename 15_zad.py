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

for A in range(1000):
    if all( ((201 != y + 2 * x) or (A > x) or (A > y)) for x in range(1000) for y in range(1000)):
        print(A)
        break



















































