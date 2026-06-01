# 🐙 Configuration GitHub

## Vous avez déjà le repo ?

Votre repo GitHub existe déjà à : https://github.com/kokoudev/algorithmetest-.git

Parfait ! Suivez ces étapes pour mettre à jour avec votre code.

---

## **ÉTAPE 1 : Cloner votre repo (première fois)**

```bash
git clone https://github.com/kokoudev/algorithmetest-.git
cd algorithmetest-
```

---

## **ÉTAPE 2 : Ajouter tous les fichiers**

```bash
git add .
```

---

## **ÉTAPE 3 : Faire votre premier commit**

```bash
git commit -m "Initial commit: Visualiseur d'Algorithmes avec QuickSort, Two Sum, Karatsuba"
```

---

## **ÉTAPE 4 : Pousser vers GitHub**

```bash
git push origin main
```

Ou si la branche s'appelle `master` :
```bash
git push origin master
```

---

## ✅ Vérifier que c'est sur GitHub

1. Allez sur https://github.com/kokoudev/algorithmetest-
2. Vous devez voir tous vos fichiers
3. README.md doit être visible

---

## 📝 Que voir sur GitHub

Vous devriez avoir dans votre repo:

```
✅ app.py
✅ index.html
✅ requirements.txt
✅ Procfile
✅ runtime.txt
✅ .gitignore
✅ README.md
✅ DEPLOYMENT.md
✅ ALGORITHMS.md
✅ GUIDE_CV_LINKEDIN.md
✅ etc.
```

Si tous ces fichiers apparaissent → ✅ GitHub OK !

---

## 🚀 Ensuite : Déployer sur Railway

Une fois que c'est sur GitHub, allez sur https://railway.app et déployez !

Railway va automatiquement :
1. Cloner votre repo
2. Installer requirements.txt
3. Lancer avec gunicorn (selon Procfile)
4. Vous donner une URL

---

## 📚 Branche par défaut

Si vous avez un message "There isn't a main branch":

```bash
# Renommer master en main
git branch -M main
git push -u origin main
```

---

## ✅ Problèmes courants

### "fatal: not a git repository"
```bash
git init
git remote add origin https://github.com/kokoudev/algorithmetest-.git
```

### "Permission denied (publickey)"
Configurez votre SSH ou utilisez HTTPS avec token personnel

### "rejected non-fast-forward"
```bash
git pull origin main --rebase
git push origin main
```

---

## 🎉 Une fois sur GitHub

Vous pouvez :
1. Partager le lien https://github.com/kokoudev/algorithmetest-
2. Ajouter une description dans les "About"
3. Pingler le repo
4. Partager sur LinkedIn
5. L'ajouter au CV

---

**Vous êtes prêt ! 🚀**
