#!/bin/bash

# Script pour lancer facilement le projet sous Linux/Mac

echo ""
echo "========================================"
echo "  Visualiseur d'Algorithmes"
echo "========================================"
echo ""

# Vérifier que Python est installé
if ! command -v python3 &> /dev/null; then
    echo "[ERREUR] Python 3 n'est pas installé"
    echo "Installez avec : sudo apt-get install python3 python3-pip"
    exit 1
fi

echo "[✓] Python détecté : $(python3 --version)"

# Vérifier que pip est installé
if ! command -v pip3 &> /dev/null; then
    echo "[ERREUR] pip3 n'est pas installé"
    exit 1
fi

echo "[✓] pip3 détecté"

# Installation des dépendances
echo ""
echo "Installation des dépendances..."
pip3 install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "[ERREUR] Impossible d'installer les dépendances"
    exit 1
fi

echo "[✓] Dépendances installées"

# Lancer l'application
echo ""
echo "========================================"
echo "[✓] Lancement du serveur..."
echo "========================================"
echo ""
echo "🚀 Le serveur démarre sur : http://localhost:5000"
echo ""
echo "Appuyez sur Ctrl+C pour arrêter le serveur"
echo ""

python3 app.py
