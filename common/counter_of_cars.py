import sqlite3


def count_of_auto_in_db():
    with sqlite3.connect("database/autokavkaz.db") as conn:
        cur = conn.cursor()

        cur.execute('''SELECT COUNT(id) FROM auto''')

        for i in cur.fetchone():
            result = i + 1


    return result