import streamlit as st
import pandas as pd

def run_result_viewer():
    st.header("📊 Résultats – Objets détectés")

    if "results" not in st.session_state or not st.session_state["results"]:
        st.info("Aucun objet détecté pour le moment. Lancez une analyse dans l'onglet '🔍 Nouvelle détection'.")
        return

    df = pd.DataFrame(st.session_state["results"])

    # Colonnes à afficher (si présentes)
    colonnes_affichees = [
        "Titre", "Description", "Prix détecté (€)", "Indice de rareté",
        "Prix estimé revente (€)", "Score global (/100)", "Lien de l’annonce"
    ]
    colonnes_existantes = [col for col in colonnes_affichees if col in df.columns]
    df = df[colonnes_existantes]

    # Tri par score décroissant
    df = df.sort_values(by="Score global (/100)", ascending=False)

    st.dataframe(df, use_container_width=True)

    # Sauvegarde temporaire possible (fichier CSV)
    if st.button("💾 Sauvegarder dans un fichier", key="save_results_btn"):
        df.to_csv("results.csv", index=False)
        st.success("Les résultats ont été enregistrés dans `results.csv`")
