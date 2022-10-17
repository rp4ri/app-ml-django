# app-ml-django

- **By:** Rodrigo Pari

- **Contact:** rodrigo.parisusao25201@gmail.com

This is a machine learning project deployed using django

## Licence


This project has not a license file

## Directories Distribution
```
├── README.md
├── main.py
├── backend\server
│   ├── apps
│   │   ├── endpoints
|   |   |   ├── __init__.py
|   |   |   ├── admin.py
|   |   |   ├── apps.py
|   |   |   ├── migrations
|   |   |   |   └── __init__.py
|   |   |   ├── models.py
|   |   |   ├── serializers.py
|   |   |   ├── tests.py
|   |   |   ├── urls.py
|   |   |   └── views.py
│   │   └── ml
|   |   |   ├── __init__.py
|   |   |   ├── income_classifier
|   |   |   |   ├── __init__.py
|   |   |   |   ├── extra_trees.py
|   |   |   |   └── random_forest.py
|   |   |   ├── registry.py
|   |   |   └── tests.py
│   ├── db.sqlite3
│   ├── manage.py
│   ├── server
|   |   ├── __init__.py
|   |   ├── asgi.py
|   |   ├── settings.py
|   |   ├── urls.py
|   |   └── wsgi.py
├── docker-compose.yml
├── docker
│   ├── backend
│   │   ├── Dockerfile
│   │   └── wsgi-entrypoint.sh
│   └── nginx
│       ├── Dockerfile
│       └── default.conf
├── notebooks
│   ├── 1_creando-modelo.ipynb
│   ├── 2_ab-test.ipynb
│   ├── encoders.joblib
│   ├── extra_trees.joblib
│   ├── random_forest.joblib
│   └── train_mode.joblib
└── requirements.txt
```
