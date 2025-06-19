# models.py

import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# Table to store phishing templates
c.execute('''CREATE TABLE IF NOT EXISTS templates (
    id INTEGER PRIMARY KEY,
    name TEXT,
    content TEXT
)''')

# Table to store clicks (logs)
c.execute('''CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY,
    template_id INTEGER,
    email TEXT,
    clicked INTEGER,
    timestamp TEXT
)''')

conn.commit()
conn.close()
print("Database initialized successfully.")
