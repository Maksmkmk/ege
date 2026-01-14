#---------1-------------
"""
# инв кон диз имп экв
# ¬w∧(y∨z→y∧¬x)
def f(x, y, z, w):
    return (((not (w))) and ((((y) or (z)) <= ((y) and ((not (x)))))))
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if f(x, y, z, w) == 1:
                    print(x, y, z, w)
"""
#--------2----------
"""
# инверсия кон диз импликация эквиваленция
print("a b c")
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            if ((a) == (((b and b) <= c))):
                print(a, b, c)
"""
#---------------3------------
"""
# инверсяи конъюнкция дизъюнкция импликация эквиваленция
# (z≡¬x)→((w→¬y)∧(y→x))
def f(x, y, z, w):
    return int(  (((z) == ((not x)))) <= (((((w) <= ((not y)))) and (((y) <= (x)))))  )
c = 0
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                c += 1
                print(c, "    ", x, y, z, w, "    ", f(x, y, z, w))
#       x y z w   F
#15     1 1 1 0   1
#7      0 1 1 0   0
#14     1 1 0 1   0

#       y z x w   F
#15     1 1 1 0   1
#7      1 1 0 0   0
#14     1 0 1 1   0
"""
#----------------4----------
"""
# ¬(z→w)∨(x→y)∨¬x
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ( (not(z <= w)) or (x <= y) or (not(x)) ) == 0:
                    print(x, y, z, w)
"""
#---------------5------------------
"""
#w∨(y∧¬x)∨¬z
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ( (w) or (((y) and ((not(x)))) or ((not(z)))) ) == 0:
                    print(x, y, z, w)
"""
#------------------6-------------
"""
# ¬(y→(x≡w))∧(z→x)
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ( (not(((y) <= (((x) == (w)))))) and (((z) <= (x))) ):
                    print(x, y, z, w)
"""
#--------------7-----------
"""
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ( ((w <= y) <= x) or (not(z)) ) == 0:
                    print(x, y, z, w)
"""
#----------------------8-----------------
"""
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ( (not(y <= w)) or (x <= z) ) == 0:
                    print(x, y, z, w)
"""
#---------------------9-------------------
"""
# инверсия кон диз импликация эквиваленция
print("k l m n")
for k in range(2):
    for l in range(2):
        for m in range(2):
            for n in range(2):
                if ( ((not(n))) or (k) and ((not(m))) or (((l == m))) ) == 0:
                    print(k, l, m, n)
"""
#-------------------10---------------
"""
def f(a, b, c, d):
    return ( (not(c)) and (((not (a)) <= (not (d))) <= (not (b))) )

print("a b c d")
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if f(a, b, c, d):
                    print(a, b, c, d)
"""
#----------------11-------------------
"""
def f(x, y, z, w):
    return int( (x and y) or ((z == y) and w) )

c = 0
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                c += 1
                print(c, "    ", x, y, z, w, "    ", f(x, y, z, w))
"""
#----------12--------------
"""
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ( (x and (not(y))) or (y == z) or w ) == 0:
                    print(x, y, z, w)
"""
#---------------------13----------
"""
def f(x, y, z, w):
    return ( not(w <= (x == y)) and (z <= x) )

print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if f(x, y, z, w):
                    print(x, y, z, w)
"""
#--------------14---------------
"""
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ( (y <= x) and (not(w)) and (z) ):
                    print(x, y, z, w)
"""
#-----------------15------------------
"""
print("p1 p2 p3 p4")
for p1 in range(2):
    for p2 in range(2):
        for p3 in range(2):
            for p4 in range(2):
                if ( (p3 <= p1) <= (p4 or (not(p2))) ) == 0:
                    print(p1, p2, p3, p4, sep = "  ")
"""
#-----------------16-------------
"""
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((not(w <= x)) or (y <= z) or (not(y))) == 0:
                    print(x, y, z, w)
"""
#-----------------17------------------
"""
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ( not((z <= x) and (w or y) and (not(w == x))) ) == 0:
                    print(x, y, z, w)
"""
#---------------18------------------
"""
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ( (x or (y == z)) and (not(w <= y)) ):
                    print(x, y, z, w)
"""
#---------------19-----------------
"""
print("x y z w")
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                if (not ((z <= x) and (w or y) and (not(w == x)))) == 0:
                    print(x, y, z, w)
"""
#---------------20-------------
"""
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                print(x, y, z, w, int( ((1 == w) == (not((w and x) or y))) <= z))
"""
#---------------21--------------
"""
def f(x, y, z, w):
    return not((((((w and x) == x) or True) <= z) or (not(x))) and y)

print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if f(x, y, z, w) == 0:
                    print(x, y, z, w)
"""
"""
# выбираем ёлку
height = 6  # высота
trunk_width = 3  # ширина ствола

# решаем, куда поставить
offset = 10  # сдвиг вправо

# вешаем звезду
print(' ' * (height - 1 + offset) + '★')

# расправляем ветки
for i in range(1, height + 1):
    line = ''
    for j in range(2*i - 1):
        # вешаем игрушки
        line += '*' if j % 2 == 0 else 'o'
    print(' ' * (height - i + offset) + line)

# Дед Мороз принёс подарки
print(' ' * (height - trunk_width//2 - 1 + offset - 2) + '🎁' + '|' * trunk_width + '🎁')

# новогоднее поздравление
print("\nС Новым годом, друзья! 🎉")
print("Желаем, чтобы в 2026-м радость крутилась в бесконечном цикле, а экзамены запускались, как идеальный код, с первого раза и без ошибок.")
"""
#--------------22------------
"""
print("a b c d")
for a in 1,0:
    for b in 1,0:
        for c in 1,0:
            for d in 1,0:
                f = ((a == b) or (not(c == d))) and (b <= (not c))
                if f == 0:
                    print(a, b, c, d)
"""
#-------------23------------

print("x y z w")

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (  (z == (not(y))) and ((not(x)) or y) and w  ):
                    print(x, y, z, w)








