# Задание 1
import sqlite3

# Создаем подключение к базе данных (если файла не существует, он будет создан)
conn = sqlite3.connect('homework.db')
cursor = conn.cursor()

# Создаем таблицу
cursor.execute("""
CREATE TABLE IF NOT EXISTS table_truck_with_vaccine (
    truck_number TEXT,
    timestamp DATETIME,
    temperature_in_celsius REAL
)
""")

# Вставляем тестовые данные
cursor.execute("""
INSERT INTO table_truck_with_vaccine (truck_number, timestamp, temperature_in_celsius)
VALUES 
    ('TRUCK_001', '2024-10-20 10:00:00', -19),
    ('TRUCK_001', '2024-10-20 11:00:00', -21),
    ('TRUCK_001', '2024-10-20 12:00:00', -15),
    ('TRUCK_002', '2024-10-20 13:00:00', -17),
    ('TRUCK_002', '2024-10-20 14:00:00', -18),
    ('TRUCK_002', '2024-10-20 15:00:00', -19)
""")

# Сохраняем изменения
conn.commit()

# Закрываем подключение
conn.close()

# Задание 2
import sqlite3

# Создаем подключение к базе данных (если файла не существует, он будет создан)
conn = sqlite3.connect('homework13.2.db')
cursor = conn.cursor()

# Создаем таблицу штрафов
cursor.execute("""
CREATE TABLE IF NOT EXISTS table_fees (
    truck_number TEXT,
    timestamp DATETIME,
    fine_amount REAL
)
""")

# Вставляем тестовые данные
cursor.execute("""
INSERT INTO table_fees (truck_number, timestamp, fine_amount)
VALUES 
    ('A619BC147', '2020-08-01T01:13:51', 500.0),
    ('B133XY48', '2020-08-01T06:36:27', 750.0),
    ('C180DE778', '2020-07-31T14:40:22', 1200.0),
    ('D357XY48', '2020-08-01T07:17:28', 800.0),
    ('E268XY11', '2020-08-01T09:17:07', 600.0),
    ('F799XY11', '2020-07-31T15:51:41', 900.0),
    ('G737XY777', '2020-07-31T15:25:53', 1100.0),
    ('H024BC147', '2020-08-01T03:12:44', 400.0),
    ('I838XY777', '2020-08-01T09:07:32', 500.0),
    ('J398BC147', '2020-08-01T03:38:46', 750.0)
""")

# Сохраняем изменения
conn.commit()

# Закрываем подключение
conn.close()
