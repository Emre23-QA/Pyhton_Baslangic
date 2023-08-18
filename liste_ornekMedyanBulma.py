#MEDYAN
L=[]
elemanSayisi=int(input("liste kac elemanli olsun:"))

if elemanSayisi%2==1:
    for i in range(0,elemanSayisi): # tek elemanlı liste olusturma
        sayi=int(input("sayi gir:"))
        L.append(sayi)
    L.sort()
    print(L[int((len(L)-1)/2)])
else:
    for i in range(0,elemanSayisi): # cift elemanlı liste olusturma
        sayi=int(input("sayi gir:"))
        L.append(sayi)
    L.sort()
    print((L[int(len(L)/2-1)]+L[int(len(L)/2)])/2)

