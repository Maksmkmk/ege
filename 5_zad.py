for n in range(100, 100000):
    lst = []
    for i in range(len(str(n)) - 2):
        lst.append(int(str(n)[i:i + 3]))
    res = max(lst) - min(lst)
    if res == 415:
        print(n)
        break
