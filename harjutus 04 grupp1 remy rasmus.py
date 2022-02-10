#harjutus 04
#Remy Rasmus Koptelkov
#03.02.2022
#Ruutude ja kuupide tabel
for i in range(1,11):
    ruut = i**2
    kuup = i**3
    print(f"{i:5} {ruut:5} {kuup:5}")







#Pank
konto = 0
raha = 10000 # muuda int(input("Pane raha panka: "))
intress = 0.05
aastad = 5 # muuda int(input("Vali aastad: "))
konto += raha
print(f"{'Aasta':4} {'Algsumma':10} {'Intress':10} {'Aasta lõpuks':10}")
for i in range (aastad):
    kasum = konto*intress
    print(f"{i+1:4} {konto:10.2f},{kasum:10.2f},{konto+kasum:10.2f}")
    konto+=kasum
    








#Arvamismäng
import random

loop = 1
korrad = 1
suv = random.randint(1,10)
while loop==1:
    
    if korrad <=3:
        arv = int(input("Arva number 1-10: "))
    else:
        veel = input("Tahad veel mängida? Jah/Ei: ")
        if veel=="Jah":
            korrad = 0
        else:
            loop = 0
    korrad += 1
    if arv == suv:
        print ("Ära arvasid!")
        loop = 0
    else:
        print("Ei arvanud ära")
    
    print(suv, arv)
input()
    






#Viisikud
for i in range (1,101):
    if i%5==0:
        print(i)





#Pisike korrutustabel
for i in range(1,6):
    for j in range(1,6):
        print('{0:>3}'.format(j*i), end=" ")
    print()





#Paaris ja Paaritu
for i in range (1,101):
    if i%2==0:
        print(f"{i} paaris")
    else:
        print(f"{i} paaritu")





#Loto
from random import randrange
for i in range (1,6):
    print(randrange(0,9), end="")
print()



#Tärnid
for i in range(1,6):
    for j in range(1,6):
        print('* ', end='')
    print()      
#Kasvav kolmnurk
for i in range (1,6): 
    print(i*"* ")
    
#Kahanev kolmnurk
hoid = 6
for i in range (1,hoid+1):
    print(hoid*"* ")
    hoid = hoid-1





#Jalgpalli meeskond
sugu=input("Sugu (Mees või Naine): ")
if sugu=="Mees":
    vanus=int(input("Sisesta oma vanus: "))
    if vanus>=16 and vanus<=18:
        print("Sa oled meeskonnas.")
else:
    print("Ei sobi tiimi lol F")


       





#Juubel
synd = input("Sisesta sünniaeg kujul dd.mm.dddd: ")
p, k, a = synd.split(".")
vanus = 2022 - int(a)
if vanus%5 == 0:
    print("On juubel")
else:
    print("Ei ole juubel")


#matemaatika
arv1 = int(input("Sisesta arv 1:  "))
arv2 = int(input("Sisesta arv 2:  "))
tehe = input("\n 1) +\n 2) -\n 3) *\n 4) /\vali tehe: ")

if tehe=="+":
    vastus=arv1 + arv2
elif tehe=="-":
    vastus=arv1 - arv2
elif tehe==":":
    vastus=arv1 / arv2
else:
    vastus=arv1 * arv2
print(f"{arv1}{tehe}{arv2}={vastus}")


#ruut
a = int(input("1. kylg: "))
b = int(input("2. kylg: "))

if a==b:
    print("Ruut")
else:
    print("Ristkülik")
    

#Müük
hind = int(input("sisesta hind: "))
if hind <= 10:
    ale=0.1
else:
    ale=0.2
    
vastus = hind-(hind*ale)
print("vastus on",vastus,"eurot")







