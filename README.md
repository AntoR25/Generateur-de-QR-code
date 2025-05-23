pip install -r requirements.txt


python ui.py


pytest test_logic.py


qr_project/

├── ui.py               # Interface graphique (Tkinter)

├── logic.py            # Fonctions métiers : QR code, persistance

├── test_logic.py       # Tests unitaires avec pytest

├── logs.txt            # Fichier texte de persistance

└── requirements.txt    # Dépendances
