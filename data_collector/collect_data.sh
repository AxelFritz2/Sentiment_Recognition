#!/bin/bash

# Activer l'environnement virtuel
source ./venv/bin/activate

# Exécuter le serveur Flask
python3 ./data_collector/collect.py

mkdir "data"
chmod 777 data

mv face-expression-recognition-dataset data
