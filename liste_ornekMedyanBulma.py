L=[]
while True:
    TC=int(input("TC GİR..:"))
    if TC in L:
        i=L.index(TC)
        print("Muayene sirasi..:",i+1)
    elif TC==0:
        print(L[0])
        L.pop(0)
        print(L[0],"TC numarali hasta iceri giriniz")
    else:
        L.append(TC)
        print(TC,"TC numarali hasta siraya alindi")
        
        
        
