L1=[1,2,3]
L2=[4,5]
#1)
L3=L1+L2
print(L3) #[1, 2, 3, 4, 5]
#2) L1.extend(L2)--> L1 e L2 ekler. L1=L1+L2 gibi. L1'in  devamına KALICI olarak ekler
L1.extend(L2)
print(L1)
