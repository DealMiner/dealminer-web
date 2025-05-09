import requests
from bs4 import BeautifulSoup
import random
import re

# Liste de mots-clés rares ou collectionnables
MOTS_RARES = [
    "édition limitée", "prototype", "collector", "vintage", "1ère édition",
    "numéroté", "signé", "ancien", "rare", "épuisé", "rarement vu"
]

# Estimation de prix de revente
def estimer_prix_revente(prix_actuel, rarete):
    multiplicateur = 1.5 + (rarete / 100)
    return round(prix_actuel * multiplicateur, 2)

# Plafonnement spécial pour cartes non gradées
def appliquer_regle_cartes(objet, etat, prix_estime):
    if (
        "carte" in objet.lower()
        and any(x in objet.lower() for x in ["pokemon", "magic", "yu-gi-oh"])
        and "non gradée" in etat.lower()
        and "mint" not in etat.lower()
    ):
        return min(prix_estime, 30)
    return prix_estime

# Fonction principale
def scrape_data(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(url, headers=headers, timeout=10)

        if r.status_code != 200:
            return {"Erreur": f"Échec requête {r.status_code}", "Lien": url}

        soup = BeautifulSoup(r.content, "html.parser")
        titre = soup.title.get_text(strip=True) if soup.title else "Titre non trouvé"
        description_tag = soup.find("meta", attrs={"name": "description"}) or soup.find("meta", attrs={"property": "og:description"})
        description = description_tag["content"] if description_tag and "content" in description_tag.attrs else "Description non trouvée"

        texte_complet = (titre + " " + description).lower()
        prix_detecte = detecter_prix(texte_complet)
        rarete = detecter_rarete(texte_complet)
        prix_revente = estimer_prix_revente(prix_detecte, rarete)

        # Appliquer règle spéciale si carte non gradée
        prix_revente_corrige = appliquer_regle_cartes(titre, description, prix_revente)

        score = int((rarete + random.randint(20, 40)) if rarete > 0 else random.randint(25, 50))

        return {
            "Titre": titre,
            "Description": description,
            "Prix détecté (€)": prix_detecte,
            "Indice de rareté": rarete,
            "Prix estimé revente (€)": prix_revente_corrige,
            "Score global (/100)": score,
            "Lien de l’annonce": url
        }

    except Exception as e:
        return {"Erreur": str(e), "Lien": url}

# Tentative de détection du prix dans le texte
def detecter_prix(texte):
    prix = re.findall(r"\d{1,4}(?:[.,]\d{1,2})?\s?(?:€|eur|euros)", texte)
    if prix:
        nombre = re.findall(r"\d{1,4}(?:[.,]\d{1,2})?", prix[0])[0]
        return float(nombre.replace(",", "."))
    return random.randint(5, 80)

# Détection de rareté
def detecter_rarete(texte):
    return sum(1 for mot in MOTS_RARES if mot in texte) * 10  # max 100

