import streamlit as st

def display_results():
    st.header("📊 Résultats")
    if "results" in st.session_state:
        st.dataframe(st.session_state["results"])
    else:
        st.info("Aucun résultat à afficher. Lancez un scan d'abord.")
