from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Configuración de PostgreSQL
POSTGRES = {
    "dbname": "tu_base",
    "user": "tu_usuario",
    "password": "tu_contraseña",
    "host": "localhost",
    "port": 5432
}

def connect_db():
    return psycopg2.connect(**POSTGRES)

@app.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO clientes (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)",
            (data["first_name"], data["last_name"], data["email"], data["password"])
        )
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Usuario registrado exitosamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
ssss