import sqlite3


def get_patient_list():
    conn = sqlite3.connect('database/patients.db')
    c = conn.cursor()
    c.execute("SELECT DISTINCT * FROM patients")
    listt = c.fetchall()
    conn.close()
    return listt


def update_patient_record(idx, fn, ln, age, ts, phv, prf):
    conn = sqlite3.connect('database/patients.db')
    c = conn.cursor()
    c.execute("INSERT INTO  patients VALUES (?, ?, ?, ?, ? ,? ,? )",
              (idx, fn, ln, age, ts, phv, prf))
    conn.commit()
    conn.close()
