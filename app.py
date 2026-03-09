import os
import mysql.connector
from flask_cors import CORS
from flask import Flask, jsonify, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

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
def get_users():
    mydb = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM clients")
    myresult = mycursor.fetchall()

    mycursor.close()
    mydb.close()

    return jsonify(myresult)

@app.route('/api/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'GET':
        return "Cette route attend une requête POST"

    data = request.json
    name = data.get("name")
    age = data.get("age")

    return jsonify({
        "message": "Utilisateur reçu",
        "name": name,
        "age": age
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)