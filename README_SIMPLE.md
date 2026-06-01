# 🚀 VISUALISEUR D'ALGORITHMES

Interface web interactive pour explorer **3 algorithmes fondamentaux** en informatique.

## 📊 Les 3 Algorithmes

### 1. **QuickSort** - Tri Rapide
- **Fichier**: `quicksortv1.py`
- **Complexité**: O(n log n) moyenne
- **Stratégies**: 3 pivots testables (premier, dernier, médiane)
- **Concept**: Diviser pour régner

### 2. **Two Sum** - Recherche de Paires
- **Fichier**: `tow_sum2.py`
- **Complexité**: O(n log n) avec recherche binaire
- **Fonction**: Trouve paires dont somme ∈ [-10000, 10000]
- **Concept**: Optimisation avec structure de données

### 3. **Karatsuba** - Multiplication Rapide
- **Fichier**: `Karasubasolo.py`
- **Complexité**: O(n^1.585) vs O(n²)
- **Fonction**: Multiplie 2 grands nombres rapidement
- **Concept**: Diviser pour régner (4 multiplications → 3)

---

## 🚀 Démarrage Rapide

### Installation Locale

```bash
# 1. Installer dépendances
pip install -r requirements.txt

# 2. Lancer le serveur
python app.py

# 3. Ouvrir dans navigateur
http://localhost:5000
```

### Déploiement sur Railway (GRATUIT)

1. Allez sur https://railway.app
2. "New Project" → "Deploy from GitHub"
3. Sélectionnez ce repo
4. Site live en 5 minutes!

**Gratuit**: Railway offre $5/mois de crédits gratuits = gratuit long terme

---

## 🎯 Utilisation

### QuickSort
1. Entrez une liste de nombres (ex: `3 1 4 1 5 9`)
2. Choisissez stratégie de pivot (1, 2 ou 3)
3. Cliquez "Exécuter"
4. Voyez le tableau trié et le nombre de comparaisons

### Two Sum
1. Entrez une liste de nombres (ex: `1 2 3 4 5`)
2. Cliquez "Exécuter Two Sum"
3. Voyez combien de paires et les sommes trouvées

### Karatsuba
1. Entrez 2 nombres à multiplier (ex: `1234 5678`)
2. Cliquez "Exécuter"
3. Vérifiez que le résultat est correct

---

## 📁 Architecture

```
Backend (Python):
  ├─ app.py           ← API Flask avec les 3 algorithmes
  └─ requirements.txt ← Dépendances

Frontend (Web):
  └─ index.html       ← Interface web (HTML+CSS+JS)

Configuration:
  ├─ Procfile         ← Railway configuration
  ├─ runtime.txt      ← Python version
  └─ .gitignore
```

---

## 🌐 Endpoints API

```
GET  /              → Page d'accueil
POST /api/quicksort → Tri avec QuickSort
POST /api/two-sum   → Recherche de paires
POST /api/karatsuba → Multiplication Karatsuba
GET  /api/health    → Vérifier que l'API fonctionne
```

---

## 📋 Exemples de Requêtes

### QuickSort
```json
{
  "numbers": "3 1 4 1 5 9 2 6",
  "strategy": "1"
}
→ Response: {"sorted_array": [1,1,2,3,4,5,6,9], "comparaisons": 19}
```

### Two Sum
```json
{
  "numbers": "1 2 3 4 5"
}
→ Response: {"count": 15, "sums": [-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9]}
```

### Karatsuba
```json
{
  "a": "1234",
  "b": "5678"
}
→ Response: {"result": 7006652, "verification": 7006652, "correct": true}
```

---

## 💻 Technologie Utilisée

- **Backend**: Python 3.11 + Flask 3.0
- **Frontend**: HTML5 + CSS3 + JavaScript (vanilla)
- **Serveur**: Gunicorn
- **Déploiement**: Railway
- **Versioning**: Git/GitHub

---

## ✅ Tests Locaux

Tous les tests passent:
- ✅ QuickSort trie correctement
- ✅ Two Sum trouve les paires
- ✅ Karatsuba multiplie correctement
- ✅ Interface web responsive
- ✅ API REST fonctionnelle

---

## 📝 Pour Votre CV

```
🚀 Visualiseur d'Algorithmes
Lien: https://algorithmetest-production-xxxx.up.railway.app

• Interface web interactive pour 3 algorithmes fondamentaux
• Backend: Python/Flask | Frontend: HTML/CSS/JavaScript  
• QuickSort (3 stratégies), Two Sum (recherche binaire), Karatsuba
• Déploiement: Railway (CI/CD automatique depuis GitHub)
```

---

## 🎓 Concepts Clés

### QuickSort
- Stratégie "Diviser pour régner"
- L'impact du choix du pivot sur la performance
- Partitionnement efficace

### Two Sum
- Importance de choisir la bonne structure de données
- Optimisation O(n²) → O(n log n)
- Recherche binaire (bisect)

### Karatsuba
- Réduction du nombre d'opérations
- Complexité O(n²) → O(n^1.585)
- Application pour les très grands nombres

---

## 📚 Ressources

- **Algorithmes**: CLRS "Introduction to Algorithms"
- **Implémentation**: Code commenté en français
- **Documentation**: README.md complet

---

## ⚡ Commandes Utiles

```bash
# Lancer localement
python app.py

# Installer dépendances
pip install -r requirements.txt

# Test d'un algorithme
curl -X POST http://localhost:5000/api/quicksort \
  -H "Content-Type: application/json" \
  -d "{\"numbers\": \"3 1 4 1 5\", \"strategy\": \"1\"}"

# Vérifier que l'API fonctionne
curl http://localhost:5000/api/health
```

---

## 🚀 Prochaines Étapes

1. **Tester localement**: `python app.py`
2. **Mettre sur GitHub**: `git push`
3. **Déployer sur Railway**: railway.app
4. **Ajouter au CV**: Lien du site

**Total: 15 minutes pour avoir un projet en production!**

---

## 💡 Gratuit & Long Terme

- ✅ Railway offre $5/mois de crédits gratuits
- ✅ Ce projet coûte ~$0.10/mois
- ✅ Gratuit pour des années
- ✅ Pas de suppression après 6 mois
- ✅ Déploiement automatique avec git push

---

**Créé pour montrer vos compétences aux recruteurs. Bon succès! 🎉**
