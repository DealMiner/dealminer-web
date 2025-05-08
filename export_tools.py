import streamlit as st
import pandas as pd
import os

RESULTS_FILE = "results.csv"

def run_export_tools():
    st.header("📁 Export & Sauvegarde des trouvailles")

    # Priorité aux résultats en session
    if "results" in st.session_state and st.session_state["results"]:
        df = pd.DataFrame(st.session_state["results"])
    elif os.path.exists(RESULTS_FILE):
        df = pd.read_csv(RESULTS_FILE)
    else:
        st.info("Aucun résultat disponible à exporter.")
        return

    st.write("📄 Aperçu des résultats à exporter :")
    st.dataframe(df, use_container_width=True)

    # Export CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇️ Télécharger au format CSV",
        data=csv,
        file_name="dealminer_resultats.csv",
        mime="text/csv"
    )

    # Export Excel
    try:
        excel = df.to_excel(index=False, engine='openpyxl')
        st.download_button(
            label="⬇️ Télécharger au format Excel",
            data=excel,
            file_name="dealminer_resultats.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    except Exception as e:
        st.warning("⚠️ Impossible d’exporter en Excel (vérifiez les dépendances).")

    # Sauvegarde persistante locale
    if st.button("💾 Enregistrer localement (results.csv)", key="save_results_file"):
        df.to_csv(RESULTS_FILE, index=False)
        st.success("Résultats enregistrés dans le fichier `results.csv`")
