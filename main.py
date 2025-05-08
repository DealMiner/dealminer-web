import streamlit as st
import pandas as pd
from scraper import scrape_data
from image_analysis import run_image_analysis

# Configuration de la page
st.set_page_config(page_title="DealMiner Web", layout="wide")
st.title("🪙 DealMiner - Détection de Bonnes Affaires")

# Initialisation des résultats en mémoire
if "results" not in st.session_state:
    st.session_state["results"] = []

# Menu de navigation
menu = st.sidebar.radio("Navigation", [
    "🔍 Détection",
    "📊 Résultats",
    "📁 Export",
    "🖼️ Analyse d’image"
])

# Onglet : Détection
if menu == "🔍 Détection":
    st.header("🔍 Détection d'une annonce")
    url = st.text_input("Entrez l'URL d'une annonce à analyser")

    if st.button("Lancer la détection") and url:
        with st.spinner("Analyse en cours..."):
            results = scrape_data(url)
            st.session_state["results"] = results
            st.success(f"{len(results)} élément(s) détecté(s)")

# Onglet : Résultats
elif menu == "📊 Résultats":
    st.header("📊 Résultats")
    if st.session_state["results"]:
        df = pd.DataFrame(st.session_state["results"])
        st.dataframe(df, use_container_width=True)
    else:
        st.info("Aucun résultat disponible. Lancez une détection dans l'onglet précédent.")

# Onglet : Export
elif menu == "📁 Export":
    st.header("📁 Export des résultats")
    if st.session_state["results"]:
        df = pd.DataFrame(st.session_state["results"])
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📄 Télécharger en CSV", csv, "resultats_dealminer.csv", "text/csv")
    else:
        st.info("Aucun résultat à exporter.")

# Onglet : Analyse d’image
elif menu == "🖼️ Analyse d’image":
    run_image_analysis()
