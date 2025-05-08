import streamlit as st
from PIL import Image

def run_image_analysis():
    st.header("🖼️ Analyse d'image")
    uploaded = st.file_uploader("Téléversez une image", type=["png", "jpg", "jpeg"])
    if uploaded:
        image = Image.open(uploaded)
        st.image(image, caption="Image chargée", use_column_width=True)
        st.success("Image analysée (placeholder)")
