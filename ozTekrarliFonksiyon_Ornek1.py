# üstalma fonk--- rekürsif fonk ile
def ustel(a,b):
    if b==0:
        return 1
    else:
        return a*ustel(a,b-1) #2*2*2*2*1
a= int(input("tabanı gir"))
b= int(input("üssü gir"))
print (ustel(a,b))
