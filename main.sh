echo "******************* Initialisation de l'application *******************"
source ./venv/bin/activate

echo "******************* Wine *******************"
bash ./test_wine/wine.sh
echo "******************* Wined *******************"


echo "******************* Collecte des données *******************"
bash ./data_collector/collect_data.sh
echo "******************* Données collectées *******************"


echo "******************* Entraînement du modèle *******************"
bash ./data_processor/train_model.sh
echo "******************* Modèle entraîné *******************"


echo "******************* Lancement de l'application *******************"
source ./venv/bin/activate
python -m streamlit run ./application/app.py --server.port 8501