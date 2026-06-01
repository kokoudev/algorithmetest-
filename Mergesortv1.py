print("bonjour mergesort algo")
a= list(map(int,input("entrer les nombre : ").split()))
S=len(a)//2
A1=a[:S]
A2=a[S:]
i=0
j=0
R=[]
while i<len(A1) and j<len(A2):
  if A1[i]>A2[j]:
    R.append(A2[j])
    j+=1
  else:
    R.append(A1[i])
    i+=1
R+=A1[i:]+A2[j:]
print("le resultat de la fusion est : ",R)