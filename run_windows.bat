@echo off
REM Script pour lancer facilement le projet sous Windows

echo.
echo ========================================
echo   Visualiseur d'Algorithmes
echo ========================================
echo.

REM Vérifier que Python est installé
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERREUR] Python n'est pas installé ou pas dans le PATH
    echo Téléchargez Python depuis : https://www.python.org/downloads/
    echo Assurez-vous de cocher "Add Python to PATH" lors de l'installation
    pause
    exit /b 1
)

echo [✓] Python détecté

REM Vérifier que pip est installé
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERREUR] pip n'est pas installé
    echo Essayez : python -m pip install --upgrade pip
    pause
    exit /b 1
)

echo [✓] pip détecté

REM Vérifier les dépendances
echo.
echo Installation des dépendances...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERREUR] Impossible d'installer les dépendances
    pause
    exit /b 1
)

echo [✓] Dépendances installées

REM Lancer l'application
echo.
echo ========================================
echo [✓] Lancement du serveur...
echo ========================================
echo.
echo 🚀 Le serveur démarre sur : http://localhost:5000
echo.
echo Appuyez sur Ctrl+C pour arrêter le serveur
echo.

python app.py

pause
