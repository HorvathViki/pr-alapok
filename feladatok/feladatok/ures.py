#Horváth Viktória    10/D    11.30
#sorszám : 7
# 1 es feladat 
# A készits egy rövid programot amely 1 és 3 között generál véletlen számot ,
#majd összehasonlitja ezt a felhasznalo által megadott, szintén ebbe a tartományba 
#eső számmal ! Az összehasonlitasal eredményrol tajekoztassa a felhasznalot

import random  
random.randint = random.randint(1,3)
veletlensz = input("Kérek egy számot 1 és 3 között! ")
veletlensz = int(veletlensz)
if veletlensz == random.randint:
    print(f"ugyan az a te számod {veletlensz } mint a random szám {random.randint}")
elif random.randint < veletlensz :
    print(f"A te számod {veletlensz} nagyobb mint a random szám {random.randint}")
elif veletlensz < random.randint:
    print(f"A te számod {veletlensz} kisebb mint a random szám {random.randint}")
else :
    print(f"Ezt nem tudom értelmezni")

