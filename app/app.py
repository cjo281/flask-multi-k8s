from flask import Flask, jsonify
# psycopg2 is the PostgreSQL driver
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    """
    Creates a connection to PostgreSQL using environment variables.
    Kubernetes and Docker Compose both inject these variables.
    """
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

@app.route("/")
def root():
    """
    Basic endpoint to confirm the API is running.
    """
    return jsonify(message="Flask API running in a multi-container setup")

@app.route("/db")
def db_test():
    """
    Tests the database connection by running SELECT NOW().
    This confirms:
    - Networking works
    - Credentials are correct
    - PostgreSQL is reachable
    """
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT NOW();")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify(database_time=str(result[0]))

@app.route("/health")
def health():
    """
    Health endpoint used by Kubernetes readiness/liveness probes.
    """
    return jsonify(status="ok")

if __name__ == "__main__":
    # 0.0.0.0 is required so the container is reachable externally
    app.run(host="0.0.0.0", port=5000)
