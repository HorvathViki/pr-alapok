
darab_karakter = 1
sor = 1
while sor <= 7:
      oszlop = 1
      while oszlop <= darab_karakter:
          print('O ', end='')
          oszlop = oszlop + 1
      print('')
      darab_karakter = darab_karakter + 1
      sor = sor + 1       



sorokszam = int(input("kérek egy egész pozítiv számot"))
ujsorokszam = int (sorokszam/2)
darab_karakter = 1
sor = 1
while sor <= ujsorokszam:
      oszlop = 1
      while oszlop <= darab_karakter:
          print('O ', end='')
          oszlop = oszlop + 1
      print('')
      darab_karakter = darab_karakter + 1
      sor = sor + 1       
darab_karakter = ujsorokszam
sor = 1
while sor <= ujsorokszam:
      oszlop = 1
      while oszlop <= darab_karakter:
          print('O ', end='')
          oszlop = oszlop + 1
      print('')
      darab_karakter = darab_karakter - 1
      sor = sor + 1       
