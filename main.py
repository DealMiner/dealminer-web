import streamlit as st
from modules.scraper import run_scraper_interface
from modules.image_analysis import run_image_analysis
from modules.export_tools import run_export_tools
from modules.result_viewer import display_results

st.set_page_config(page_title="DealMiner", layout="wide")
st.title("📀 DealMiner - Détection de Bonnes Affaires")

menu = ["🔍 Détection", "📊 Résultats", "📁 Export & Suivi", "🖼️ Analyse d'image"]
choice = st.sidebar.radio("Navigation", menu)

if choice == "🔍 Détection":
    run_scraper_interface()
elif choice == "📊 Résultats":
    display_results()
elif choice == "📁 Export & Suivi":
    run_export_tools()
elif choice == "🖼️ Analyse d'image":
    run_image_analysis()
