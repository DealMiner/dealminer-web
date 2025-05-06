import requests
from bs4 import BeautifulSoup
import pandas as pd

# Exemple de fonction pour scraper des données
def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Exemple : récupération des titres de produits
    product_titles = soup.find_all('h2', class_='product-title')
    
    products = []
    for title in product_titles:
        products.append(title.text.strip())

    # Retourne les données sous forme de DataFrame pandas
    df = pd.DataFrame(products, columns=['Product Title'])
    return df

# Exemple d'utilisation
if __name__ == "__main__":
    url = "https://www.example.com/products"
    data = scrape_data(url)
    print(data)
