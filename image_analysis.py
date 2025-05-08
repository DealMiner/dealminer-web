import streamlit as st
from PIL import Image
import numpy as np

def run_image_analysis():
    st.header("🖼️ Analyse d’image – État de l’objet")
    uploaded_file = st.file_uploader("📷 Téléversez une photo de l’objet", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Image importée", use_column_width=True)

        # Analyse simple par luminosité
        grayscale = np.array(image.convert("L"))
        moyenne = np.mean(grayscale)

        if moyenne > 160:
            etat = "✨ Très bon état"
        elif moyenne > 100:
            etat = "🟡 État moyen"
        else:
            etat = "🔴 État faible"

        st.write(f"💡 Luminosité moyenne : **{moyenne:.1f}**")
        st.success(f"État estimé : **{etat}**")
