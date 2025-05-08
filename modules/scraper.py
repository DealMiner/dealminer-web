import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
import requests

def scrape_site(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        titles = soup.find_all("h2")
        data = [{"Titre": t.text.strip()} for t in titles]
        return pd.DataFrame(data)
    except Exception as e:
        st.error(f"Erreur de scraping : {e}")
        return pd.DataFrame()

def run_scraper_interface():
    st.header("Lancer une détection")
    url = st.text_input("Entrez l'URL d'un site de petites annonces :")
    if st.button("Démarrer le scan"):
        if url:
            df = scrape_site(url)
            st.session_state["results"] = df
            st.success("Détection terminée.")
        else:
            st.warning("Veuillez entrer une URL valide.")
