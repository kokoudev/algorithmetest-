import bisect

def find_t_sum(numbers):
    """
    Trouve toutes les paires de nombres dont la somme est entre -10000 et 10000
    et renvoie le nombre de sommes uniques trouvées.
    """
    nums = sorted(list(set(numbers)))
    targets_found = set()
    
    # Parcourir chaque nombre du tableau trié
    for x in nums:
        low = -10000 - x
        high = 10000 - x
        
        # Utiliser la recherche binaire (bisect) pour trouver l'intervalle valide
        idx_start = bisect.bisect_left(nums, low)
        idx_end = bisect.bisect_right(nums, high)
        
        # Ajouter toutes les sommes valides
        for i in range(idx_start, idx_end):
            y = nums[i]
            # Éviter d'ajouter x + x
            if y != x:
                targets_found.add(x + y)
                
    return len(targets_found)

def solve_2sum():
    # Charger et trier les données si le fichier existe
    try:
        with open('two_sum.txt', 'r') as f:
            nums = sorted(list(set(int(line.strip()) for line in f)))
    except FileNotFoundError:
        # Fallback pour test local sans le fichier
        return find_t_sum([1, 2, 3, 4, 5, -1, -2, 0])

    return find_t_sum(nums)

if __name__ == '__main__':
    print("Execution du Two Sum avec le fichier local two_sum.txt...")
    # Note : L'exécution peut prendre entre 1 et 5 minutes selon le fichier
    try:
        result = solve_2sum()
        print(f"Nombre de cibles distinctes : {result}")
    except Exception as e:
        print(f"Erreur lors de l'exécution : {e}")