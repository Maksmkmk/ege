#--------------1---------
'''
def ss(n, sys):
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    res = ""
    while n > 0:
        res += digits[n % sys]
        n = n // sys
    return res[::-1]

for x in range(400, 600):
    res = 16**560 + 16**120 - x
    if ss(res, 16).count("0") == 442:
        print(x)
        break
'''
#------------2-----------
'''
def ss9(n):
    res = ""
    while n > 0:
        res += str(n % 9)
        n = n // 9
    return res[::-1]

for x in range(1, 500):
    zn = 9**1942 + 9 * 6**971 + 214 - x
    zn = ss9(zn)
    if zn.count("2") - zn.count("8") == 471 or\
       zn.count("8") - zn.count("2") == 471:
        print(x)
        break
'''
#---------------3------------
'''
def ss49(n):
    digits = "0123456789abcdefghijklmnopqrstuvwxyzабвгдежзийклмнопрст"
    res = ""
    while n > 0:
        res += digits[n % 49]
        n = n // 49
    return(res[::-1])
# print(18 * 7**108 - 5 * 49**76 + 343**35 - 50)
s = 1425187768786964075530968380830964335069681210825637506307484333897600081633441901451175986908243966373099287451243953076669572830
res = "4мммммммммммммммммммммuмж0000000000000000000000000000000000000000000000000011"
print(res.count("4") + res.count("м") + res.count("u") + \
      res.count("ж") + res.count("0") + res.count("1"))
# 1   22   1   1   50   2
# 4   м    u   ж   0    1

# 4   48   30  42  0    1
c = 0
for i in "0123456789abcdefghijklmnopqrstuvwxyzабвгдежзийклмнопрст":
    
    print(c, i)
    c += 1
'''
#---------------4--------------
'''
a = "36053"
b = "403"


lst1 = [i for i in range(110) if "8" not in str(i) and "9" not in str(i)]
lst2 = []
for i in lst1:
    b = b[0] + str(i) + b[-1]
    lst2.append(b)

lst = []

for j in lst2:
    lst.append(int(a, 8) - int(j, 8))
    print(a, j, int(a, 8), int(j, 8), int(a, 8) - int(j, 8))
print(min(lst))
'''
#-------------5--------------
'''
def ss6(n):
    res = ""
    while n > 0:
        res += str(n % 6)
        n = n // 6
    return res[::-1]
for x in range(1, 2031):
    zn = 6**260 + 6**160 + 6**60 - x
    if ss6(zn).count("0") == 202:
        print(x)
        break
'''


























