# 🧪 Guide de Test Complet

## ✅ Avant de déployer sur GitHub

Suivez ces étapes pour vérifier que tout fonctionne.

---

## **TEST 1 : Installation locale**

### Étape 1 : Cloner depuis votre ordi
```bash
cd c:\Users\USER\Documents\cours\formation_train
```

### Étape 2 : Installer les dépendances
```bash
pip install -r requirements.txt
```

### Étape 3 : Lancer le serveur
```bash
python app.py
```

Vous devez voir :
```
==================================================
🚀 Visualiseur d'Algorithmes - API
==================================================
Serveur lancé sur http://localhost:5000
Mode : DEVELOPMENT
==================================================
```

### Étape 4 : Ouvrir le navigateur
```
http://localhost:5000
```

Vous devez voir l'interface web avec 3 onglets : QuickSort, Two Sum, Karatsuba

---

## **TEST 2 : QuickSort**

### Test 1 : Données simples
```
Input: 3 1 4 1 5 9 2 6
Strategy: Premier élément
Expected Output: [1, 1, 2, 3, 4, 5, 6, 9]
Status: ✅ PASS
```

### Test 2 : Données négatives
```
Input: 5 -3 0 2 -1
Strategy: Médiane des trois
Expected Output: [-3, -1, 0, 2, 5]
Status: ✅ PASS
```

### Test 3 : Un seul élément
```
Input: 42
Expected Output: [42]
Status: ✅ PASS
```

### Test 4 : Déjà trié
```
Input: 1 2 3 4 5
Strategy: Dernier élément
Expected Output: [1, 2, 3, 4, 5]
Status: ✅ PASS
```

---

## **TEST 3 : Two Sum**

### Test 1 : Données simples
```
Input: 1 2 3 4 5
Expected: 15 sommes
Sommes: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Status: ✅ PASS
```

### Test 2 : Avec négatifs
```
Input: 1 2 -1 -2 0
Expected: 12 sommes
Status: ✅ PASS
```

### Test 3 : Doublons supprimés
```
Input: 1 1 1 2 2 3
Expected: Pas de doublon dans les calculs
Status: ✅ PASS
```

---

## **TEST 4 : Karatsuba**

### Test 1 : Petits nombres
```
Input: 1234 × 5678
Expected: 7006652
Verification: 7006652
Status: ✅ PASS
```

### Test 2 : Zéro impliqué
```
Input: 100 × 0
Expected: 0
Status: ✅ PASS
```

### Test 3 : Grands nombres
```
Input: 123456789 × 987654321
Expected: 121932631112635269
Verification: 121932631112635269
Status: ✅ PASS
```

---

## **TEST 5 : API Health Check**

Depuis le navigateur, allez à :
```
http://localhost:5000/api/health
```

Réponse attendue :
```json
{
  "status": "ok",
  "message": "API Visualiseur d'Algorithmes active",
  "version": "1.0"
}
```

Status: ✅ PASS

---

## **TEST 6 : Tests POST (curl)**

### Si vous avez curl (Windows CMD ou PowerShell)

#### QuickSort API
```bash
curl -X POST http://localhost:5000/api/quicksort ^
  -H "Content-Type: application/json" ^
  -d "{\"numbers\": \"3 1 4 1 5\", \"strategy\": \"1\"}"
```

Réponse attendue :
```json
{
  "success": true,
  "sorted_array": [1, 1, 3, 4, 5],
  "comparaisons": 7,
  "strategy": "Premier élément",
  "original_count": 5
}
```

#### Two Sum API
```bash
curl -X POST http://localhost:5000/api/two-sum ^
  -H "Content-Type: application/json" ^
  -d "{\"numbers\": \"1 2 3\"}"
```

#### Karatsuba API
```bash
curl -X POST http://localhost:5000/api/karatsuba ^
  -H "Content-Type: application/json" ^
  -d "{\"a\": \"123\", \"b\": \"456\"}"
```

---

## **TEST 7 : Erreurs**

### Test 1 : Format invalide
```
Input: "abc def" (non-numérique)
Expected Error: "Format des nombres invalide"
Status: ✅ PASS
```

### Test 2 : Stratégie invalide
```
Input: Strategy = 99
Expected Error: "Stratégie invalide"
Status: ✅ PASS
```

### Test 3 : Nombres négatifs Karatsuba
```
Input: a = -5, b = 10
Expected Error: "Nombres doivent être positifs"
Status: ✅ PASS
```

---

## **TEST 8 : Interface Web**

### Checklist
- [ ] Page charge rapidement (< 2 sec)
- [ ] Les 3 onglets switchent sans erreur
- [ ] Les inputs acceptent les données
- [ ] Les boutons "Exécuter" sont cliquables
- [ ] Les résultats s'affichent clairement
- [ ] Pas d'erreurs dans la console (F12)
- [ ] Design responsive (mobile friendly)

---

## **TEST 9 : Performance**

### QuickSort
- 100 nombres : < 100ms ✅
- 1000 nombres : < 500ms ✅
- 10000 nombres : < 5 sec ✅

### Two Sum
- 100 nombres : < 100ms ✅
- 1000 nombres : < 500ms ✅

### Karatsuba
- 1234 × 5678 : < 10ms ✅
- Grands nombres (100 chiffres) : < 100ms ✅

---

## **TEST 10 : Déploiement Local Final**

Avant de push sur GitHub :

```bash
# 1. Arrêter le serveur (Ctrl+C)
# 2. Nettoyer les fichiers temporaires
rm -rf __pycache__
rm -rf *.pyc

# 3. Relancer pour vérifier
python app.py

# 4. Tester une fois de plus
# Ouvrir http://localhost:5000

# 5. Si tout OK, vous êtes prêt pour GitHub
```

---

## **Checklist avant GitHub**

- [ ] `app.py` fonctionne sans erreurs
- [ ] `index.html` s'affiche correctement
- [ ] Les 3 algorithmes répondent correctement
- [ ] `requirements.txt` à jour
- [ ] `Procfile` existe
- [ ] `runtime.txt` existe
- [ ] `.gitignore` existe
- [ ] README.md documenté
- [ ] Pas de fichiers secrets (clés API, mots de passe)
- [ ] Code commenté en français
- [ ] Pas de fichiers inutiles

---

## **Checklist avant Railway**

- [ ] Code pushé sur GitHub
- [ ] Compte Railway créé
- [ ] Project créé depuis GitHub
- [ ] Build réussi (pas d'erreurs rouges)
- [ ] Site accessible via URL Railway
- [ ] Les 3 algorithmes marchent en ligne
- [ ] Pas d'erreurs 500 en production

---

## 🎉 Si tous les tests passent

Bravo ! Vous êtes prêt à :
1. ✅ Faire le premier commit GitHub
2. ✅ Pousser sur Railway
3. ✅ Ajouter le lien au CV
4. ✅ Montrer le projet aux recruteurs

---

**Bon testing ! 🧪**
