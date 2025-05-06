import streamlit as st
import pandas as pd
from scraper import scrape_data
from image_analysis import analyze_image
import datetime
import os

# Configuration initiale
st.set_page_config(page_title="DealMiner", layout="wide")

# Titre
st.title("🪙 DealMiner - Détection de Bonnes Affaires")

# Onglets de navigation
tab1, tab2, tab3, tab4 = st.tabs(["🔍 Détection", "📊 Résultats", "📁 Export & Suivi", "🖼️ Analyse d’image"])

# Détection
with tab1:
    st.header("Lancer une détection")
    url_input = st.text_input("Entrez l'URL d'un site de petites annonces :")

    if st.button("Démarrer le scan"):
        if url_input:
            with st.spinner("Analyse en cours..."):
                df = scrape_data(url_input)
                st.session_state['resultats'] = df
                st.success(f"{len(df)} résultats détectés.")
        else:
            st.warning("Merci de fournir une URL.")

# Résultats
with tab2:
    st.header("Résultats détectés")

    if 'resultats' in st.session_state:
        df = st.session_state['resultats']

        # Filtres dynamiques (à compléter plus tard)
        nb_resultats = st.slider("Nombre de résultats à afficher", 1, len(df), min(10, len(df)))
        st.dataframe(df.head(nb_resultats), use_container_width=True)
    else:
        st.info("Aucun résultat disponible. Lancez une détection dans l'onglet précédent.")

# Export
with tab3:
    st.header("Export des résultats")

    if 'resultats' in st.session_state:
        df = st.session_state['resultats']
        date_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"resultats_dealminer_{date_str}.xlsx"

        if st.button("📥 Exporter en Excel"):
            df.to_excel(filename, index=False)
            st.success(f"Fichier {filename} généré.")
            with open(filename, "rb") as f:
                st.download_button("📄 Télécharger le fichier", f, file_name=filename)
    else:
        st.info("Aucun résultat à exporter.")

# Analyse d’image
with tab4:
    st.header("Analyse visuelle d’un objet")
    image_file = st.file_uploader("Téléversez une image", type=["jpg", "png", "jpeg"])

    if image_file is not None:
        image_path = os.path.join("temp_image.jpg")
        with open(image_path, "wb") as f:
            f.write(image_file.read())
        st.image(image_path, caption="Image chargée", use_column_width=True)

        if st.button("Lancer l’analyse visuelle"):
            with st.spinner("Analyse en cours..."):
                analyze_image(image_path)
            st.success("Analyse terminée.")

st.markdown("---")
st.caption("📦 Projet DealMiner - Version Web initiale | 2025")
