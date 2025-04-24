# Projet Selenium Python Dockerisé
Un projet automatisé de tests Selenium avec Python, entièrement dockerisé pour une exécution simplifiée des tests dans un environnement isolé.




## Prérequis

- Docker : [Télécharger Docker Desktop](https://www.docker.com/products/docker-desktop)
- Docker Compose : Inclus avec Docker Desktop.

## Dépendances

- `selenium==4.27.1`  : Automatisation des tests avec les navigateurs.
- `pytest==8.3.5`  : Framework de tests pour exécuter les scénarios automatisés.
- `pytest-html` : Génération de rapports HTML pour les résultats de tests.
- `webdriver-manager` : Gestion automatique des drivers pour les navigateurs.
- `dotenv` : Gestion des variables d'environnement.

## Structure du projet

  Le projet est organisé de la manière suivante :

/arvea-automation
│
── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── dashboard_page.py
│   ├── login_page.py
│   └── order_page.py
│ 
│ 
│ 
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   └── test_dashboard.py
│
├── reports/ (généré automatiquement)
│   
│
│── utilities/
│   ├── __init__.py
│   └─── config.py  
│
│
├── .env.example
├── requirements.txt
├── Dockerfile
└── docker-compose.yml


## Lancer les tests via Docker

### 1. Construire et démarrer les services

```bash
docker-compose up --build
 

