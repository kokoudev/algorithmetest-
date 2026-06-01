import bisect

def solve_2sum():
    # 1. Charger et trier les données (environ 1 million d'entrées)
    # Créer un set pour éviter les doublons, puis trier
    with open('two_sum.txt', 'r') as f:
        nums = sorted(list(set(int(line.strip()) for line in f)))

    # Ensemble pour stocker toutes les sommes distinctes trouvées
    targets_found = set()
    
    # 2. Parcourir chaque nombre du tableau trié
    for x in nums:
        # On cherche y tel que -10000 <= x + y <= 10000
        # Donc y doit être dans l'intervalle [low, high]
        low = -10000 - x
        high = 10000 - x
        
        # Utiliser la recherche binaire (bisect) pour trouver l'intervalle valide
        # bisect_left : position où insérer 'low' pour garder le tri
        # bisect_right : position après le dernier élément <= 'high'
        idx_start = bisect.bisect_left(nums, low)
        idx_end = bisect.bisect_right(nums, high)
        
        # 3. Ajouter toutes les sommes valides trouvées dans cet intervalle
        for i in range(idx_start, idx_end):
            y = nums[i]
            # Éviter d'ajouter x + x (le même nombre deux fois)
            if y != x:
                targets_found.add(x + y)
                
    return len(targets_found)

# Note : L'exécution peut prendre entre 1 et 5 minutes 
# selon la puissance de votre processeur.
print(f"Nombre de cibles distinctes : {solve_2sum()}")