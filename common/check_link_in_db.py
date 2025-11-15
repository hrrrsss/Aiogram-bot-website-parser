#Данный вспомогательный модуль нужен для того чтобы отсеить ссылки, которые уже есть базеданных


import sqlite3

from parsing.first_stage import links


def check_link():
    global links

    with sqlite3.connect("database/autokavkaz.db") as file:
        cur = file.cursor()
        
        for i in range(len(links)):
            cur.execute('''SELECT 1 FROM auto WHERE link = ?''', (links[i],))
            result = cur.fetchone()
            if result:
                links = links[:i]
                break

    return links