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

    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "name et email sont obligatoires"}), 400

    mydb = get_db_connection()
    mycursor = mydb.cursor()

    mycursor.execute(
        "UPDATE clients SET name = %s, email = %s WHERE id = %s",
        (name, email, user_id)
    )
    mydb.commit()

    mycursor.close()
    mydb.close()

    return jsonify({"message": f"User with id {user_id} updated successfully!"})


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    mydb = get_db_connection()
    mycursor = mydb.cursor()

    mycursor.execute("DELETE FROM clients WHERE id = %s", (user_id,))
    mydb.commit()

    mycursor.close()
    mydb.close()

    return jsonify({"message": f"User with id {user_id} deleted successfully!"})


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)