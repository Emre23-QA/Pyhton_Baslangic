#dikdortgen uzunluk ve alan hesaplama
def alan(x,y):
    Alan=x*y
    return Alan
def cevre(x,y):
    Cevre=(x+y)*2
    return Cevre

x=int(input("dikdortgenin uzun kenarını gir:"))
y=int(input("dikdortgenin kısa kenarını gir:"))
print("Dikdörtgenin alanı=",alan(x,y),"m2")
print("Dikdörtgenin cevresi=",cevre(x,y),"m")
