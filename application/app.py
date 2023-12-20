import cv2
from keras.preprocessing.image import load_img, img_to_array
import random
import os
from PIL import Image
import numpy as np
import streamlit as st
from keras.models import load_model

classifier = load_model('..data/model.h5')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def predict(img_path, model):
    class_names = ["Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise"]

    image = load_img(img_path, target_size=(48, 48))
    image = img_to_array(image) / 255
    image = np.expand_dims(image, axis=0)
    predictions = model.predict(image)[0]

    predicted_class_index = np.argmax(predictions)
    predicted_class_name = class_names[predicted_class_index]
    return(predicted_class_name)

def random_img(chosen_class:str):
    class_names = ["Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise"]
    root_dir = ".data/images/validation"

    if chosen_class == 'random' :
        chosen_class = random.choice(class_names)

    class_dir = os.path.join(root_dir, chosen_class.lower())
    image_files = os.listdir(class_dir)
    random.shuffle(image_files)
    img_path = os.path.join(class_dir, image_files[0])

    return img_path, chosen_class

def predict_uploaded_image(img):
    class_names = ["Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise"]

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        img = img[y:y + h, x:x + w]
        img = cv2.resize(img, (48, 48))
        img = img_to_array(img) / 255
        img = np.expand_dims(img, axis=0)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        predictions = classifier.predict(img)[0]
        predicted_class_index = np.argmax(predictions)
        predicted_class_name = class_names[predicted_class_index]

    return(predicted_class_name, (x, y, w, h))

def main():
    st.markdown("<h1 style='text-align: center; font-size: 40px; font-weight: bold;'>Détection de Sentiment</h1>", unsafe_allow_html=True)

    st.sidebar.markdown("<h2 style='font-weight: bold;'>Image d'Entraînement</h2>", unsafe_allow_html=True)
    class_names = ["Random", "Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise"]
    chosen_class = st.sidebar.selectbox("Choisir une Émotion", class_names)

    if st.sidebar.button("Générer"):
        img_path, chosen_class = random_img(chosen_class.lower())
        image = Image.open(img_path)

        col1, col2, col3 = st.columns([1,4,1])
        with col2:
            st.image(image, width=450)

        predicted_class = predict(img_path, classifier)
        st.markdown(f"<h3 style='text-align: center; font-weight: bold;'>Real Class: {chosen_class}</h3>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; font-weight: bold;'>Predicted Class: {predicted_class}</h3>", unsafe_allow_html=True)

    st.sidebar.markdown("<h2 style='font-weight: bold;'>Image Personnelle</h2>", unsafe_allow_html=True)
    uploaded_file = st.sidebar.file_uploader("Importer une image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert('RGB')

        img_array = np.array(image)
        predicted_class, coords = predict_uploaded_image(img_array)
        x,y,w,h = coords

        cv2.rectangle(img_array, (x,y), (x + w, y + h), (0, 0, 255), 4)
        col1, col2, col3 = st.columns([1, 4, 1])
        with col2:
            st.image(img_array, width=450)

        st.markdown(f"<h3 style='text-align: center; font-weight: bold;'>Predicted Class: {predicted_class}</h3>",
                    unsafe_allow_html=True)

    st.sidebar.markdown("<h2 style='font-weight: bold;'>En direct</h2>", unsafe_allow_html=True)
    if st.sidebar.button("Démarrer la caméra"):
        classes = ["Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise"]
        cap = cv2.VideoCapture(0)
        frame_placeholder = st.empty()
        stop_button_pressed = st.button("Stop")
        while cap.isOpened() and not stop_button_pressed:
            ret, frame = cap.read()
            if not ret:
                st.write("Video Capture Ended")
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                # Extraire la région du visage pour la prédiction
                face = frame[y:y + h, x:x + w]
                face = cv2.resize(face, (48, 48))
                face = face[..., ::-1]  # Convertir BGR en RGB
                face = img_to_array(face) / 255
                face = np.expand_dims(face, axis=0)

                predictions = classifier.predict(face)[0]
                predicted_class_index = np.argmax(predictions)
                predicted_class_name = classes[predicted_class_index]

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(frame, predicted_class_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_placeholder.image(frame, channels="RGB")

                if cv2.waitKey(1) & 0xFF == ord("q") or stop_button_pressed:
                    break
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()



