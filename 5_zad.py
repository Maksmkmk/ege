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






