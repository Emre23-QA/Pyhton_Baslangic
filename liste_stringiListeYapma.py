#String i liste ye cevirme

kelime="btkakademi"
L=[]
L=list(kelime)
print(L) # ['b', 't', 'k', 'a', 'k', 'a', 'd', 'e', 'm', 'i']
print(L.count("a"))
L.remove("a") # ilk a'yı sil   ['b', 't', 'k', 'k', 'a', 'd', 'e', 'm', 'i']
print(L)
L.pop(2)   # ['b', 't', 'k', 'a', 'd', 'e', 'm', 'i']
print(L)
L.clear()  # []
print(L)
