import sqlite3

DB_NAME = "car_rental.db"


def insert_data():
    initial_clients = [
        ("Иванов И.И.", "Toyota Camry", 5, 25000.00, "да"),
        ("Петров П.П.", "Hyundai Solo", 3, 12000.00, "нет"),
        ("Сидоров С.С.", "Kia Rio", 10, 30000.00, "да"),
        ("Смирнов А.А.", "Toyota RAV4", 7, 42000.00, "нет"),
        ("Кузнецов В.В.", "BMW X5", 2, 20000.00, "да"),
        ("Попов М.М.", "Mercedes E-Class", 0, 0.00, "нет"),
        ("Васильев К.К.", "Audi A6", 4, 24000.00, "да"),
        ("Соколов Д.Д.", "Porsche Cayenne", 12, 180000.00, "да"),
        ("Михайлов Е.Е.", "Skoda Octavia", 6, 18000.00, "нет"),
        ("Новиков Н.Н.", "Toyota Corolla", 14, 42000.00, "да")
    ]

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM client")
        if cursor.fetchone()[0] == 0:
            
            cursor.executemany("""
                INSERT INTO client (fio, car_model, rental_period, total_sum, prepayment)
                VALUES (?, ?, ?, ?, ?)
            """, initial_clients)
            
            conn.commit()
