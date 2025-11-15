import sqlite3


def init_db():
    with sqlite3.connect(r'C:\Users\Admin\Desktop\tg\Пересылка объявлений с сайта бот\database\autokavkaz.db') as conn:
        cur = conn.cursor()

        cur.execute('''CREATE TABLE IF NOT EXISTS auto (
                            id INTEGER PRIMARY KEY NOT NULL,
                            model TEXT,
                            city TEXT,
                            mileage TEXT,
                            price TEXT,
                            description TEXT,
                            link TEXT,
                            number TEXT,
                            date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            sent INTEGER DEFAULT 0
                    )''')

        conn.commit()