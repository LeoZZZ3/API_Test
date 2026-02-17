import os

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
    """Returns a list of users"""
    return jsonify({
        'users': [
            {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
            {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'},
            {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com'}
        ],
        'total': 3
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)
