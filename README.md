# 🚀 Visualiseur d'Algorithmes - Projet Éducatif

Bienvenue dans ce projet de visualisation interactive de **3 algorithmes fondamentaux** en informatique ! Ce projet combine Python (backend) avec une interface web moderne (HTML/CSS/JavaScript).

## 📚 Les 3 Algorithmes

### 1. **QuickSort** 🔄
- **Fichier** : `quicksortv1.py`
- **Type** : Algorithme de tri
- **Complexité** : O(n log n) en moyenne, O(n²) pire cas
- **Stratégies testables** :
  - 🎯 Pivot = Premier élément
  - 🎯 Pivot = Dernier élément
  - 🎯 Pivot = Médiane des trois
- **Description** : Algorithme "Diviser pour régner" qui partitionne le tableau autour d'un pivot, puis trie récursivement les sous-tableaux.

### 2. **Two Sum** 🎯
- **Fichier** : `tow_sum2.py`
- **Type** : Problème d'optimisation
- **Complexité** : O(n log n) avec recherche binaire
- **Description** : Trouve toutes les paires de nombres distincts dont la somme est entre -10000 et 10000. Utilise la recherche binaire (`bisect`) pour une performance optimale.
- **Exemple** : Pour [1, 2, 3], trouve les sommes : {3, 4, 5}

### 3. **Karatsuba** ✖️
- **Fichier** : `Karasubasolo.py`
- **Type** : Multiplication optimisée
- **Complexité** : O(n^1.585) vs O(n²) pour multiplication naïve
- **Description** : Algorithme "Diviser pour régner" pour multiplier rapidement deux grands nombres. Réduit le nombre de multiplications de 4 à 3.
- **Exemple** : 1234 × 5678 = 7,006,652

---

## 🛠️ Installation et Configuration

### Prérequis
- Python 3.8+
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner le projet** :
   ```bash
   git clone https://github.com/kokoudev/algorithmetest-.git
   cd algorithmetest-
   ```

2. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

3. **Lancer l'application** :
   ```bash
   python app.py
   ```

4. **Ouvrir dans le navigateur** :
   - Allez à `http://localhost:5000`
   - L'interface web s'ouvrira automatiquement

---

## 💻 Utilisation de l'Interface Web

### QuickSort
1. Entrez une liste de nombres (ex: `3 1 4 1 5 9`)
2. Choisissez une stratégie de pivot (1, 2, ou 3)
3. Cliquez "Exécuter QuickSort"
4. Voyez le tableau trié et le nombre de comparaisons

### Two Sum
1. Entrez une liste de nombres (ex: `1 2 3 4 5`)
2. Cliquez "Exécuter Two Sum"
3. Voyez le nombre de sommes distinctes et la liste des sommes trouvées

### Karatsuba
1. Entrez deux nombres à multiplier
2. Cliquez "Exécuter Karatsuba"
3. Comparez le résultat Karatsuba avec la vérification standard

---

## 🌐 Déploiement Gratuit à Long Terme

