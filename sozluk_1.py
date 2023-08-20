
# sözlük olusturma
S={'bir':1,'iki':2,'üç':3,'dört':4}
print(S)
# S.get(anahtar,mesaj):  girilen anahtarın değerini döndürür
#                      eğer anahtarın  yoksa mesajı yazdırır
S.get('bir',"yok")
S.get('üç',"yok")
S.get('yedi',"yok")

# S.pop(anahtar): anahtar ve değerini siler. ve sildiği değeri döndürür
S.pop('üç')
print(S)

#S.keys(): anahtarları döndürür
S.keys()

#S.values(): değerleri döndürür
S.values()

# sözlüğü döndürür
S.items()


