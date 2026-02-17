import os
import mysql.connector

from flask import Flask, jsonify

app = Flask(__name__)



@app.route('/', methods=['GET'])
def index():
    return "<button> Bienvenue </button>"



@app.route('/api/hello', methods=['GET'])
def hello():
    """Returns a greeting message"""
    return jsonify({
        'message': 'Hello, World!',
        'status': 'success'
    })

@app.route('/api/users', methods=['GET'])
def get_users():
    # Connection à la base de données MySQL
    mydb = mysql.connector.connect(
        host="mysql-berke.alwaysdata.net",
        user="berke_jetski",
        password="Jetski567@",
        database="berke_jetski"
    )
    mycursor = mydb.cursor()

    # Exécution de la requête SQL pour récupérer les utilisateurs
    mycursor.execute("SELECT * FROM clients")

    # Récupération des résultats de la requête
    myresult = mycursor.fetchall()



    """Returns a list of users"""
    return jsonify(myresult)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)
