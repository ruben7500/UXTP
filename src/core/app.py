from flask import Flask, jsonify, request
from flask_cors import CORS  # Import flask-cors
import sqlite3
import os

app = Flask(__name__)
CORS(app)  # Activer CORS pour toutes les routes

DATABASE = 'bdd.sqlite'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/products', methods=['GET'])
def get_products():
    try:
        page = int(request.args.get('page', 1))
        per_page = 10
        offset = (page - 1) * per_page

        conn = get_db_connection()
        products = conn.execute('SELECT * FROM products LIMIT ? OFFSET ?', (per_page, offset)).fetchall()
        conn.close()

        return jsonify([dict(product) for product in products])
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Renvoie un message d'erreur en cas de problème

if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        print("Database not found. Run faker_data.py to generate data.")
    app.run(debug=True)
