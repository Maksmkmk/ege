from itertools import *
a = set()
for i in product("СНЕГУРОЧКА", repeat=1):
    i = "".join(i)
    if i.count("С") + i.count("Н") + i.count("Г") + i.count("Р") + i.count("Ч") + i.count("К") == 3:
        a.add(i)
print(a)
print(len(a))



