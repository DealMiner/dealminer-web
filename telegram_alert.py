import requests
import os

# Configuration : ajoute ces deux secrets dans Streamlit (Settings > Secrets)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")     # Clé API de ton bot
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID") # ID du chat ou canal cible

def send_telegram_alert(data):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        return  # Sécurité : ne rien envoyer si les infos ne sont pas configurées

    # Construction du message
    try:
        message = f"📢 Nouvelle trouvaille DealMiner :\n\n"
        message += f"🔸 **{data.get('Titre', 'Objet inconnu')}**\n"
        message += f"💶 Prix : {data.get('Prix détecté (€)', '?')} €\n"
        message += f"📈 Score : {data.get('Score global (/100)', '?')} / 100\n"
        message += f"🔗 Lien : {data.get('Lien de l’annonce', 'non précisé')}"

        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": "Markdown"
        }
        requests.post(url, data=payload, timeout=10)

    except Exception as e:
        print("Erreur lors de l’envoi Telegram :", e)
