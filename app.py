"""
VISUALISEUR D'ALGORITHMES - BACKEND API
========================================
API Flask pour exécuter 3 algorithmes fondamentaux
"""

import os
import sys
import bisect
from flask import Flask, render_template, request, jsonify

# Ajouter le dossier algorithms au path pour pouvoir importer
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'algorithms'))

# ==================== CONFIGURATION ====================
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# ==================== ALGORITHME 1 : QUICKSORT ====================
def quicksort_algo(arr, strategy):
    """
    Tri rapide (QuickSort) avec 3 stratégies de pivot différentes
    Complexité : O(n log n) en moyenne
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
        
        if len(arr_inner) <= 1:
            return arr_inner
        
        comparaisons += len(arr_inner) - 1
        
        if strat == 1:
            pivot_index = 0
        elif strat == 2:
            pivot_index = len(arr_inner) - 1
        else:
            pivot_index = mediane(arr_inner)
        
        arr_inner[0], arr_inner[pivot_index] = arr_inner[pivot_index], arr_inner[0]
        p = arr_inner[0]
        
        g = []
        d = []
        
        for x in arr_inner[1:]:
            if x < p:
                g.append(x)
            else:
                d.append(x)
        
        return quicksort_helper(g, strat) + [p] + quicksort_helper(d, strat)
    
    result = quicksort_helper(arr[:], strategy)
    return result, comparaisons

# ==================== ALGORITHME 2 : TWO SUM ====================
def two_sum_algo(numbers):
    """
    Trouve toutes les paires de nombres dont la somme est entre -10000 et 10000
    Complexité : O(n log n) avec recherche binaire
    """
    nums = sorted(list(set(numbers)))
    targets_found = set()
    
    for x in nums:
        low = -10000 - x
        high = 10000 - x
        
        idx_start = bisect.bisect_left(nums, low)
        idx_end = bisect.bisect_right(nums, high)
        
        for i in range(idx_start, idx_end):
            y = nums[i]
            if y != x:
                targets_found.add(x + y)
    
    return len(targets_found), sorted(list(targets_found))

# ==================== ALGORITHME 3 : KARATSUBA ====================
def karatsuba_algo(a, b):
    """
    Multiplication optimisée de deux grands nombres (Karatsuba)
    Complexité : O(n^1.585) vs O(n²)
    """
    if a < 10 or b < 10:
        return a * b
    
    m = max(len(str(a)), len(str(b))) // 2
    
    high_a, low_a = divmod(a, 10**m)
    high_b, low_b = divmod(b, 10**m)
    
    z0 = karatsuba_algo(low_a, low_b)
    z2 = karatsuba_algo(high_a, high_b)
    z1 = karatsuba_algo(low_a + high_a, low_b + high_b)
    
    return z2 * 10**(2*m) + (z1 - z2 - z0) * 10**m + z0

# ==================== ROUTES ====================

@app.route('/')
def index():
    """Servir l'interface HTML"""
    return render_template('index.html')

@app.route('/api/quicksort', methods=['POST'])
def api_quicksort():
    """API QuickSort"""
    try:
        data = request.json
        numbers = list(map(int, data['numbers'].split()))
        strategy = int(data['strategy'])
        
        if strategy not in [1, 2, 3]:
            return jsonify({'success': False, 'error': 'Stratégie invalide'}), 400
        
        result, comparaisons = quicksort_algo(numbers, strategy)
        
        strategy_names = {1: "Premier élément", 2: "Dernier élément", 3: "Médiane des trois"}
        
        return jsonify({
            'success': True,
            'sorted_array': result,
            'comparaisons': comparaisons,
            'strategy': strategy_names[strategy],
            'original_count': len(numbers)
        })
    except ValueError:
        return jsonify({'success': False, 'error': 'Format des nombres invalide'}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/two-sum', methods=['POST'])
def api_two_sum():
    """API Two Sum"""
    try:
        data = request.json
        numbers = list(map(int, data['numbers'].split()))
        
        count, sums = two_sum_algo(numbers)
        
        return jsonify({
            'success': True,
            'count': count,
            'sums': sums[:100],  # Limiter les 100 premières sommes distinctes
            'total_sums': len(sums),
            'input_count': len(numbers)
        })
    except ValueError:
        return jsonify({'success': False, 'error': 'Format des nombres invalide'}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/karatsuba', methods=['POST'])
def api_karatsuba():
    """API Karatsuba"""
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

@app.route('/api/health', methods=['GET'])
def health():
    """Health check"""
    return jsonify({
        'status': 'ok',
        'message': 'API Visualiseur d\'Algorithmes active',
        'version': '1.0'
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({'success': False, 'error': 'Route non trouvée'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'success': False, 'error': 'Erreur interne du serveur'}), 500

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
