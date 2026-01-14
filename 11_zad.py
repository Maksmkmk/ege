#------------1------------
"""
from math import *

len_nomera = 623
alf = 1267 + 10
i_glub = 11
I_nomera = i_glub * len_nomera
I_nomera = ceil(I_nomera / 2**13)
N_kolvo = 2048
V_obsh = N_kolvo * I_nomera // 2**10
print(V_obsh)
"""
#-----------2-------------
"""
from math import *

len_nomera = 79
alf = 10 + 4080
i_glub = ceil(log2(alf))
I_nomera = i_glub * len_nomera
I_nomera = ceil(I_nomera / 2**3)
N_kolvo = 65536
V_obsh = N_kolvo * I_nomera // 2**10
print(V_obsh)
"""
#--------------3--------------
"""
from math import *

len_nomera = 102
alf = 10 + 510
i_glub = ceil(log2(alf))
I_nomera = i_glub * len_nomera
I_nomera = ceil(I_nomera / 2**3)
V_obsh = 7 * 2**23
N_kolvo = V_obsh // (I_nomera * 2 **3)
print(N_kolvo)
"""
#-------------4-------------
"""from math import *

Lp = 23
Ap = 12
ip = ceil(log2(Ap))
Ip = ceil(ip * Lp / 8) * 8 #биты
N = 297
V = 13068 * 2**3 #биты
Id = (V / N - Ip) / 2**3 #байты
print(Id)
"""
#------------5-----------
"""
from math import *

a = []
for A in range(1, 100):
    L = 246
    i = ceil(log2(A))
    I = ceil(i * L / 8) * 8 #бит
    N = 703_569
    V = N * I #бит
    if V <= 77 * 2 ** 23:
        a.append(A)
print(max(a))
"""
#----------6--------
"""
from math import *

for A in range(1, 1000):
    L = 172
    i = ceil(log2(A))
    I = ceil(L * i / 8) * 8 # биты
    N = 356984
    V = N * I #байты
    if V >= 54 * 2 ** 23:
        print(A)
        break
"""
#----------7-------------
"""
from math import *

Lp = 34
Ap = 36
ip = ceil(log2(Ap))
Ip = ceil(ip * Lp / 2 ** 3) #байты
N = 10240
V = 20 * 2 ** 20 #байты
#V = N * (Ip + Id)
Id = V / N - Ip
print(Id)
"""
#----------8---------
"""
from math import *

L = 4
A = 26
i = ceil(log2(A))
I = ceil(L * i / 8) #байты
N = 10
V = I * N
print(V)
"""
#-----------9-------------
"""
from math import *

L = 163
A = 1500 + 10
i = ceil(log2(A))
I = ceil(i * L / 8) * 8 #бит
N = 65536
V = N * I #бит
print(V / 2 ** 13)
"""
#---------10---------
"""
from math import *

Lp = 31
Ap = 10 + 26
ip = ceil(log2(Ap))
Ip = ceil(Lp * ip / 8) #байты
N = 128
V = 12 * 2 ** 10 #байты
#V = N * (Ip + Id)
Id = V / N - Ip
print(Id)
"""
#----------11--------
"""
from math import *

for L in range(100):
    A = 10 + 17
    i = ceil(log2(A))
    I = ceil(L * i / 8) * 8 #биты
    N = 7_564_230
    V = N * I #биты
    if V > 31 * 2 ** 23:
        print(L)
        break
"""
#------------12----------
"""
from math import *

a = []
for A in range(1, 100000):
    L = 34
    i = ceil(log2(A))
    I = ceil(L * i / 8) * 8 + 28 * 8 #биты
    N = 2000
    V = N * I #биты
    if V <= 124 * 2 ** 13:
        a.append(A)
print(max(a))
"""
#---------------13--------------
"""
from math import *
# x = ?

for x in range(1, 100):
    A = 10 + 52 + x
    L = 53
    i = ceil(log2(A))
    I = ceil(L * i / 8) # байт
    N = 2000
    V = I * N
    if V <= 93 * 2 ** 10:
        last = x
print(last)
"""
#--------------14---------------
"""
from math import *

for A in range(1, 100):
    L = 1231
    i = ceil(log2(A))
    I = ceil(L * i / 8) * 8 # биты
    N = 523872
    V = N * I # биты
    if V >= 432 * 2 ** 23:
        print(A)
        break
"""
#-------------15---------------
"""
from math import *

l = 8
A = 7
i = ceil(log2(A))
I = ceil(l * i / 8) # байты
N = 42
V = N * I + N * 8
print(V)
"""
#--------------16------------
"""
from math import *

for l in range(100):
    A = 10 + 70
    i = ceil(log2(A))
    V = ceil(l * i / 8)
    if 1_234_567 * V > 24 * 2 ** 20:
        print(l)
        break
"""
#---------------------17--------------------

from math import *

for A in range(1, 1000):
    l = 21
    i = ceil(log2(A))
    k = 1_222_333
    V = ceil(l * i / 8) * k
    if V >= 30 * 2 ** 20:
        print(A, i)
        break
























