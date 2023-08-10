masaNo=0
liste=['ali','veli','can','zeynep']
isim=input('isminiz nedir?..')

if isim=='ali':
    masaNo=5
if isim=='veli':
    masaNo=7
if isim=='can':
    masaNo=2
if isim=='zeynep':
    masaNo=10
if isim in liste:
    print(masaNo,"Numaralı masada Rezervasyonunuz var")
if isim not in liste:
    print("Rezervasyonunuz yok")
