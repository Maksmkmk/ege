#------------1_glava--------------
#---------------1-----------------
"""
# + 3 or + or 10 or * 2 win >= 61
def f(s, m):
    if s >= 61: return m % 2 == 0
    if m == 0: return False
    h = [f(s + 3, m - 1), f(s + 10, m - 1), f(s * 2, m - 1)]
    return any(h) if m % 2 != 0 else all(h)
    # return any(h) if m % 2 != 0 else any(h) # Для 20 (неудачный Пети)

# print("19)", [s for s in range(1, 51) if f(s, 1)]) # Петя выйграет первым ходом
# print("20)", [s for s in range(1, 51) if f(s, 2)]) # Ваня выйграет первым ходом после неудачного Пети
# print("21)", [s for s in range(1, 51) if not(f(s, 1)) and f(s, 3)]) # Пети не выйграет первым ходом и выйграет вторым
# 31
# 16
# 14 27
"""
#-------------------------2--------------------------
"""
# + 3 or * 3 win >= 50
def f(a, b, m):
    if a + b >= 50: return m % 2 == 0
    if m == 0: return False
    h = [f(a + 3, b, m - 1), f(a, b + 3, m - 1), f(a * 3, b, m - 1), f(a, b * 3, m - 1)]
    return any(h) if m % 2 != 0 else all(h)
    # return any(h) if m % 2 != 0 else any(h) # Для 20 (неудачный Петя)

# print("19)", [s for s in range(2, 46) if f(4, s, 1)]) # Петя выигрывает первым ходом
# print("20)", [s for s in range(2, 46) if f(4, s, 1)]) # Ваня выигрывает после неудачного Пети
# print("21)", [s for s in range(2, 46) if not(f(4, s, 1)) and f(4, s, 3)]) # Петя выигрывает 1-ым или 2-ым своим ходом
# 16
# 6
# 5
"""
#------------------3-------------------
"""
# + 2 or + 4 or * 3 win >=82
def f(s, m):
    if s >= 82: return m % 2 == 0
    if m == 0: return False
    h = [f(s + 2, m - 1), f(s + 4, m - 1), f(s * 3, m - 1)]
    return any(h) if m % 2 != 0 else all(h)
    # return any(h) if m % 2 != 0 else any(h) # Для 19 (неудачный Петя)

# print("19)", [s for s in range(1, 82) if f(s, 2)]) # Ваня выигрывает первым ходом после неудачного Пети
# print("20)", [s for s in range(1, 82) if not(f(s, 1)) and f(s, 3)]) # Петя выигрывает вторым ходом, но не первым
# print("21)", [s for s in range(1, 82) if (f(s, 2) or f (s, 4)) and (not(f(s, 2)))]) # Ваня выигрывает 1-ым или 2-ым, но не 1-ым
# 10
# 9 22
# 21
"""
#---------------4---------------
"""
# + 2 or * 2 win >= 123
def f(a, b, m):
    if a * b >= 123: return m % 2 == 0
    if m == 0: return False
    h = [f(a + 2, b, m - 1), f(a, b + 2, m - 1), f(a * 2, b, m - 1), f(a, b * 2, m - 1)]
    return any(h) if m % 2 != 0 else all(h)
    # return any(h) if m % 2 != 0 else any(h) # Для 19 (неудачный Петя)

# print("19)", [s for s in range(1, 41) if f(3, s, 2)]) # Ваня выигрывает после неудачного Пети
# print("20)", [s for s in range(1, 41) if f(3, s, 3) and not(f(3, s, 1))]) # Ваня выигрывает после неудачного Пети
# print("21)", [s for s in range(1, 41) if (f(3, s, 2) or f(3, s, 4)) and (not(f(3, s, 2)))]) # Ваня выигрывает после неудачного Пети
# 38
# 17 18
# 16
"""
#---------------2_glava---------------
#------------------5------------------
"""
# + 7 or * 4 win >= 342
def f(s, m):
    if s >= 342: return m % 2 == 0
    if m == 0: return False
    h = [f(s + 7, m - 1), f(s * 3, m - 1)]
    return any(h) if m % 2 != 0 else all(h)

print("19)", [s for s in range(1, 301) if f(s, 2)]) # Полина выиграет своим 1-ым ходом
print("20)", [s for s in range(1, 301) if f(s, 3) and not(f(s, 1))]) # Полина выиграет 2-ым ходом, но не 1-ым
print("21)", [s for s in range(1, 301) if (f(s, 2) or f(s, 4)) and not(f(s, 2))]) # Вика может выиграть 1-ым или 2-ым ходом, но не гарантированно 1-ым
# 113
# 36 37
# 99
"""
#---------------------6----------------------
"""
# + 2 or + 3 or + 4 or * 2 win >= 229
def f(s, m):
    if s >= 229: return m % 2 == 0
    if m == 0: return False
    h = [f(s + 2, m - 1), f(s + 3, m - 1), f(s + 4, m - 1), f(s * 2, m - 1)]
    return any(h) if m % 2 != 0 else all(h)

# print("19)", [s for s in range(1, 229) if f(s, 2)]) # Ваня выиграет 1-ым своим ходом
# print("20)", [s for s in range(1, 229) if f(s, 3) and not(f(s, 1))]) # Пети не выиграет за 1 ход, но выиграет 2-ым
# print("21)", [s for s in range(1, 229) if (f(s, 2) or f(s, 4)) and (not(f(s, 2)))]) # Ваня выиграет 1-ым или 2-ым ходом, но не гарантированно 1-ым
# 113
# 57 112
# 107
"""
#--------------------7------------------
"""
# + 2 or + 4 or * 3
def f(s, m):
    if s >= 82: return m % 2 == 0
    if m == 0: return False
    h = [f(s + 2, m - 1), f(s + 4, m - 1), f(s * 3, m - 1)]
    return any(h) if m % 2 != 0 else all(h)
    # return any(h) if m % 2 != 0 else any(h) # Для 19-ого (неудачный Петя)

# print("19)", [s for s in range(1, 82) if f(s, 2)]) # Ваня выиграет после неудачного Пети
# print("20)", [s for s in range(1, 82) if f(s, 3) and not(f(s, 1))]) # Петя выиграет 2-ым ходом, но не выиграет 1-ым
# print("21)", [s for s in range(1, 82) if (f(s, 4) or f(s, 2)) and not(f(s, 2))]) # Ваня выиграет 1-ым или 2-ым, но не 1-ым
# 10
# 9 22
# 21
"""
#-------------------8-------------------
"""
from math import *

# - 2 or - 4 or ceil( / 2) win <= 35
def f(s, m):
    if s <= 35: return m % 2 == 0
    if m == 0: return False
    h = [f(s - 2, m - 1), f(s - 4, m - 1), f(ceil(s / 2), m - 1)]
    return any(h) if m % 2 != 0 else all(h)

print("19)", [s for s in range(200, 35, -1) if f(s, 2)]) # Ваня выиграет своим 1-ым ходом
print("20)", [s for s in range(200, 35, -1) if f(s, 3) and not(f(s, 1))]) # Петя выиграет 2-ым, но не 1-ым ходом
print("20)", [s for s in range(200, 35, -1) if (f(s, 4) or f(s, 2)) and (not(f(s, 2)))]) # Ваня выиграет 1-ым или 2-ым, но не гарантированно 1-ым
# 71
# 143 144
# 77
"""
#----------------9----------------

















