import streamlit as st
import pandas as pd
from scraper import scrape_data
from result_viewer import run_result_viewer
from export_tools import run_export_tools
from image_analysis import run_image_analysis
from profit_score import run_profit_score
from telegram_alert import send_telegram_alert

# Configuration de la page
st.set_page_config(page_title="DealMiner Web", layout="wide")
st.title("💎 DealMiner – Détection intelligente de bonnes affaires")

# Initialisation de session
if "results" not in st.session_state:
    st.session_state["results"] = []

if "last_result" not in st.session_state:
    st.session_state["last_result"] = None

# Menu latéral
menu = st.sidebar.radio("🧭 Navigation", [
    "🔍 Nouvelle détection",
    "📊 Résultats",
    "📁 Export",
    "🖼️ Analyse d’image",
    "💰 Rentabilité"
])

# Onglet 1 : Détection d'annonce
if menu == "🔍 Nouvelle détection":
    st.header("🔍 Analyse d'une annonce en ligne")
    url = st.text_input("📎 Colle ici l'URL d'une annonce")

    if st.button("Lancer la détection", key="btn_detect"):
        with st.spinner("🔎 Analyse en cours..."):
            result = scrape_data(url)
            if result:
                st.session_state["results"].append(result)
                st.session_state["last_result"] = result
                st.success("✅ Annonce analysée avec succès")
                st.write(result)

                # Envoi alerte Telegram
                send_telegram_alert(result)

            else:
                st.error("❌ Aucune donnée récupérée. Vérifie l'URL.")

# Onglet 2 : Visualisation des résultats
elif menu == "📊 Résultats":
    run_result_viewer()

# Onglet 3 : Export CSV/Excel
elif menu == "📁 Export":
    run_export_tools()

# Onglet 4 : Analyse d’image
elif menu == "🖼️ Analyse d’image":
    run_image_analysis()

# Onglet 5 : Calcul de rentabilité
elif menu == "💰 Rentabilité":
    run_profit_score()

