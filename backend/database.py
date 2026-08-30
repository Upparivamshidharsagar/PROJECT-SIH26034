import sqlite3

connection = sqlite3.connect("compliance.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS inspections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    status TEXT NOT NULL,
    issues TEXT
)
""")

connection.commit()
connection.close()

print("Database and inspections table created!")