from flask import Flask, jsonify
import mysql.connector
import time

app = Flask(__name__)


DB_HOST = "mysql_db"

def get_connection():
    while True:
        try:
            conn = mysql.connector.connect(
                host=DB_HOST,
                user="root",
                password="root",
                database="parcial_db"
            )
            return conn
        except:
            print("Esperando DB...")
            time.sleep(2)

@app.route("/")
def index():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios")
    data = cursor.fetchall()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)