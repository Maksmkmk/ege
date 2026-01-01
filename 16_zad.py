#-----------1----------
"""
from functools import *

@lru_cache(None)
def f(n):
    if n <= 5:
        return 1
    else:
        return n + f(n-2)

for i in range(1, 3000):
    f(i)

print(f(2126) - f(2122))
"""
#----------------2----------
"""
from functools import *

@lru_cache(None)
def f(n):
    if n >= 4025:
        return n
    if n < 4025:
        return n * 2 + f(n + 2)

for i in range(3000, 0, -1):
    f(i)

print(f(82) - f(81))
"""
#---------------3---------------
"""
from functools import *

@lru_cache(None)
def f(n):
    if n < 110:
        return n
    else:
        return n + f(n - 1)

for i in range(3000):
    f(i)

print(f(2025) - f(2021))
"""
#------------------4-----------
"""
def f(n):
    if n <= 10:
        return n
    elif n % 2 == 0:
        return 2 * f(n - 2) + 6
    else:
        return f(n - 1) + 2 * n

# Сумма цифр значения f(27) - f(20)
print(sum(int(x) for x in str(f(27) - f(20))))
"""
#---------------5--------------
"""
from functools import *

@lru_cache(None)
def f(n):
    if n < 10:
        return n - 1
    elif n % 2 == 0:
        return 3 * n - 1 + f(n - 3)
    else:
        return 5 * n + 2 + f(n - 4)

for i in range(5000):
    f(i)

print(f(4445) - f(4444))
"""
#---------------6--------------
"""
from functools import *

@lru_cache(None)
def f(n):
    if n < 7:
        return 7
    if n % 3 != 0:
        return 5 - f(n - 1)
    else:
        return 3 + f(n - 1)

for i in range(3500):
    f(i)

print(f(3015))
"""
#-----------------7-----------------
"""
from functools import *

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    else:
        return 2 * n + f(n - 1)

for i in range(1, 58000):
    f(i)

# Квадрат суммы цифр значения f(57693)
print(sum(int(x) for x in str(f(57693))) ** 2)
"""
#-----------------8----------------
"""
from functools import *

@lru_cache(None)
def f(n):
    if n <=3:
        return 1
    else:
        return (n + 3) * f(n - 2)

for i in range(2500):
    f(i)

print(f(2028) / f(2024))
"""
#----------------9-------------
"""
from functools import *

@lru_cache(None)
def f(n):
    if n < 3:
        return 2
    if n > 2 and n % 2 == 0:
        return 2 * f(n - 2) - f(n - 1) + 2
    else:
        return 2 * f(n - 1) + f(n - 2) - 2

for i in range(200):
    f(i)

print(f(170))
"""
#----------------10---------
"""
from functools import *

@lru_cache(None)
def f(n):
    if n >= 2222:
        return n
    else:
        return f(n + 5) + 7

for i in range(2500):
    f(i)

print(f(45) - f(49))
"""
#--------------11----------------
"""
from functools import *

@lru_cache(None)
def f(n):
    if n >= 10_000:
        return n
    if n % 2 == 0:
        return f(n + 2) - 3
    else:
        return f(n + 2) + 1

for i in range(100_000, 10, -1):
    f(i)

print(f(94) - f(80))
"""
#--------------12---------------
"""
from functools import *

@lru_cache(None)
def f(n):
    if n < 5:
        return 4
    return 4 * f(n - 4)

for i in range(5000):
    f(i)

print(f(4444)/f(4400))
"""
#-------------13--------------
"""
from functools import *

@lru_cache(None)
def f(n):
    if n >= 2024:
        return 1
    return f(n + 2) + f(n + 4)

for i in range(3000, 0, -1):
    f(i)

a = set()
for i in range(150000, -100000, -1):
    if i > 0:
        a.add(f(i))

print(len(a))
"""
#-----------14--------------














