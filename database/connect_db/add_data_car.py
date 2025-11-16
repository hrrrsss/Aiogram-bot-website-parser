import sqlite3


def add_auto(model, city, mileage, price, description, link, number):
    with sqlite3.connect('database/autokavkaz.db') as conn:
        cur = conn.cursor()

        cur.execute('''INSERT INTO auto (model, city, mileage, price, description, link, number)
                                    VALUES (?, ?, ?, ?, ?, ?, ?)''',
                                    (model, city, mileage, price, description, link, number))
        
        conn.commit()