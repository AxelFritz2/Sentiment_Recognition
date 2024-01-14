echo "******************* Initialisation de l'application *******************"
source ./venv/bin/activate
echo "******************* Collecte des données *******************"
bash ./data_collector_2/collect_data.sh
echo "******************* Données collectées *******************"

cd data
ls
cd ..

echo "******************* Entraînement du modèle *******************"
bash ./data_processor/train_model.sh
echo "******************* Modèle entraîné *******************"

echo "******************* Lancement de l'application *******************"

source ./venv/bin/activate
python -m streamlit run ./application/app.py