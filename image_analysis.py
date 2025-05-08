import streamlit as st
import cv2
import numpy as np
from io import BytesIO

def run_image_analysis():
    st.header("🖼️ Analyse d’image – Estimation de l’état de l’objet")
    uploaded_file = st.file_uploader("📷 Téléversez une photo de l’objet", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Convertir l'image en format compatible OpenCV
        image = np.array(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        
        # Convertir l'image en niveaux de gris
        grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        average_brightness = np.mean(grayscale)

        # Affichage de l'image
        st.image(image, caption="Image importée", use_column_width=True)

        # Estimation de l'état basé sur la luminosité
        if average_brightness > 160:
            state = "✨ Très bon état"
        elif average_brightness > 100:
            state = "🟡 État moyen"
        else:
            state = "🔴 État faible"

        st.write(f"💡 Luminosité moyenne : **{average_brightness:.1f}**")
        st.success(f"État estimé : **{state}**")
