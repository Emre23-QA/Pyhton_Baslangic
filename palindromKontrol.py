# palindrom kontrol

kelime=input("kelime giriniz..:")
print(kelime,"'nin tersi",kelime[::-1])

if kelime==kelime[::-1]:
    print(kelime,"bir palindromdur")
else:
    print(kelime,"bir palindrom degildir")
