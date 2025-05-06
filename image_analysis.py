from PIL import Image

# Fonction pour charger et afficher une image
def analyze_image(image_path):
    # Ouvre l'image
    image = Image.open(image_path)
    
    # Affiche l'image
    image.show()

# Exemple d'utilisation
if __name__ == "__main__":
    image_path = "path/to/your/image.jpg"
    analyze_image(image_path)
