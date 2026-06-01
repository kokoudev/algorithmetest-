print("compte nombre d'inversion")
with open("C:/Users/USER/Documents/cours/formation_train/trie.txt", "r") as f:
    a = list(map(int, f.read().split()))
S=len(a)//2
A1=a[:S]
A2=a[S:]
inver2=0
inver1= 0
i=0
j=0
R=[]
while i<len(A1) and j<len(A2):
  if A1[i]<=A2[j]:
    R.append(A1[i])
    i+=1
    inver2 += len(A2) - j
  else:
    R.append(A2[j])
    j+=1
    inver1 += len(A1) - i
R+=A1[i:]+A2[j:]
inver=inver1+inver2
print("le resultat de la fusion est : ",R)
print("Nombre d'inversions :", inver)
#je ne compte que les inversion externers pas internse pour les intrnes faux encore les diviser 