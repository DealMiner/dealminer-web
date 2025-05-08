import requests
from bs4 import BeautifulSoup

def scrape_data(url):
    """
    Extrait les informations principales depuis l'URL d'une annonce.
    Retourne une liste de dictionnaires avec Titre, Description, Lien.
    """
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            return [{"Erreur": f"Échec de la requête ({response.status_code})"}]

        soup = BeautifulSoup(response.content, "html.parser")

        # Extraction basique pour tout type de site
        titre = soup.title.get_text(strip=True) if soup.title else "Titre non trouvé"

        description_tag = soup.find("meta", attrs={"name": "description"}) or \
                          soup.find("meta", attrs={"property": "og:description"})

        description = description_tag["content"] if description_tag and "content" in description_tag.attrs else "Description non trouvée"

        return [{
            "Titre": titre,
            "Description": description,
            "Lien de l’annonce": url
        }]

    except Exception as e:
        return [{"Erreur": str(e)}]
