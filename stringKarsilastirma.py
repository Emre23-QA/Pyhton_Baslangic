sifre="1234"
kullanici='talat'

k_giris=input("kullanici adini giriniz: ")


if k_giris == 'talat':
    s_giris=input("sifre giriniz: ")
    if s_giris == "1234":
        print("hosgeldiniz")
    else:
        print("sifre hatali")
else:
    print("kullanici adi hatali")

