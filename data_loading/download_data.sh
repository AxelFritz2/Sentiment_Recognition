#!/bin/bash

curl http://localhost:8001/download_data && pkill -f serveur.py
