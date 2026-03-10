import os
import mysql.connector
from flask_cors import CORS
from flask import Flask, jsonify, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


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
    mydb = get_db_connection()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM clients")
    myresult = mycursor.fetchall()

    mycursor.close()
    mydb.close()

    return jsonify(myresult)


@app.route('/users', methods=['GET'])
def get_users():
    mydb = get_db_connection()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM clients")
    myresult = mycursor.fetchall()

    mycursor.close()
    mydb.close()

    return jsonify(myresult)


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Aucune donnée JSON envoyée"}), 400

    prenom = data.get("prenom")
    nom = data.get("nom")
    telephone = data.get("telephone")
    email = data.get("email")

    if not prenom or not nom or not telephone or not email:
        return jsonify({"error": "prenom, nom, telephone et email sont obligatoires"}), 400

    mydb = get_db_connection()
    mycursor = mydb.cursor()

    mycursor.execute(
        "INSERT INTO clients (nom, prenom, telephone, email) VALUES (%s,%s,%s,%s)",
        (nom, prenom, telephone, email)
    )

    mydb.commit()

    mycursor.close()
    mydb.close()

    return jsonify({"message": "Client ajouté avec succès"})


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

    mydb = get_db_connection()
    mycursor = mydb.cursor()

    mycursor.execute(
        """
        UPDATE clients
        SET nom = %s, prenom = %s, telephone = %s, email = %s, a_permis_bateau = %s
        WHERE id_client = %s
        """,
        (nom, prenom, telephone, email, a_permis_bateau, user_id)
    )
    mydb.commit()

    mycursor.close()
    mydb.close()

    return jsonify({"message": f"Client {user_id} mis à jour avec succès"})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    mydb = get_db_connection()
    mycursor = mydb.cursor()

    mycursor.execute("DELETE FROM clients WHERE id_client = %s", (user_id,))
    mydb.commit()

    mycursor.close()
    mydb.close()

    return jsonify({"message": f"Client avec id {user_id} supprime avec succes"})


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)