### Option 1 : **Railway** (Recommandé) ⭐
- **Avantages** : Interface simple, $5/mois crédits gratuits, très stable
- **Durée gratuite** : Illimitée avec crédits
- **Étapes** :
  1. Créez un compte sur [railway.app](https://railway.app)
  2. Connectez votre GitHub
  3. Créez un nouveau projet → "Deploy from GitHub"
  4. Sélectionnez `algorithmetest-`
  5. Railway détecte `requirements.txt` et configure automatiquement
  6. Cliquez "Deploy"
  7. Votre site sera accessible à `https://votre-projet.railway.app`

### Option 2 : **Render**
- **Avantages** : Gratuit, bon support Python
- **Durée gratuite** : Illimitée (avec sleep après 15 min inactivité)
- **Étapes** :
  1. Allez sur [render.com](https://render.com)
  2. New + Web Service
  3. Connectez votre GitHub
  4. Sélectionnez `algorithmetest-`
  5. Configurez :
     - Name: `algorithmetest`
     - Runtime: `python-3`
     - Build command: `pip install -r requirements.txt`
     - Start command: `gunicorn app:app`
  6. Cliquez "Create Web Service"

### Option 3 : **Vercel** (Frontend uniquement)
- Meilleur pour HTML/CSS/JS pur, mais Flask nécessite un backend différent

---



### Dans un portefeuille/GitHub
Ajoutez dans votre `README` principal :

```markdown
## 📚 Projets

### [Visualiseur d'Algorithmes](https://votre-projet.railway.app)
Interface web interactive pour explorer 3 algorithmes :
- **QuickSort** : Tri rapide avec 3 stratégies de pivot
- **Two Sum** : Recherche de paires avec optimisation binaire
- **Karatsuba** : Multiplication rapide de grands nombres

[Code sur GitHub](https://github.com/kokoudev/algorithmetest-)
```

---

## 📁 Structure du Projet

```
algorithmetest-/
├── app.py                  # Backend Flask principal
├── requirements.txt        # Dépendances Python
├── index.html             # Interface web (HTML/CSS/JS intégré)
├── quicksortv1.py         # QuickSort avec commentaires
├── tow_sum2.py            # Two Sum avec commentaires
├── Karasubasolo.py        # Karatsuba avec commentaires
├── README.md              # Ce fichier
└── .gitignore             # Fichiers ignorés par Git
```

---

## 🧪 Tester Localement

### Exemple 1 : QuickSort
```
Input: 3 1 4 1 5 9 2 6
Strategy: 1 (Premier élément)
Output: [1, 1, 2, 3, 4, 5, 6, 9]
Comparaisons: 19
```

### Exemple 2 : Two Sum
```
Input: 1 2 3 4 5 -1 -2 0
Output: 16 sommes distinctes
Sommes: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### Exemple 3 : Karatsuba
```
Input: 1234 × 5678
Karatsuba Result: 7,006,652
Standard Verification: 7,006,652
✅ Correct!
```

---

## 🔧 Problèmes Courants

### "Le port 5000 est déjà utilisé"
```bash
# Linux/Mac
lsof -ti:5000 | xargs kill -9

# Windows (PowerShell)
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### "Module flask non trouvé"
```bash
pip install flask==3.0.0
```

### Les fichiers Python ne s'exécutent pas
Vérifiez que `python` est dans votre PATH :
```bash
python --version
```

---

## 🎓 Points Pédagogiques

### Pourquoi ces 3 algorithmes ?

1. **QuickSort** : Fondamental pour comprendre les algorithmes de tri
2. **Two Sum** : Montre l'importance de choisir la bonne structure de données
3. **Karatsuba** : Démontre la puissance du "Diviser pour régner"

### Concepts clés
- **Diviser pour régner** : Décomposer un problème en sous-problèmes
- **Complexité algorithmique** : Analyser la performance O(n)
- **Optimisation** : Réduire le nombre d'opérations
- **Vérification** : Toujours vérifier la correction du résultat

---

## 📞 Support

Si vous avez des questions :
1. Vérifiez les messages d'erreur affichés
2. Consultez les commentaires dans le code Python
3. Testez avec des données simples d'abord
4. Vérifiez que Flask est correctement installé

---

## 📜 Licence

Ce projet est fourni à titre éducatif. Vous êtes libre de l'utiliser, le modifier et le distribuer.

---

## 🚀 Prochaines Étapes

- ✅ Déployer sur Railway/Render
- ✅ Ajouter le lien au CV
- ✅ Partager le projet sur GitHub
- 🔄 Ajouter des algorithmes supplémentaires (Merge Sort, Dijkstra, etc.)
- 🔄 Créer des visualisations graphiques des étapes

---

**Créé avec ❤️ par un développeur passionné d'algorithmique**

Bon codage ! 🎉
