#feladat_008
sebesség = input("Add meg a sebességet:")
sebesség=int(sebesség)
if sebesség == 0:
    print(f'Megálltál')
    if sebesség < =50:
    print(f'Büntetés 15000FT')
    if sebesség < =65:
    print(f'Büntetés 30000FT')
    elif sebesség < =80:
    print(f'Büntetés 60000')
    elif sebesség < =100:
    print(f'Elveszik a jogositványt')
