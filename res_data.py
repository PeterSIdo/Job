# This script creates the ResData table 
import sqlite3
conn = sqlite3.connect("ResData.db")
cursor = conn.cursor()

# SQLite CREATE TABLE statement
create_table_query = """
CREATE TABLE IF NOT EXISTS Cardex (
    ResId TEXT,
    ResName TEXT,
    CarerName TEXT,
    DateRecord TEXT,
    TimeRecord TEXT,
    CardexText TEXT
)
"""

cursor.execute(create_table_query)
conn.commit()
conn.close()