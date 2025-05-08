import streamlit as st
from PIL import Image
import numpy as np

def run_image_analysis():
    st.subheader("🖼️ Analyse d’image – Estimation de l’état de l’objet")
    uploaded_file = st.file_uploader("Téléversez une photo de l’objet", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Image importée", use_column_width=True)

        # Conversion en niveaux de gris
        grayscale = np.array(image.convert("L"))
        avg_brightness = np.mean(grayscale)

        # Évaluation simple de l’état selon la luminosité
        if avg_brightness > 160:
            etat = "✨ Très bon état"
        elif avg_brightness > 100:
            etat = "🟡 État moyen"
        else:
            etat = "🔴 État faible"

        st.write(f"💡 Luminosité moyenne : **{avg_brightness:.1f}**")
        st.success(f"Estimation de l’état : **{etat}**")
