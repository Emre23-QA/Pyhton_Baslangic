L=[1,2,3,4,5,6]
deger=int(input("sayi gir:"))
if deger in L:
    indis=L.index(deger)
    print("Aranan",indis,"indis degerinde bulundu")
else:
    print("aranan deger bulunamadı")
