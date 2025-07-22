from flask import Flask, render_template, request, redirect
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
def index():
    return render_template('user.html')

@app.route('/submit', methods=['POST'])
def submit_issue():
    title = request.form['title']
    description = request.form['description']
    email = request.form['email']
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO issues (title, description, email, status) VALUES (%s, %s, %s, %s)',
        (title, description, email, 'open')
    )
    conn.commit()
    cur.close()
    conn.close()
    
    return redirect('/')

if __name__ == '__main__':
    # Initialize database table if not exists
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS issues (
            id SERIAL PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            description TEXT NOT NULL,
            email VARCHAR(100) NOT NULL,
            status VARCHAR(20) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()
    
    app.run(host='0.0.0.0', port=5000)