'''
#-------------1-----------
mask = 255.254.0.0
sett = 11111111.11111110.00000000.00000000
2 ** 17 - 2
131070
'''

#--------------2------------
'''
sett = 192.168.31.0
mask = 255.255.255.0
2 ** 8 - 2 - 10
244
'''

#--------3--------
'''
devc = 192.168.1.1
mask = 255.192.0.0
devc = 11000000.10101000.00000001.00000001
mask = 11111111.11000000.00000000.00000000
sett = 11000000.10000000.00000000.00000000
10000000
'''

#--------------4---------
'''
devc = 205.99.68.249
mask = 255.255.248.0
devc = 11001101.01100011.01000100.11111001
mask = 11111111.11111111.11111000.00000000
sett = 11001101.01100011.01000000.00000000
neww = 11001101.01100011.01000111.11111110
neww = 205.99.71.254
2059971254
'''
#-------------5--------------
'''
devc = 49.26.38.163
mask = 255.255.255.192
devc = 00110001.00011010.00100110.10100011
mask = 11111111.11111111.11111111.11000000
sett = 00110001.00011010.00100110.10000000

(2 ** 6 - 2) / 2

from ipaddress import *

ip_net = ip_network("49.26.38.163/255.255.255.192", False)

c = 0
for i in ip_net:
    c += 1
print((c - 2) / 2)
'''
#------------6---------
'''
from ipaddress import *

#При худшем исходе последние 4 бита IP будут "1111"
#Поэтому bin(35) -> 00100011 превращается в 00110 + 1111
#Слева 8 нулей, справа 3 + A.count("0")
#8 <= 3 + A.count("0") ; A.count("0") >= 5
#Нам надо получить максимальное, поэтому эти 5 нулей в конец
#int("11100000", 2) -> 224
a = []
for i in range(9):
    A = int(((i * "1" + 8 * "0")[:8]), 2)
    net = ip_network(f"248.112.{A}.35/255.255.255.240", False)
    for ip in net:
        ip = (bin(int(ip)))[2:]
        if ip[:16].count("0") == ip[-16:].count("0"):
            a.append(A)
            break
print(a[0])
'''
#-------------7--------------
'''
from ipaddress import *

#Нужно получить минимальный, поэтому от большего к меньшему
for i in range(31, 0, -1):
    net = ip_network(f"242.190.196.159/{i}", False)
    shirokovesh = net.broadcast_address
    # if "242.190.196.159" != shirokovesh НЕПРАВИЛЬНо
    if IPv4Address("242.190.196.159") != shirokovesh:
        print(i)
        break

#242.     190.     196.     159
#11110010.10111110.11000100.10011111
#Answ: 26
#11111111.11111111.11111111.11
#Справа налево считаем, когда хостовая часть будет содержать
#хотя бы один 0 (чтобы не был широковещательным) и хотя бы
#одну 1 (чтобы не был адресом сети)
'''
#-----------8----------
'''
from ipaddress import *

#devc = 111.081.093.127
#devc = 01101111.01010001.01011101
#sett = 111.081.080.0         ^
#sett = 01101111.01010001.01010000
#mask = 255.255.              ^
#int("11110000", 2) -> 240
'''
#---------9-------------
'''
from ipaddress import *

#Наименьшее кол-во нулей в маске?
#devc = 117.73.208.27
#devc = 01110101.01001001.11010000.00011011
#sett = 117.73.192.0
#sett = 01110101.01001001.11000000.00000000
#mask = 11111111.11111111.111
'''
#-------------10------------
'''
from ipaddress import *

net = ip_network("192.168.63.0/255.255.255.128", False)

c = 0
for ip in net:
    ip = (bin(int(ip)))[2:]
    if ip.count("0") % 5 != 0:
        c += 1
print(c)
'''
#--------------11------------
'''
from ipaddress import *

a = []
net = ip_network("172.17.167.18/255.255.240.0", False)
for ip in net:
    shirok = net.broadcast_address
    if IPv4Address(f"{ip}") != shirok:
        a.append(ip)
print(a[-1])
'''
#----------------12-----------
'''
from ipaddress import *

net = ip_network("192.168.32.160/255.255.255.240", False)
c = 0
for ip in net:
    ip = (bin(int(ip)))[2:]
    if ip.count("0") > 21:
        c += 1

print(c)
'''
#----------------13-----------
'''
from ipaddress import *

# devc = 192.168.76.160
# devc = 11000000.10101000.01001100.10100000
# mask = 11111111.11111111.11111111.11110000
# sett = 11000000.10101000.01001100.10100000

# .hosts() позволяет не учитывать адрес самой сети
net = ip_network("192.168.76.160/255.255.255.240", False).hosts()
c = 0
for ip in net:
    ip = (bin(int(ip)))[2:]
    if ip[-1] == "0" and ip[-8:].count("1") % 2 == 0:
        print(ip, ip[-8:], ip[-8:].count("1"), int(ip[-8:], 2)) 
'''
#---------14--------
"""
from ipaddress import *

net = ip_network("195.102.65.64/255.255.255.192")
c = 0
for ip in net:
    ip = (bin(int(ip)))[2:]
    if ip[-8:].count("1") == 4:
        c += 1
        print(ip, ip[-8:], ip[-8:].count("1"), int(ip[-8:], 2))
print(c)
"""
#--------------------15---------
"""
from ipaddress import *

net = ip_network("192.168.248.176/255.255.255.240", False)

c = 0
for ip in net:

    ip = bin(int(ip))[2:]
    if ip.count("0") == ip.count("1"):
        c += 1
print(c)
"""
#------------16---------------
"""
from ipaddress import *

net = ip_network("222.121.128.0/255.255.224.0", False)

c = 0
for ip in net:

    ip = bin(int(ip))[2:].zfill(32)
    if ip[-1] == ip[-2]:
        c += 1
print(c)
"""
#----------17-----------
"""
from ipaddress import *

net = ip_network("172.140.68.0/255.255.248.0", False)

c = 0
for ip in net:

    ip = bin(int(ip))[2:]
    if ip.count("0") > 15:
        c += 1
print(c)
"""
#--------------18--------------
"""
from ipaddress import *

for x in range(10, 31):
    net = ip_network(f"143.131.211.37/{x}", False)
    c = 0
    for ip in net:
        ip = bin(int(ip))[2:]
        if ip.count("1") == 10:
            c += 1
    if c == 15:
        print(x)
"""
#-------------19--------------
"""

uzel 222.190.122.24
sett 222.190.120.0

bin(122) = 1111010
bin(120) = 1111000
3bitmask = 1111*00

max mask = 11111111.11111111.11111000.00000000 = "0" * 11 =>
=> 2 ** 11 variantov = 2048
2048 - adres seti - shirokovesh - adres uzla = 2045

"""
#---------------20-------------
"""
from ipaddress import *

net = ip_network("102.162.200.51/255.255.255.0", False).hosts()

last = 0
for ip in net:
    last = ip

# summa oktatov ip adressa
print(sum(map(int, str(last).split("."))))
"""
#---------------21-------------
"""
from ipaddress import *

net = ip_network("73.148.145.65/255.224.0.0", False).hosts()

last = 0
for ip in net:
    last = ip
print(str(last).replace(".", ""))
"""
#-------------22----------
"""
from ipaddress import *

net = ip_network("172.16.192.0/255.255.192.0", False)

c = 0
for ip in net:
    ip = bin(int(ip))[2:]
    if ip.count("1") % 5 != 0:
        c += 1
print(c)
"""
#-----------23------------
"""
from ipaddress import *

net = ip_network("158.214.121.40/255.255.255.224", False).hosts()

for ip in net:
    print(str(ip).replace(".", ""))
    break
"""
#----------24-------------
"""
from ipaddress import *

net = ip_network("5.2.5.0/255.255.0.0", False)

c = 0
for ip in net:
    ip = bin(int(ip))[2:].zfill(32)
    if ip.count("0") % 25 == 0:
        c += 1
print(c)
"""
#-----------25-----------
"""
uzl1 = 200.154.190.12
uzl2 = 200.154.184.0

uzl1 = 11001000.10011010.10111110.00001100
uzl2 = 11001000.10011010.10111000.00000000
mask = 11111111.11111111.11111000.00000000

13003 15821412133 1820 20


print(bin(200), bin(154))
print(190, bin(190))
print(184, bin(184))
print(12, bin(12))
"""
#-----------25---------------
"""
print(212, bin(212)[2:])
print(192, bin(192)[2:])
print(20, bin(20)[2:].zfill(8))

# sett = 205.154.11000000.00000000
# uzel = 205.154.11010100.00010100
# mask = 255.255.11100000.00000000

print(int("11100000", 2))
"""
#----------------26--------------
"""
from ipaddress import *

net = ip_network("115.192.0.0/255.192.0.0", False)

c = 0
for ip in net:
    ip = bin(int(ip))[2:]
    if ip.count("1") % 3 != 0:
        c += 1
print(c)
"""
#--------27----------
"""
uzl1 = 174.215.202.10110101
uzl2 = 174.215.202.10010011
sett = 174.215.202.11000000

print(181, bin(181)[2:])
print(147, bin(147)[2:])
print(2 ** 6 - 2 - 2)
"""
#----------28------------
"""
from ipaddress import *

net = ip_network("192.168.76.160/255.255.255.240", False)

c = 0
for ip in net:
    ip = bin(int(ip))[2:]
    if ip[-1] == "0" and ip[24:].count("1") % 2 == 0:
        c += 1
print(c)
"""
#--------------29-------------
"""
from ipaddress import *

net = ip_network("52.52.52.52/255.255.240.0", False).hosts()

c = 0
for ip in net:
    c += 1
print(c)
"""
#----------------30---------------
"""
from ipaddress import *

net = ip_network("192.168.32.160/255.255.255.240")

c = 0
for ip in net:
    ip = bin(int(ip))[2:]
    if ip.count("0") > 21:
        c += 1
print(c)
"""
#-------------------31-------------------
"""
from ipaddress import *

net = ip_network("165.44.96.0/255.255.248.0")

c = 0
for ip in net:
    ip = bin(int(ip))[2:]
    if "111" in ip:
        c += 1
print(c)
"""
#------------32----------
"""
from ipaddress import *

net = ip_network("87.226.26.72/255.255.255.252", False)

c = 0
for ip in net:
    ip = bin(int(ip))[2:].zfill(32)
    print(ip)
    if ip.count("0") % 2 == 0:
        c += 1
print(c)
"""
#---------------33---------------
"""
from ipaddress import *

net = ip_network("218.194.82.148/255.255.255.192", False).hosts()

last = 0
for ip in net:
    last = ip
print(last)
"""
#------------34-----------
"""
from ipaddress import *

net = ip_network("123.222.111.192/255.255.255.248", False)

c = 0
for ip in net:
    ip = bin(int(ip))[2:].zfill(32)
    if ip[24:].count("1") % 3 != 0:
        c += 1
print(c)
"""
#-------------35------------
"""
uzl1 = 151.172.115.01111001
uzl2 = 151.172.115.10011100
mask = 255.255.255.
"""
#------------36------------
"""
from ipaddress import *

net = ip_network("172.16.160.0/255.255.240.0", False)

c = 0
for ip in net:
    i = ip
    ip = bin(int(ip))[2:]
    if ip.count("1") % 3 == 0:
        c += 1
        print(i, ip, int(i))
print(c)
"""
#------------36------------
"""
from ipaddress import *

net = ip_network("77.180.176.14/255.255.254.0", False).hosts()

for ip in net:
    print(ip)
"""
#------------37-----------
"""
from ipaddress import *

net = ip_network("153.196.115.75/255.248.0.0", False)

for ip in net:
    print(ip)
"""
#---------------38---------------














