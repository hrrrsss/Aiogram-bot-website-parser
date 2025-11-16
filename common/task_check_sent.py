import sqlite3

def check_sent():
    with sqlite3.connect('database/autokavkaz.db') as conn:
        cur = conn.cursor()

        cur.execute('''SELECT id, model, city, mileage, price, description, link, number FROM auto WHERE sent == 0 ORDER BY id ASC LIMIT 1''')
        result = cur.fetchone()

        if result:
            cur.execute('''UPDATE auto SET sent = 1 WHERE id == ?''',
                                            (result[0],))
            
            conn.commit()

        return result