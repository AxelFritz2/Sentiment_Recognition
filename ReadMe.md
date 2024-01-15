# Sentiment Recognition 👁️

## Introduction

Bienvenue dans Sentiment Recognition, une application de reconnaissance de sentiment. Dans cette application, vous pourrez :

- Détecter les sentiments d'une image à partir des images d'entraînement.
- Uploader votre propre image pour détecter les sentiments à partir de celle-ci.
- Utiliser votre caméra pour une détection en temps réel.


## Comment Exécuter

Pour exécuter l'application, il faut créer un docker à partir du dockerfile. Voici les étapes :


1. Cloner le repository de l'application : 

    ```bash
    git clone https://github.com/AxelFritz2/Sentiment_Recognition.git
    ```

2. Créer l'image Docker :

    ```bash
    Docker build -t application:latest .
    ```

En créant l'image docker, un environnement virtuel va se créer et les dépendances vont se télécharger directement. 
## Utilisation

Pour lancer l'application, il vous suffit de lancer la commande Docker run :

```bash
Docker run application 
```

Cette commande va effectuer les tâches suivantes : 
- Télecharger les données d'entraînement depuis Kaggle (https://www.kaggle.com/datasets/jonathanoheix/face-expression-recognition-dataset)
- Entraîner le modèle de computer vision. 
- Lancer l'application streamlit

Vous pourrez ainsi lancer l'application via l'url fourni.

## Remarques

- La fonctionnalité de détection de sentiment peut ne pas fonctionner. Cette dernière est encore en cours développement. 
- 