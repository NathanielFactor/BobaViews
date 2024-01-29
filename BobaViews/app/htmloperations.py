import sqlite3
from datetime import datetime
from BobaViews.app.imagebot import ai_response

# Connect to the SQLite database

connection = sqlite3.connect('db/BobaViews.db')
cursor = connection.cursor()

# Close the database connection
connection.commit()
connection.close()

