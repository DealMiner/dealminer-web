import streamlit as st
import pandas as pd
import os

RESULTS_FILE = "results.csv"

def run_result_viewer():
    st.header("📊 Résultats")
    
    if not os.path.exists(RESULTS_FILE):
        st.info("Aucun résultat à afficher. Lancez un scan d'abord.")
        return

    df = pd.read_csv(RESULTS_FILE)
    if df.empty:
        st.warning("Le fichier de résultats est vide.")
    else:
        st.dataframe(df)
