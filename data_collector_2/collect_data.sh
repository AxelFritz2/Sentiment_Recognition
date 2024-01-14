#!/bin/bash

# Activer l'environnement virtuel
source ./venv/bin/activate

# Exécuter le serveur Flask
python3 ./data_collector_2/collect.py

mkdir "./data"
mv './data_collector_2/face-expression-recognition-dataset' './data'