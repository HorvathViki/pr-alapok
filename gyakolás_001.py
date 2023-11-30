#létrehozok  egy jelszot , irjuk ki hogy a belépéshez kérek jelszot és ha 5 szor rossz jelszot add meg akkor ki irja program hogy 
#"rossz jelszot addtqal meg tobb lehetoseged nincs" ha a jelszo jo akkor belephetel és vege a programnak

jelszo = "kkszki01"
proba=0
keres=None
while jelszo!=keres or proba < 5:
    keres=input("Add meg a jelszót: ")
    proba+=1
    if proba==5:
        print("Nem jó a jelszó ")
        break
    if keres == jelszo:
        print("Sikeres berlépés ")
        break


