import sqlite3

connection = sqlite3.connect('BobaViews.db')


with open('db/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()


connection.commit()
connection.close()