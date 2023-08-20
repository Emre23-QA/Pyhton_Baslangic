# GİRİLEN TÜRKÇE GÜN ADININ İNGİLİZCE KARŞILIĞINI VEREN SÖZLÜK

while True:

    gun=input("Turkce gun adi..:")
    if gun!='bitti':
        TrEn={'pazartesi':'monday','salı':'tuesday','çarşamba':'wendesday','perşembe':'thursday','cuma':'friday','cumartesi':'saturday','pazar':'sunday'}
        print("ingilizce..:",end=" ")
        print(TrEn.get(gun,'bu kelime sözlükte yok!'))
    else:
        break
