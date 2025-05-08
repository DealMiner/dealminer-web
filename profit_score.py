import streamlit as st

def run_profit_score():
    st.header("💰 Estimation de la rentabilité d’un achat")

    prix_achat = st.number_input("💸 Prix d'achat (€)", min_value=0.0, step=0.5)
    prix_revente = st.number_input("💰 Prix estimé de revente (€)", min_value=0.0, step=0.5)
    frais = st.number_input("📦 Frais éventuels (livraison, commissions…) (€)", min_value=0.0, step=0.5)

    if st.button("Calculer la rentabilité", key="btn_profit_calc"):
        if prix_revente > 0:
            benefice_net = prix_revente - prix_achat - frais
            marge_pct = (benefice_net / prix_achat * 100) if prix_achat > 0 else 0

            # Score basé sur la marge
            if benefice_net <= 0:
                score = 10
            elif marge_pct >= 100:
                score = 95
            elif marge_pct >= 50:
                score = 85
            elif marge_pct >= 30:
                score = 70
            elif marge_pct >= 15:
                score = 55
            else:
                score = 40

            st.write(f"🧾 Bénéfice net estimé : **{benefice_net:.2f} €**")
            st.write(f"📈 Marge estimée : **{marge_pct:.1f} %**")
            st.success(f"📊 Score de rentabilité : **{score} / 100**")
        else:
            st.warning("⚠️ Veuillez indiquer un prix de revente supérieur à 0.")

