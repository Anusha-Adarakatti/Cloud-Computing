from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

# Database configuration
DB_HOST = os.getenv('DB_HOST', 'postgres-service')
DB_NAME = os.getenv('DB_NAME', 'issues_db')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASS = os.getenv('DB_PASS', 'postgres')

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    return conn

@app.route('/')
def admin_dashboard():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, title, description, email, status, created_at FROM issues ORDER BY created_at DESC')
    issues = cur.fetchall()
    cur.close()
    conn.close()
    
    return render_template('admin.html', issues=issues)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)