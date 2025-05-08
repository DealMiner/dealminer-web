import requests
from bs4 import BeautifulSoup

def scrape_data(url):
    """
    Extrait les informations essentielles depuis une URL de petite annonce.
    Retourne une liste de dictionnaires représentant les données extraites.
    """
    try:
        headers = {"User-Agent": "Mozilla/5.0
