import sqlite3
import datetime

# connects to db if exists, otherwise creates a DB
conn = sqlite3.connect('patients.db')

c = conn.cursor()  # cursor

c.execute("SELECT DISTINCT * FROM patients")

listt = c.fetchall()

for i in listt:
    print(f'{i[0]} {i[1]} {i[2]} {i[3]} {i[4]} {i[5]} {i[6]}')


# conn.commit()
conn.close()
