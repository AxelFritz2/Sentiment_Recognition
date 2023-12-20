import zipfile
import os

# Chemins
fichier_zip = "face-expression-recognition-dataset.zip"
destination = "./data/"


with zipfile.ZipFile(fichier_zip, 'r') as zip_ref:
    zip_ref.extractall(destination)

# Supprimer le fichier zip s'il n'est plus nécessaire
os.remove(fichier_zip)

print(f"Le fichier {fichier_zip} a été dézippé avec succès dans le dossier {destination}.")
