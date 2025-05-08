import streamlit as st
from PIL import Image
import numpy as np

def run_image_analysis():
    st.header("🖼️ Analyse d’image – Estimation de l’état de l’objet")
    uploaded_file = st.file_uploader("📷 Téléversez une photo de l’objet", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Charger l'image avec Pillow
        image = Image.open(uploaded_file)
        st.image(image, caption="Image importée", use_column_width=True)

        # Convertir l'image en niveaux de gris
        grayscale = np.array(image.convert("L"))
        average_brightness = np.mean(grayscale)

        # Estimation de l'état basé sur la luminosité
        if average_brightness > 160:
            state = "✨ Très bon état"
        elif average_brightness > 100:
            state = "🟡 État moyen"
        else:
            state = "🔴 État faible"

        st.write(f"💡 Luminosité moyenne : **{average_brightness:.1f}**")
        st.success(f"État estimé : **{state}**")
