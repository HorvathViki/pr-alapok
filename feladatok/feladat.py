#Horváth Viktória 10/D 1.csoport
"""
be kérek egy égesz számot, irassuk ki hogy a szám, negatív ,pozítiv vagy nulla.
"""
szam=input("Kérek egy égesz számot: ")
szam = int(szam)
if szam < 0:
    print(f'A megadott szám {szam} negatív.')
elif szam > 0:
    print(f'A megadott szám {szam} pozitív.')
elif szam == 0:
    print(f'A megadott szám {szam} nulla.')
