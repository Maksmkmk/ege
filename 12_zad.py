#------------old_12-------------
#-----------1--------------
"""
s = 111 * "3"
while "33333" in s or "1111" in s:
    if "33333" in s: s = s.replace("33333", "111", 1)
    else: s = s.replace("111", "33", 1)
lst = [int(i) for i in s]
print(sum(lst))
"""
#------------2----------------
"""
s = 81 * "1"
while "11111" in s or "888" in s:
    if "11111" in s: s = s.replace("11111", "88", 1)
    else: s = s.replace("888", "8", 1)
print(s)
"""
#---------------3-----------------
"""
for n in range(4, 10000):
    s = "7" + "8" * n
    while "78" in s or "688" in s or "8888" in s:
        if "78" in s: s = s.replace("78", "8", 1)
        if "688" in s: s = s.replace("688", "87", 1)
        if "8888" in s: s = s.replace("8888", "6", 1)
    lst = [int(i) for i in s]
    if sum(lst) == 61:
        print(n)
        break
"""
#---------new_12-------------
#-----------1-------------

a = set()
for n in range(4, 10_000):
    s = "7" + "6" * n
    while "766" in s or "667" in s:
        if "766" in s:
            s = s.replace("766", "67", 1)
        if "667" in s:
            s = s.replace("667", "7", 1)
    a.add(s)
print(len(a))









