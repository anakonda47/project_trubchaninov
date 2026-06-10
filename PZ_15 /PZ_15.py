import sqlite3
from db import insert_data

DB_NAME = "car_rental.db"


def main(title, rows):
    print(f"\n{title}:")
    for row in rows:
        print(row)


with sqlite3.connect(DB_NAME) as conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS client (
            client_id INTEGER PRIMARY KEY AUTOINCREMENT,
            fio TEXT NOT NULL,
            car_model TEXT NOT NULL,
            rental_period INTEGER NOT NULL,
            total_sum REAL NOT NULL,
            prepayment TEXT NOT NULL
        )
    """)


insert_data()

with sqlite3.connect(DB_NAME) as conn:
    cursor = conn.cursor()

    
    cursor.execute("SELECT * FROM client")
    main("Исходное состояние базы данных", cursor.fetchall())

    
    cursor.execute("SELECT * FROM client WHERE car_model LIKE 'Toyota%'")
    main("Поиск клиентов на машинах марки 'Toyota'", cursor.fetchall())

    
    cursor.execute("SELECT * FROM client WHERE total_sum <= 50000 AND rental_period > 5")
    main("Поиск проката дешевле 50000 и дольше 5 дней", cursor.fetchall())

    
    cursor.execute("SELECT * FROM client WHERE fio LIKE 'С%'")
    main("Поиск клиентов на букву 'С'", cursor.fetchall())

    
    cursor.execute("UPDATE client SET total_sum = 15000.00 WHERE client_id = 2")
    cursor.execute("UPDATE client SET total_sum = total_sum * 1.1 WHERE car_model = 'BMW X5'")
    cursor.execute("UPDATE client SET rental_period = rental_period - 1 WHERE client_id = 3 AND rental_period >= 1")
    
    conn.commit()

  
    cursor.execute("SELECT * FROM client")
    main("Состояние базы после редактирования", cursor.fetchall())

   
    cursor.execute("DELETE FROM client WHERE client_id = 1")
    cursor.execute("DELETE FROM client WHERE rental_period = 0")
    
    conn.commit()

    
    cursor.execute("SELECT * FROM client")
    main("Состояние базы после удаления", cursor.fetchall())
