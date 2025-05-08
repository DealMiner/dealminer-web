import streamlit as st
import pandas as pd

def run_export_tools():
    st.header("📁 Export & Suivi")
    if "results" in st.session_state:
        df = st.session_state["results"]
        st.download_button("Télécharger en CSV", df.to_csv(index=False), "resultats.csv")
        st.download_button("Télécharger en Excel", df.to_excel(index=False, engine='openpyxl'), "resultats.xlsx")
    else:
        st.info("Aucun résultat disponible pour export.")
