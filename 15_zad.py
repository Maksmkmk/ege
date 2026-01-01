#--------1-------------
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