#---------------1------------
"""
def is_prost(n):
    dividers = set()
    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            dividers.add(i)
            dividers.add(n // i)
    if len(dividers) > 0:
        return False
    else:
        return True

def summ(n):
    summ = 0
    for i in str(n):
        summ += int(i)
    return summ

for i in range(177000, 177300 + 1):
    if is_prost(i):
        if is_prost(summ(i)):
            print(i, summ(i))
"""
#-----------------2---------------
"""
def is_prost(n):
    dividers = set()
    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            dividers.add(i)
            dividers.add(n // i)
    if len(dividers) > 0:
        return False
    else:
        return True

# Перебор всех чисел из диапазона
for i in range(33333, 55555 + 1):
    # Сумма простых делителей числа
    summ = 0
    # Набираем сумму (можно до корня из i, но до половины надежнее)
    for j in range(2, i // 2 + 1):
        # Если j является делителем и является простым
        if i % j == 0 and is_prost(j):
            # Добавляем это j в сумму
            summ += j
    # Сумма больше 250 и само перебираемое число i делится на эту сумму
    if summ > 250 and i % summ == 0:
        print(i, summ)
"""
#-----------------3----------------
"""
def dividers(n):
    dividers = set()
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            dividers.add(i)
            dividers.add(n // i)
    return dividers

for i in range(135790, 163228 + 1):
    summ = sum(dividers(i))
    if summ > 460000:
        print(len(dividers(i)), sum(dividers(i)))
"""
#-------------4--------------

# for i in range(1):
#     i = 1000125
#     N = 0
#     for j in range(3, i // 2 + 1, 2):
#         if i % j == 0:
#             N += j
#     if N > i:
#         print(i, N)

def f(n):
    dividers = set()
    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            dividers.add(i)
            dividers.add(n // i)

    res = set()
    for j in dividers:
        if j % 2 != 0:
            res.add(j)

    return sum(sorted(res))

# print(f(1000350), sum(f(1000350)))
c = 0
for x in range(10**6, 10**6 + 10000):
    if f(x) > x:
        c += 1
        print(c, x, f(x))
    if c == 5:
        break





















