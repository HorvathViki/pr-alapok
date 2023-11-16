#feladat_009
"""
Kérjük be két számot,szám1 és szám2.
Hasónlitsuk össze a két számot, és irrasuk ki, hogy
a szám1 kisebb minta szám2,
vagy a szám2 kisebb mint szám1,
vagy egyenlő.
"""
szám1 = input("Kérek egy számot: ")
szám2 = input("Kérek egy másik számot: ")
szám1 = int(szám1)
szám2 = int(szám2)

"""
if szám1 < szám2:
    print("szám1 kisebb mint szám2")

elif szám1 == szám2:
    print("szám1 egyenlő szám2-vel")

else:
   print("szám2 kisebb mint szám1")
  
 """

 
if szám1 < szám2:
    print(f'szám1 kisebb mint szám2')

if szám2 < szám1:
    print(f'szám1 egyenlő szám2-vel')

if szám1 == szám2:
   print(f'szám2 kisebb mint szám1')

 

 