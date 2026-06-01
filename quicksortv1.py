print("bienvenue algorithme de quick sort")

# Charger les données depuis un fichier texte
with open("C:/Users/USER/Documents/cours/formation_train/trie.txt", "r") as f:
    T = list(map(int, f.read().split()))

# Compteur global pour tracer le nombre de comparaisons effectuées
comparaisons = 0

# ---- FONCTION MEDIANE DES TROIS (pour Q3) ----
def mediane(arr):
    # Calcule l'index du pivot qui est la médiane entre premier, milieu et dernier élément
    n = len(arr)
    first_val = arr[0]  # Premier élément
    # Pour taille paire 2k → index k-1, pour impaire → index n//2
    mid_index = (n - 1) // 2
    mid_val = arr[mid_index]  # Élément du milieu
    last_val = arr[n - 1]  # Dernier élément

    # Déterminer quel des 3 éléments est la médiane
    if (first_val <= mid_val <= last_val) or (last_val <= mid_val <= first_val):
        return mid_index
    elif (mid_val <= first_val <= last_val) or (last_val <= first_val <= mid_val):
        return 0
    else:
        return n - 1

# ---- FONCTION QUICKSORT AVEC 3 STRATÉGIES DE PIVOT ----
def quicksort(arr, question):
    # question : 1=premier élément, 2=dernier élément, 3=médiane des trois
    global comparaisons
    
    # Cas de base : tableau de 0 ou 1 élément est déjà trié
    if len(arr) <= 1:
        return arr

    # Compter les comparaisons : m-1 comparaisons pour partitionner m éléments
    comparaisons += len(arr) - 1

    # Sélectionner le pivot selon la stratégie choisie (question)
    if question == 1:
        pivot_index = 0  # Stratégie 1 : premier élément
    elif question == 2:
        pivot_index = len(arr) - 1  # Stratégie 2 : dernier élément
    elif question == 3:
        pivot_index = mediane(arr)  # Stratégie 3 : médiane des trois

    # Permuter le pivot en première position
    arr[0], arr[pivot_index] = arr[pivot_index], arr[0]

    # Récupérer la valeur du pivot
    p = arr[0]
    
    # Partitionner : éléments < pivot à gauche, éléments >= pivot à droite
    g = []  # Gauche (éléments plus petits)
    d = []  # Droite (éléments supérieurs ou égaux)

    for x in arr[1:]:
        if x < p:
            g.append(x)
        else:
            d.append(x)

    # Récursivement trier les deux partitions et combiner
    return quicksort(g, question) + [p] + quicksort(d, question)


# ---- TEST Q1 : pivot = premier élément ----
comparaisons = 0
quicksort(T[:], 1)
print("Q1 - Premier élément   :", comparaisons)

# ---- TEST Q2 : pivot = dernier élément ----
comparaisons = 0
quicksort(T[:], 2)
print("Q2 - Dernier élément   :", comparaisons)

# ---- TEST Q3 : pivot = médiane des trois ----
comparaisons = 0
quicksort(T[:], 3)
print("Q3 - Médiane des trois :", comparaisons)