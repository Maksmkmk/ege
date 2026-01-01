#----------1--------
"""
from itertools import *

c = 0
for i in product("01234", repeat=6):
    i = "".join(i)
    if i[-1] not in "34" and i[0] not in "01":
        c += 1
print("""
#----------2--------
"""
from itertools import *

c = 0
for i in product("КАЛИЙ", repeat=6):
    i = "".join(i)
    if i.count("Й") <= 1 and\
       i[0] != "Й" and i[-1] != "Й" and\
       "ИЙ" not in i and "ЙИ" not in i:
        c += 1
print(c)
"""
#----------3--------
"""
from itertools import *

#B 0
#E 1
#K 2
#H 3
#O 4

#OHHKK

c = 0
a = []
for i in product("BEKHO", repeat=5):
    c += 1
    i = "".join(i)
    if i.count("H") == 2 and i.count("K") == 2:
        a = [c, i]
print(a)
"""
#----------4--------
"""
from itertools import *

#АВДПР
#01234

#ВДПР
#1234

c = 0
for i in product("АВДПР", repeat=4):
    i = "".join(i)
    c += 1
    if len(set(i)) == len(i) and i.count("А") == 0:
        print(c, i)
        break
"""
#-------------5------------
"""
from itertools import *
# А В Н Р Ь Я
# 0 1 2 3 4 5
# 5 букв
# 4 5 3 5 3
# Ь Я Р Я Р
a = []
c = 0
for i in product(sorted("ЯНВАРЬ"), repeat=5):
    i = "".join(i)
    c += 1
    if i[0] != "Я" and i.count("Ь") <= 1 and "ЯЯ" not in i:
        a.append([c, i])
print(a[-1])
"""
#--------------6------------
"""
from itertools import *

c = 0
for i in product("КОТБУС", repeat=8):
    i = "".join(i)
    if i[0] not in "ОУ" and "КОТ" in i:
        c += 1
print(c)
"""
#-------------7-----------
"""
from itertools import *

c = 0
for i in product("0123456789abcde", repeat=5):
    i = "".join(i)
    
    if i[0] % 2 == 0 and\
        i[1] % 3 == 0 and\
        i[2] % 2 == 0 and\
        i[3] % 3 == 0 and\
        i[4] % 2 == 0:
        c += 1
    elif:

    
    #12345
    #%2%3%2%3%2
    #%3%2%3%2%3
"""
#---------------8-----------
"""
from itertools import *

c = 0
for i in product("ДИКМО", repeat=5):
    i = "".join(i)
    c += 1
    if i.count("М") == 2 and "ММ" not in i:
        print(c, i)
"""
#----------------9-------------
"""
from itertools import *

c = 0
for i in product("ЖКМФЦЧ", repeat=6):
    i = "".join(i)
    if i.count("Ч") >= 2:
        c += 1
print(c)
"""
#---------------------------10------------
"""
from itertools import *

c = 0
for i in permutations("АРТЕМ"):
    if i[0] not in "АЕ" or i[-1] not in "АЕ":
        c += 1
print(c)
"""
#------------------11--------------------
"""
from itertools import *

c = 0
for i in product("АКОРСТ", repeat=5):
    c += 1
    i = "".join(i)
    if c % 2 == 0 and i[0] not in "АСТ" and i.count("О") == 2:
        print(c, i)
"""
#-------------------12---------------
"""
from itertools import *
c = 0

for i in product("КОМПЕГЭ", repeat=6):
    i = "".join(i)
    if i[0] in "ОЕЭ" and i[5] in "ОЕЭ" and\
        i[1] in "КМПГ" and \
        i[2] in "КМПГ" and \
        i[3] in "КМПГ" and \
        i[4] in "КМПГ":
        c += 1
print(c)
"""
#--------------------------13---------------
"""
from itertools import *

c = 0
c2 = 0
for i in product(sorted("ВЕЧНОСТЬ"), repeat=6):
    c += 1
    i = "".join(i)
    if c % 2 == 0 and i.count("О") >= 2 and i[0] not in "ВНСТЧ":
        c2 += 1
print(c2)
"""
#--------------14--------------
"""
from itertools import *

c = 0
for i in product("012345", repeat=7):
    i = "".join(i)
    if i[0] != "0" and i.count("2") == 1 and\
        "02" not in i and\
        "42" not in i and\
        "20" not in i and\
        "24" not in i:
        c += 1
print(c)
"""
#--------------------15--------------
"""
from itertools import *

c = 0
for i in product("БЕЛКА", repeat=4):
    i = "".join(i)
    if i.count("Б") == 1:
        c += 1
print(c)
"""
#----------------16----------------
"""
from itertools import *
c = 0
a = set()
for i in permutations("01234567"):
    i = "".join(i)
    if i[-5] != "0":
        a.add(i[-5:])
lst = sorted(a)

def isit(s):

    def is_ev(s):
        if int(s) % 2 == 0:
            return True
        else:
            return False

    if (is_ev(s[0]) and not(is_ev(s[2])) and is_ev(s[4])) and ((is_ev(s[1]) and not(is_ev(s[3]))) or (not(is_ev(s[1])) and is_ev(s[3]))):
        return True
    elif (not(is_ev(s[0])) and is_ev(s[2]) and not(is_ev(s[4]))) and ((is_ev(s[1]) and not(is_ev(s[3]))) or (not(is_ev(s[1])) and is_ev(s[3]))):
        return True
    else:
        return False

c = 0
for i in lst:
    if isit(i):
        c += 1
        print(c, i)
"""
#--------------17-----------------
"""
from itertools import *

a = set()
for i in permutations("01234567"):
    i = "".join(i)
    i = i[:-2]
    if "3" not in i and i[0] != "0":
        if "00" in i or "02" in i or "04" in i or "06" in i\
                or "20" in i or "22" in i or "24" in i or "26" in i \
                or "40" in i or "42" in i or "44" in i or "46" in i \
                or "60" in i or "62" in i or "64" in i or "66" in i \
                or "80" in i or "82" in i or "84" in i or "86" in i:
            a.add(i)

print(len(a))
"""
#---------------18--------------------
"""
from itertools import *

c = 0
for i in product("ДГШЯБЖ", repeat=6):
    i = "".join(i)
    if i.count("Я") == 1:
        c += 1

print(c)
"""
#----------------------19-------------
"""
from itertools import *

a = set()
for i in permutations("СОТОЧКА"):
    i = "".join(i)
    if "ОО" in i or "АО" in i or "ОА" in i:
        a.add(i)

print(len(a))
"""
#------------------------20---------------------
"""
from itertools import *

c = 0
for i in product("01234567", repeat=5):
    i = "".join(i)
    if i.count("6") == 1 and i[0] != "0":
        if "16" not in i and "36" not in i and "56" not in i and "76" not in i\
                and "61" not in i and "63" not in i and "65" not in i and "67" not in i:
            c += 1

print(c)
"""
#----------------21----------------
"""
from itertools import *

c = 0
for i in product("АГИЛМОРТ", repeat=5):
    c += 1
    i = "".join(i)
    if c % 2 == 0 and i[0] != "А" and i[0] != "Г" and i.count("Р") >= 2:
        print(c, i)
        break
"""
#----------------22------------------
"""
from itertools import *

c = 0
for i in product("КОСУФ", repeat=5):
    c += 1
    i = "".join(i)
    if "Ф" not in i and i.count("У") == 2:
        last = c
print(last)
"""
#---------------23---------------
"""
from itertools import *

c = 0
for i in permutations("КАБИНЕТ"):
    i = "".join(i)
    if i[-1] not in "АИЕ":
        c += 1
        print(c, i)
print(c)
"""
#--------------24---------------
"""
from itertools import *
a = set()
for i in product("ГИРЛЯНДА", repeat=9):
    i = "".join(i)
    if i.count("А") == 1 and "АГ" not in i and "АР" not in i and "АЛ" not in i and "АН" not in i and "АД" not in i and "ГА" not in i and "РА" not in i and "ЛА" not in i and "НА" not in i and "ДА" not in i:
        a.add(i)
print(a)
print(len(a))
"""
#---------------25--------------
"""
from itertools import *
a = set()
for i in product("СНЕГУРОЧКА", repeat=9):
    i = "".join(i)
    if i.count("С") + i.count("Н") + i.count("Г") + i.count("Р") + i.count("Ч") + i.count("К") == 3:
        a.add(i)
print(a, len(a))
"""
#---------26-----------
"""
from itertools import *
c = 0
for i in product("0123456789ABCDEF", repeat=8):
    i = "".join(i)
    if i.count("0") == 2:
        if i[0] != "0":
            if i[-1] in "02468ACE":
                c += 1
print(c)
"""
#-------------27----------------
"""
from itertools import *

c = 0
for i in permutations("АРТЕМ"):
    i = "".join(i)
    # if not (i[0] in "АЕ" and i[-1] in "АЕ"):
    if i[0] == "А" and i[-1] != "Е" or i[0] == "Е" and i[-1] != "А" or i[0] not in "АЕ":
        c += 1
        print(c, i)
"""
#-------------28--------------































