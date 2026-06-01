print("bonjour algorithme de Mergesort")
with open("C:/Users/USER/Documents/cours/formation_train/trie.txt", "r") as f:
     a = list(map(int, f.read().split()))
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