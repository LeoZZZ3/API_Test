import os
from dotenv import load_dotenv
from database import ORM

# 1. Charger les variables d'environnement
load_dotenv()

# 2. Initialiser l'ORM
db = ORM(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

def test_unitaire():
    print("--- Démarrage des tests ORM ---")
    
    try:
        # TEST 1 : Lecture
        print("Test SELECT...")
        users = db.select_all("clients")
        print(f"Succès ! Nombre de clients trouvés : {len(users)}")

        # TEST 2 : Insertion
        print("Test INSERT...")
        nouveau_client = {
            "nom": "Testeur",
            "prenom": "Jean",
            "telephone": "0102030405",
            "email": "test@example.com"
        }
        db.insert("clients", nouveau_client)
        print("Succès ! Client inséré.")

        # TEST 3 : Vérification de l'insertion
        users_apres = db.select_all("clients")
        if len(users_apres) > len(users):
            print("Vérification : La base de données contient bien un nouveau client.")

    except Exception as e:
        print(f"Erreur lors des tests : {e}")

if __name__ == "__main__":
    test_unitaire()