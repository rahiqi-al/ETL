
# ETL Project

## Aperçu du Projet
Ce projet met en œuvre un pipeline ETL (Extract, Transform, Load) pour traiter les données de manière efficace et fiable. 
Le pipeline extrait les données de différentes sources, applique les transformations nécessaires, puis charge les données 
traitées dans une base de données PostgreSQL. Les principaux objectifs de ce projet incluent la garantie de la cohérence des données, 
l'optimisation des requêtes, et la création d'une base solide pour l'analyse.

## Fonctionnalités
- **Extraction des Données** : Scripts automatisés pour extraire les données de sources structurées et semi-structurées.
- **Transformation des Données** : Nettoyage, normalisation et mise en forme des données pour répondre aux exigences du schéma de la base de données.
- **Chargement des Données** : Chargement efficace des données transformées dans une base PostgreSQL.
- **Gestion des Erreurs** : Intégration de mécanismes de gestion des erreurs pour garantir la robustesse.

## Prérequis
Avant de commencer, assurez-vous d'avoir :
- **Python** : Version 3.8 ou supérieure.
- **PostgreSQL** : Avec les tables nécessaires configurées.
- **Bibliothèques Python** : Les bibliothèques nécessaires sont listées dans le fichier `requirements.txt`.

## Installation

1. **Clonez le dépôt** :

   ```bash
   git clone https://github.com/rahiqi-al/project_etl.git
   ```

2. **Accédez au répertoire du projet** :

   ```bash
   cd project_etl
   ```

3. **Installez les dépendances** :

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurez les variables d'environnement** :

   Créez un fichier `.env` et ajoutez vos informations de connexion à PostgreSQL

5. **Exécutez le pipeline ETL** :

   ```bash
   python elt_pipeline.py
   ```

## Configurations
Le fichier `config.yml` contient les configurations suivantes :
- Localisations des sources de données.
- Règles de transformation.
- Paramètres de connexion à la base de données.

## Auteur
Ali Rahiqi
