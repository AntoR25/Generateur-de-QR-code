import qrcode
import os
from PIL import Image

def generate_qr_code(text, filename='qr_code.png'):
    """
    Génère un QR Code à partir du texte fourni et le sauvegarde sous forme d'image.
    
    Parameters:
        text (str): le texte à encoder dans le QR Code.
        filename (str): le nom du fichier image à sauvegarder.

    Returns:
        str: le chemin du fichier image sauvegardé.
    """
    if not text:
        raise ValueError("Le texte ne peut pas être vide.")

    try:
        qr = qrcode.QRCode(box_size=10, border=2)
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")
        img.save(filename)
        return filename
    except Exception as e:
        raise RuntimeError(f"Erreur lors de la génération du QR Code: {e}")

def save_text(text, filepath="logs.txt"):
    """
    Sauvegarde le texte entré dans un fichier pour persistance.

    Parameters:
        text (str): le texte à sauvegarder.
        filepath (str): le chemin du fichier texte.
    """
    try:
        with open(filepath, "a", encoding="utf-8") as file:
            file.write(text + "\n")
    except Exception as e:
        raise IOError(f"Échec de la sauvegarde du texte: {e}")