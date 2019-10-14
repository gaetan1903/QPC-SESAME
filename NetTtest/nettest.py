import time
from scapy.all import *


rep, non_rep = sr(IP(dst='192.168.8.*') / ICMP(), timeout=2)
# ans, unans = sr(IP(dst='192.168.8.100')/TCP(dport=3040), timeout=0.01)

for elem in rep:
    print(elem[1])