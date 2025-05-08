import streamlit as st
import pandas as pd
import os

RESULTS_FILE = "results.csv"

def run_export_tools():
    st.header("📁 Export & Suivi")
    
    if not os.path.exists(RESULTS_FILE):
        st.info("Aucun fichier de résultats trouvé.")
        return

    df = pd.read_csv(RESULTS_FILE)

    # 📥 Téléchargement en CSV
    st.download_button(
        label="Télécharger en CSV",
        data=df.to_csv(index=False).encode('utf-8'),
        file_name="resultats.csv",
        mime="text/csv"
    )

    # 📥 Téléchargement en Excel (si tu veux aussi cette option)
    st.download_button(
        label="Télécharger en Excel",
        data=df.to_excel(index=False, engine='openpyxl'),
        file_name="resultats.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
