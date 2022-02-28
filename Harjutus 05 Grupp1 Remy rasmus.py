#Remy Rasmus Koptelkov
#10.02.2022
#IT-21

#Tärnid
arvud = [29,87,65,17,90]
for i in range(len(arvud)):
    print("*"*arvud[i])
    
    
print()



#Vanused
vanused = [29,87,65,17,90]
print("Suurim arv:", max(vanused))
print("Väikseim arv:", min(vanused))
print("Kokku:", sum(vanused))
print("Keskmine:", sum(vanused)/len(vanused))


print()







#Duplikaadid
opilased = ['Juhan','Kati','Mario','Mario','Mati']
puh_opilased = []

for i in range(len(opilased)):
    if opilased[i] not in puh_opilased:
        puh_opilased.append(opilased[i])
for i in range(len(puh_opilased)):
    print(puh_opilased[i])
print()






#õpilased
opilased = ['Juhan','Kati','Maarja','Mario','Mati']

print("Vali number, mida soovid muuta: ")
for i in range(len(opilased)):
    print(f"{i+1}, {opilased[i]}")
valik = int(input("Sisesta number: "))
del opilased[valik-1]
uus_nimi = input("Sisesta uus nimi: ")
opilased.insert(valik-1,uus_nimi)
print(opilased)






#nimede lisamine loendisse
nimed= []
for i in range(5):
    nimi = input("Lisa oma nimi: ")
    nimed.append(nimi)
nimed.sort()
print(nimed)
