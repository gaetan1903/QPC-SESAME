import time, threading
from scapy.all import *
listc = []
lists = []
print('debut')
x = time.time()

class Find(threading.Thread):     
    def __init__(self, a, b):
        self.a = a
        self.b = b
        threading.Thread.__init__(self)

    def search(self, a, b):
        global listc
        for i in range(a, b):
            print(time.time() - x , 's :',  f'192.168.8.{i}')
            rep, non_rep = sr(IP(dst=f'192.168.8.{i}') / ICMP(), timeout=0.005)
            for elem in rep:
                if elem[1].type == 0:
                    print('**********************************')
                    print('Connected adress' ,elem[1].src + ' est connecter')
                    listc.append(elem[1].src)
                    print('**********************************')
                    ans, unans = sr(IP(dst=elem[1].src)/TCP(dport=8000), timeout=0.01)
                    for val in ans:
                        if val[1].sport == 8000:
                            print('###################')
                            print('Serveur Trouvee', (val[1].src +  ' est un serveur avec temps:' + str(time.time() - x)))
                            lists.append((val[1].src, (str(time.time() - x) + 's')))
                            print('###################')
                    

    def run(self):
        self.search(self.a, self.b)



p1 = Find(1,50)
p2 = Find(50,100)
p3 = Find(100, 150)
p4 = Find(150,200)

p1.start()
p2.start()
p3.start()
p4.start()

for i in range(200, 250):
    print(time.time() - x , 's :',  f'192.168.8.{i}')
    rep, non_rep = sr(IP(dst=f'192.168.8.{i}') / ICMP(), timeout=0.005)
    for elem in rep:
        if elem[1].type == 0:
            print('**********************************')
            print('Connected adress' ,elem[1].src + ' est connecter')
            listc.append(elem[1].src)
            print('**********************************')

p1.join()
p2.join()
p3.join()
p4.join()

print('temps totaux:', time.time() - x)
print(len(listc), 'connecter')
for i in listc:
    print(i)
print(len(lists), 'serveur')
for i in lists:
    print(i)