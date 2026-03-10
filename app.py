import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
from ORM import ORM
from client import Client

load_dotenv()

app = Flask(__name__)
CORS(app)

orm = ORM(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

client_model = Client(orm)

@app.route('/', methods=['GET'])
def index():
    return "<button>Bienvenue à l'API de Léo</button>"

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({
        'message': 'Hello, World!',
        'status': 'success'
    })

@app.route('/api/users', methods=['GET'])
def get_api_users():
    users = orm.select_all("clients")
    return jsonify(users)

@app.route('/users', methods=['GET'])
def get_users():
    users = client_model.get_all()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Aucune donnée JSON envoyée"}), 400

    prenom = data.get("prenom")
    nom = data.get("nom")
    telephone = data.get("telephone")
    email = data.get("email")
    a_permis_bateau = data.get("a_permis_bateau", 0)

    if not prenom or not nom or not telephone or not email:
        return jsonify({"error": "prenom, nom, telephone et email sont obligatoires"}), 400

    new_user = {
        "nom": nom,
        "prenom": prenom,
        "telephone": telephone,
        "email": email,
        "a_permis_bateau": a_permis_bateau
    }

    inserted_id = client_model.create(new_user)

    return jsonify({
        "message": "Client ajouté avec succès",
        "id_client": inserted_id
    }), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "Aucune donnée JSON envoyée"}), 400

    nom = data.get("nom")
    prenom = data.get("prenom")
    telephone = data.get("telephone")
    email = data.get("email")
    a_permis_bateau = data.get("a_permis_bateau", 0)

    if not nom or not prenom or not telephone or not email:
        return jsonify({"error": "nom, prenom, telephone et email sont obligatoires"}), 400

    updated_data = {
        "nom": nom,
        "prenom": prenom,
        "telephone": telephone,
        "email": email,
        "a_permis_bateau": a_permis_bateau
    }

    rows_affected = client_model.update(user_id, updated_data)

    if rows_affected == 0:
        return jsonify({"error": f"Aucun client trouvé avec l'id {user_id}"}), 404

    return jsonify({"message": f"Client {user_id} mis à jour avec succès"})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    rows_affected = client_model.delete(user_id)

    if rows_affected == 0:
        return jsonify({"error": f"Aucun client trouvé avec l'id {user_id}"}), 404

    return jsonify({"message": f"Client avec id {user_id} supprimé avec succès"})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)