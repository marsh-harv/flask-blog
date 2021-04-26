import sqlite3


connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())


cur = connection.cursor()


cur.execute("INSERT INTO login (email, password) VALUES (?, ?)",
            ('marshall.harvey@outlook.com', '1234')
            )




connection.commit()
connection.close()
