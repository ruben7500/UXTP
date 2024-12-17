
import sqlite3
from faker import Faker

fake = Faker()
DATABASE = 'bdd.sqlite'

def generate_data():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS products')
    c.execute('''
        CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL,
            description TEXT
        )
    ''')
    for _ in range(500):
        c.execute('INSERT INTO products (name, price, description) VALUES (?, ?, ?)', 
                  (fake.name(), fake.random_number(digits=4), fake.text()))
    conn.commit()
    conn.close()
    print("Database created and populated with Faker data.")

if __name__ == "__main__":
    generate_data()
