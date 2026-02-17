import os

from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "mysql-berke.alwaysdata.net"),
        port=int(os.getenv("DB_PORT", 3306)),
        user=os.getenv("DB_USER", "berke"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "berke_jetski"),
    )

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

@app.route('/api/clients/<string:client_id>', methods=['GET'])
def get_client_by_id(client_id):
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT client_id, nom, prenom, email, telephone, date_naissance,
                   permis_bateau, poids, raisons
            FROM clients
            WHERE client_id = %s
            """,
            (client_id,),
        )
        client = cursor.fetchone()
        if client is None:
            return jsonify({"error": "Client not found"}), 404
        return jsonify(client), 200
    except Error as err:
        return jsonify({"error": f"Database error: {err}"}), 500
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)
