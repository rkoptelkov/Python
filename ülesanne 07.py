#############
#ülesanne 07

#01
import math
"""
def tervitada (nimi, keel="de"):
    if keel=="et":
        print(f"Tere {nimi}")
    elif keel=="en":
        print(f"Hey {nimi}")
    else:
        print(f"Hallo {nimi}")
        
n = input("Sisesta nimi: ")
k = input("Vali keel et/en/de: ")
tervitada(n,k)
"""
#leia ruumala

def silindriRuumala(r,h):
    v=math.pi*r**2*h
    return v



def koonuseRuumala(a,h):
    v=(math.pi*a**2*h)/3
    return v

def kuubiRuumala(a):
    v=a**3
    return v
    
def keraRuumala(a):
    v=(4*math.pi*a**3)/3
    return v
    
    
print("********** LEIAME RUUMALA **********")
print("Vali kujund:\n1. Kuup\n2. Kera\n3. Koonus\n4. Silinder\n5. EXIT")

valik= int(input('Vali kujund: '))
if valik==1:
    s=int(input("Sisesta kuubi külg: "))
    print(kuubiRuumala(s))
elif valik==2:
    s=int(input("Sisesta kera raadius: "))
    print(keraRuumala(s))
elif valik==3:
    s=int(input("Sisesta koonuse raadius: "))
    h=int(input("Sisesta koonuse kõrgus: "))
    print(koonuseRuumala(s,h))
elif valik==4:
    r=int(input("Sisesta silindri raadius: "))
    h=int(input("Sisesta silindri kõrgus: "))
    print(silindriRuumala(r,h))




