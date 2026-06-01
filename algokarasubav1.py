
print("bonjour algorithme de karasubat  teste")
a= int(input("entrer un nombre : "))
b= int(input ("entrer le second nombre : "))
s1=a
s2=b
C1=0
C2=0
while s1!=0:
    s1 = s1//10
    C1=C1+1
print("le nombre de chiffre du premier nombre est : ",C1)
while s2!=0:
    s2 = s2//10
    C2=C2+1 
print("le nombre de chiffre du second nombre est : ",C2)

ms1= C1//2
print("le nombre de chiffre du premier nombre divise par 2 est : ",ms1)
ms2= C2//2
print("le nombre de chiffre du second nombre divise par 2 est : ",ms2)


D1= 10**ms1
print("D1 est : ",D1)
D2= 10**ms2
print("D2 est : ",D2)
a1= a//D1
print("a1 est : ",a1)
a0= a%D1
print("a0 est : ",a0)
b1= b//D2  
print("b1 est : ",b1) 
b0= b%D2
print("b0 est : ",b0)
E1= a1*b1
print("E1 est : ",E1)
E2= a0*b0
print("E2 est : ",E2)
E3= (a1+a0)*(b1+b0)
print("E3 est : ",E3)
R= E1*10**(2*ms1) + (E3-E1-E2)*10**ms1 + E2
print("le resultat de la multiplication est : ",R)