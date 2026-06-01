print("karasuba solo - Multiplication de deux grands nombres")

# Lire les deux nombres à multiplier
a = int(input("entrer un premier nombre : "))
b = int(input("entrer un second nombre : "))

# Variables temporaires pour ne pas perdre les valeurs initiales
S1 = a
S2 = b

# Compter le nombre de chiffres du premier nombre
C1 = 0
while S1 != 0:
    S1 = S1 // 10
    C1 = C1 + 1

# Compter le nombre de chiffres du second nombre
while S2 != 0:
    S2 = S2 // 10
    C2 = C2 + 1

# Calculer la moitié du nombre de chiffres pour chaque nombre
mc1 = C1 // 2
mc2 = C2 // 2

# Créer le diviseur pour séparer en deux parties (puissance de 10)
D1 = 10 ** mc1
D2 = 10 ** mc2

# Décomposer le premier nombre : a = A * 10^mc1 + B
A = a // D1  # Partie haute
B = a % D1   # Partie basse

# Décomposer le second nombre : b = C * 10^mc2 + D
C = b // D2  # Partie haute
D = b % D2   # Partie basse

# Calcul de l'algorithme Karatsuba avec 3 multiplications au lieu de 4
E1 = A * C        # Multiplication des parties hautes
E2 = B * D        # Multiplication des parties basses
E3 = (A + B) * (C + D)  # Multiplication des sommes
E4 = E3 - E1 - E2  # Partie centrale (produit croisé)

# Combinaison finale : (A*C)*10^(2*mc1) + (E4)*10^mc1 + (B*D)
R = E1 * 10 ** (2 * mc1) + E4 * 10 ** mc1 + E2

print("le resultat de la multiplication est : ", R)