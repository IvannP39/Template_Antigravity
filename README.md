# Template Antigravity 🤖

Ce projet sert de base pour tes futures automatisations avec **Python (Streamlit)** et **n8n**. Il inclut une interface de connexion sécurisée et une structure modulaire.

## 🚀 Démarrage Rapide

### 1. Configuration de l'environnement
Assure-toi d'avoir Python 3.10+ installé.

```powershell
# Créer l'environnement virtuel (si pas déjà fait)
python -m venv myenv

# Activer l'environnement
.\myenv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt
```

### 2. Configuration des variables d'environnement (`.env`)
Renomme le fichier `.env.template` en `.env` et modifie les valeurs :
- `N8N_WEBHOOK_URL` : L'URL de ton webhook n8n.
- `APP_USERNAME` / `APP_PASSWORD` : Tes identifiants pour l'interface.

### 3. Lancer l'application
```powershell
streamlit run app/src/main.py
```

## 🛠️ Structure du Projet
- `app/src/main.py` : L'interface utilisateur (UI) avec Streamlit. Cherche les `TODO` pour personnaliser l'affichage.
- `app/src/logic.py` : La logique d'automatisation (appels API, fonctions métier).
- `.env` : Configuration sensible.

## 📝 À faire (TODO)
Partout dans le code, tu trouveras des commentaires `# TODO` qui t'indiquent les endroits clés à modifier pour tes nouveaux projets.
