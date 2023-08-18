L=[]
Topla=0
for i in range(0,5):
    sayi=int(input("sayi gir:"))
    L.append(sayi)
    Topla+=sayi
print("en kucuk ve en buyuk sayilarin toplami",max(L)+min(L))
print("aritmetik ortalama=",Topla/len(L))
    
    
