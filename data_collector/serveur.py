import subprocess
from flask import Flask, jsonify
import os

os.environ["KAGGLE_CONFIG_DIR"] = "./data_collector/kaggle.json"

app = Flask(__name__)

@app.route('/download_data', methods=['GET'])
def download_data():
    try:
        subprocess.run(['kaggle', 'datasets', 'download', '-d', 'jonathanoheix/face-expression-recognition-dataset'])

        return jsonify({'message': 'Téléchargement réussi'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False, port = 8001)
