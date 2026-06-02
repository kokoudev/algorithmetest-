# ---- MULTIPLICATION DE DEUX GRANDS NOMBRES (KARATSUBA) ----

def karatsuba(a, b):
    """
    Algorithme de multiplication de Karatsuba
    Complexité temporelle : O(n^1.585)
    """
    # Cas de base pour les chiffres uniques
    if a < 10 or b < 10:
        return a * b
        
    # Calculer la taille des nombres
    m = max(len(str(a)), len(str(b))) // 2
    
    # Séparer les nombres en parties haute et basse
    high_a, low_a = divmod(a, 10**m)
    high_b, low_b = divmod(b, 10**m)
    
    # 3 multiplications de Karatsuba
    z0 = karatsuba(low_a, low_b)
    z2 = karatsuba(high_a, high_b)
    z1 = karatsuba(low_a + high_a, low_b + high_b)
    
    # Combinaison des résultats
    return z2 * 10**(2*m) + (z1 - z2 - z0) * 10**m + z0

if __name__ == '__main__':
    print("karasuba solo - Multiplication de deux grands nombres")
    try:
        a = int(input("entrer un premier nombre : "))
        b = int(input("entrer un second nombre : "))
        R = karatsuba(a, b)
        print("le resultat de la multiplication est : ", R)
    except ValueError:
        print("Veuillez entrer des nombres entiers valides.")