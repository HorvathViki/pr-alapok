#Horváth Viktória 10_D
#szamonkeres_001.py
"""
Be kérek egy osztályzatott egy-öt irassuk ki
a megadott jegyet értékel és szövegesen 
ha nem megfelelő jegyet adtam akkor irja ki a 
jegy érteket és melle azt a szöveget hogy nem meg felelö jegy 
"""
osztalyzat = input("Kérek egy osztályzatot: ")
osztalyzat = int(osztalyzat)

if osztalyzat == 5:
    print(f"Példás")

elif osztalyzat == 4 :
    print(f"Jó")

elif osztalyzat == 3 :
    print(f"Közepes")

elif osztalyzat == 2 :
    print(f"Elégséges")

elif osztalyzat == 1 :
    print(f"Egyes")

else osztalyzat :
    print(f"A {jegyed} Nem megfelelő jegy")