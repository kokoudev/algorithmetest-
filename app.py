"""
VISUALISEUR D'ALGORITHMES - BACKEND API
========================================
API Flask pour exécuter 3 algorithmes fondamentaux

Endpoints disponibles:
- GET  / : Servir l'interface HTML
- POST /api/quicksort : Exécuter QuickSort
- POST /api/two-sum : Exécuter Two Sum
- POST /api/karatsuba : Exécuter Karatsuba
"""

import os
import bisect
from flask import Flask, request, jsonify

# ==================== CONFIGURATION ====================
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# ==================== ALGORITHME 1 : QUICKSORT ====================
def quicksort_algo(arr, strategy):
    """
    Tri rapide (QuickSort) avec 3 stratégies de pivot différentes
    Complexité : O(n log n) en moyenne
    
    Args:
        arr (list): Tableau à trier
        strategy (int): 1=premier, 2=dernier, 3=médiane
    
    Returns:
        tuple: (tableau trié, nombre de comparaisons)
    """
    comparaisons = 0
    
    def mediane(arr_inner):
        """Trouve la médiane entre premier, milieu et dernier élément"""
        n = len(arr_inner)
        first_val = arr_inner[0]
        mid_index = (n - 1) // 2
        mid_val = arr_inner[mid_index]
        last_val = arr_inner[n - 1]
        
        if (first_val <= mid_val <= last_val) or (last_val <= mid_val <= first_val):
            return mid_index
        elif (mid_val <= first_val <= last_val) or (last_val <= first_val <= mid_val):
            return 0
        else:
            return n - 1
    
    def quicksort_helper(arr_inner, strat):
        nonlocal comparaisons
        
        # Cas de base : tableau de 0 ou 1 élément
        if len(arr_inner) <= 1:
            return arr_inner
        
        # Compter les comparaisons : m-1 pour m éléments
        comparaisons += len(arr_inner) - 1
        
        # Choisir le pivot selon la stratégie
        if strat == 1:
            pivot_index = 0  # Premier élément
        elif strat == 2:
            pivot_index = len(arr_inner) - 1  # Dernier élément
        else:
            pivot_index = mediane(arr_inner)  # Médiane des trois
        
        # Placer le pivot en première position
        arr_inner[0], arr_inner[pivot_index] = arr_inner[pivot_index], arr_inner[0]
        p = arr_inner[0]
        
        # Partitionner le tableau
        g = []  # Gauche (< pivot)
        d = []  # Droite (>= pivot)
        
        for x in arr_inner[1:]:
            if x < p:
                g.append(x)
            else:
                d.append(x)
        
        # Récursion et combinaison
        return quicksort_helper(g, strat) + [p] + quicksort_helper(d, strat)
    
    result = quicksort_helper(arr[:], strategy)
    return result, comparaisons

# ==================== ALGORITHME 2 : TWO SUM ====================
def two_sum_algo(numbers):
    """
    Trouve toutes les paires de nombres dont la somme est entre -10000 et 10000
    Complexité : O(n log n) avec recherche binaire
    
    Args:
        numbers (list): Tableau de nombres
    
    Returns:
        tuple: (nombre de sommes distinctes, liste des sommes)
    """
    nums = sorted(list(set(numbers)))
    targets_found = set()
    
    # Parcourir chaque nombre
    for x in nums:
        # Intervalle de y tels que -10000 <= x + y <= 10000
        low = -10000 - x
        high = 10000 - x
        
        # Recherche binaire pour trouver l'intervalle
        idx_start = bisect.bisect_left(nums, low)
        idx_end = bisect.bisect_right(nums, high)
        
        # Ajouter toutes les sommes valides
        for i in range(idx_start, idx_end):
            y = nums[i]
            if y != x:  # Éviter x + x avec le même nombre
                targets_found.add(x + y)
    
    return len(targets_found), sorted(list(targets_found))

