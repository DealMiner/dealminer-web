from twilio.rest import Client

# Configuration de Twilio (remplace ces valeurs par les tiennes)
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
from_number = 'your_twilio_number'
to_number = 'recipient_phone_number'

# Fonction pour envoyer un SMS
def send_sms(message):
    # Créer une instance du client Twilio
    client = Client(account_sid, auth_token)
    
    # Envoie du message
    message = client.messages.create(
        body=message,
        from_=from_number,
        to=to_number
    )
    
    print(f"Message envoyé à {to_number}: {message.sid}")

# Exemple d'utilisation
if __name__ == "__main__":
    message = "Ceci est un test d'alerte Twilio."
    send_sms(message)
