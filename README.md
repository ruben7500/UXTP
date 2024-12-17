
# Product Catalog - Flask, SQLite, TailwindCSS

Ce projet permet d'afficher des produits fictifs sous forme de cartes avec une **API REST** créée en Flask et une interface moderne utilisant **TailwindCSS**. Les produits sont générés automatiquement avec **Faker**.

---

## **Prérequis**
- Python 3.x
- Navigateurs récents (Chrome, Firefox)

---

## **Installation**

1. **Cloner le projet**  
   Placez-vous dans le répertoire racine du projet.

2. **Installer les dépendances**  
   Depuis le dossier `src/core`, exécutez :  
   ```bash
   pip install -r requirements.txt
   ```

3. **Générer la base de données avec Faker**  
   Exécutez le script suivant pour créer et remplir la base de données SQLite :  
   ```bash
   python faker_data.py
   ```

4. **Lancer le serveur Flask (backend)**  
   Démarrez le serveur Flask pour l'API REST :  
   ```bash
   python app.py
   ```
   Le serveur sera accessible à l'adresse **http://127.0.0.1:5000/api/products**.

5. **Lancer le serveur local pour le frontend**  
   Depuis le dossier `src`, servez les fichiers HTML :  
   ```bash
   python -m http.server 8000
   ```
   Accédez au frontend à l'adresse **http://localhost:8000**.

---

## **Fonctionnalités**
- **API REST** : Fournit des données de produits avec pagination.
- **Infinite Scroll** : Les produits se chargent automatiquement lors du défilement.
- **Base de données SQLite** : Stocke les produits générés via Faker.
- **Responsive Design** : L'interface est adaptée pour les mobiles et tablettes grâce à TailwindCSS.

---

## **Technologies Utilisées**
- **Backend** : Flask, SQLite, Faker
- **Frontend** : HTML, TailwindCSS, JavaScript
- **Serveur Local** : Python HTTP Server

---

## **Commandes Récapitulatives**
```bash
# Installer les dépendances
pip install -r requirements.txt

# Générer la base de données
python faker_data.py

# Lancer le backend Flask
python app.py

# Servir le frontend
cd src
python -m http.server 8000
```

---

Profitez bien du projet ! 🚀
