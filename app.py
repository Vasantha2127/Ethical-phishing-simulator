# app.py

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    templates = conn.execute('SELECT * FROM templates').fetchall()
    conn.close()
    return render_template('index.html', templates=templates)

@app.route('/create', methods=['POST'])
def create_template():
    name = request.form['name']
    content = request.form['content']
    conn = sqlite3.connect('database.db')
    conn.execute('INSERT INTO templates (name, content) VALUES (?, ?)', (name, content))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/send/<int:template_id>')
def simulate_send(template_id):
    return f"Send this link to test user: http://localhost:5000/clicked/{template_id}?email=test@lab.com"

@app.route('/clicked/<int:template_id>')
def clicked(template_id):
    email = request.args.get('email', 'unknown')
    conn = sqlite3.connect('database.db')
    conn.execute('INSERT INTO logs (template_id, email, clicked, timestamp) VALUES (?, ?, ?, ?)',
                 (template_id, email, 1, datetime.now().isoformat()))
    conn.commit()
    conn.close()
    return "This was a phishing simulation. You've been trained!"

@app.route('/analytics')
def analytics():
    conn = sqlite3.connect('database.db')
    data = conn.execute('SELECT template_id, COUNT(*) as clicks FROM logs GROUP BY template_id').fetchall()
    conn.close()
    return render_template('analytics.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
