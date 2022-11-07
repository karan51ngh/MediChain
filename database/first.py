import sqlite3
import datetime

# connects to db if exists, otherwise creates a DB
conn = sqlite3.connect('patients.db')

c = conn.cursor()  # cursor

# c.execute("""CREATE TABLE patients (
#             idx text,
#             f_name text,
#             l_name text,
#             age text,
#             timestamp text,
#             previous_hash text,
#             proof text
#             )""")

c.execute("INSERT INTO  patients VALUES (?, ?, ?, ?, ? ,? ,? )",
          ("0001", "Karan", "SIngh", "21", str(datetime.datetime.now()), "2", "2"))

# c.execute("INSERT INTO  patients VALUES (?, ?, ?, ?, ? ,? ,? )",
#           ("0002", "Fred", "Nietzsche", "65", str(datetime.datetime.now()), "0", "0"))

# c.execute("INSERT INTO  patients VALUES (?, ?, ?, ?, ? ,? ,? )",
#           ("0003", "Jordan", "Peterson", "60", str(datetime.datetime.now()), "1", "1"))

# c.execute("SELECT DISTINCT * FROM patients")

# listt = c.fetchall()

# for i in listt:
#     print(f'{i[0]} {i[1]} {i[2]} {i[3]} {i[4]} {i[5]} {i[6]}')


# conn.commit()
conn.close()
