#!/bin/bash

VENV_DIR="venv"

if [ -d "$VENV_DIR" ]; then
    echo "L'environnement virtuel existe déjà."
else
    command -v virtualenv >/dev/null 2>&1 || { echo >&2 "virtualenv n'est pas installé. Installation en cours..."; python3 pip install virtualenv; }

    python3 virtualenv $VENV_DIR

    source $VENV_DIR/bin/activate

    python3 pip install -r requirements.txt

    deactivate

    echo "Environnement virtuel créé avec succès."
fi