# ==================== ALGORITHME 3 : KARATSUBA ====================
def karatsuba_algo(a, b):
    """
    Multiplication optimisée de deux grands nombres
    Complexité : O(n^1.585) vs O(n²) pour multiplication naïve
    
    Utilise "Diviser pour régner" : réduit 4 multiplications à 3
    
    Args:
        a (int): Premier nombre
        b (int): Second nombre
    
    Returns:
        int: Résultat de la multiplication
    """
    # Compter les chiffres du premier nombre
    S1 = a
    C1 = 0
    while S1 != 0:
        S1 = S1 // 10
        C1 = C1 + 1
    
    # Compter les chiffres du second nombre
    S2 = b
    C2 = 0
    while S2 != 0:
        S2 = S2 // 10
        C2 = C2 + 1
    
    # Diviser en deux parties
    mc1 = C1 // 2
    mc2 = C2 // 2
    
    D1 = 10 ** mc1
    D2 = 10 ** mc2
    
    # Décomposition : a = A * 10^mc1 + B, b = C * 10^mc2 + D
    A = a // D1
    B = a % D1
    C = b // D2
    D = b % D2
    
    # Trois multiplications au lieu de quatre
    E1 = A * C           # Partie haute × haute
    E2 = B * D           # Partie basse × basse
    E3 = (A + B) * (C + D)  # Sommes × sommes
    E4 = E3 - E1 - E2    # Produit croisé
    
    # Combinaison finale
    R = E1 * 10 ** (2 * mc1) + E4 * 10 ** mc1 + E2
    
    return R

# ==================== ROUTES API ====================

@app.route('/')
def index():
    """Servir l'interface HTML"""
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Erreur : index.html non trouvé", 404

@app.route('/api/quicksort', methods=['POST'])
def api_quicksort():
    """API : Exécuter QuickSort"""
    try:
        data = request.json
        numbers = list(map(int, data['numbers'].split()))
        strategy = int(data['strategy'])
        
        if strategy not in [1, 2, 3]:
            return jsonify({'success': False, 'error': 'Stratégie invalide (1, 2 ou 3)'}), 400
        
        result, comparaisons = quicksort_algo(numbers, strategy)
        
        strategy_names = {
            1: "Premier élément",
            2: "Dernier élément",
            3: "Médiane des trois"
        }
        
        return jsonify({
            'success': True,
            'sorted_array': result,
            'comparaisons': comparaisons,
            'strategy': strategy_names[strategy],
            'original_count': len(numbers)
        })
    except ValueError as e:
        return jsonify({'success': False, 'error': 'Format des nombres invalide'}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/two-sum', methods=['POST'])
def api_two_sum():
    """API : Exécuter Two Sum"""
    try:
        data = request.json
        numbers = list(map(int, data['numbers'].split()))
        
        count, sums = two_sum_algo(numbers)
        
        return jsonify({
            'success': True,
            'count': count,
            'sums': sums[:100],  # Limiter à 100 pour la réponse
            'total_sums': len(sums),
            'input_count': len(numbers)
        })
    except ValueError:
        return jsonify({'success': False, 'error': 'Format des nombres invalide'}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/karatsuba', methods=['POST'])
def api_karatsuba():
    """API : Exécuter Karatsuba"""
    try:
        data = request.json
        a = int(data['a'])
        b = int(data['b'])
        
        if a < 0 or b < 0:
            return jsonify({'success': False, 'error': 'Nombres doivent être positifs'}), 400
        
        result = karatsuba_algo(a, b)
        verification = a * b
        
        return jsonify({
            'success': True,
            'result': result,
            'verification': verification,
            'correct': result == verification,
            'a': a,
            'b': b
        })
    except ValueError:
        return jsonify({'success': False, 'error': 'Format des nombres invalide'}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

# ==================== HEALTH CHECK ====================

@app.route('/api/health', methods=['GET'])
def health():
    """Vérifier que l'API fonctionne"""
    return jsonify({
        'status': 'ok',
        'message': 'API Visualiseur d\'Algorithmes active',
        'version': '1.0'
    })

# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    return jsonify({'success': False, 'error': 'Route non trouvée'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'success': False, 'error': 'Erreur serveur'}), 500

# ==================== MAIN ====================

if __name__ == '__main__':
    debug_mode = os.environ.get('ENV', 'development') != 'production'
    port = int(os.environ.get('PORT', 5000))
    
    print("\n" + "="*50)
    print("🚀 Visualiseur d'Algorithmes - API")
    print("="*50)
    print(f"Serveur lancé sur http://localhost:{port}")
    print(f"Mode : {'DEVELOPMENT' if debug_mode else 'PRODUCTION'}")
    print("="*50 + "\n")
    
    app.run(
        debug=debug_mode,
        host='0.0.0.0',
        port=port,
        use_reloader=debug_mode
    )

