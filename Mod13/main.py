# Задание 1
import sqlite3

sql_query = """SELECT * FROM 'table_truck_with_vaccine'
WHERE temperature_in_celsius NOT BETWEEN 16 AND 20 AND truck_number = ? ORDER BY timestamp
"""


def check_if_vaccine_has_spoiled(cursor: sqlite3.Cursor, truck_number: str) -> bool:
    cursor.execute(sql_query, (truck_number,))
    results = cursor.fetchall()
    print(results)
    return len(results) >= 3


if __name__ == "__main__":
    with sqlite3.connect("homework.db") as conn:
        cursor = conn.cursor()
        truck_number = input("Enter the truck number:\n")
        if check_if_vaccine_has_spoiled(cursor, truck_number):
            print("The vaccine has spoiled")
        else:
            print("The vaccine has NOT spoiled")

# Задание 2
import sqlite3
import csv

sql_query = """ DELETE FROM 'table_fees'
WHERE truck_number = ? AND timestamp = ?
"""


def delete_wrong_fees(cursor: sqlite3.Cursor, wrong_fees_file: str) -> None:
    with open(wrong_fees_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            cursor.execute(sql_query, (row[0], row[1]))


if __name__ == "__main__":
    with sqlite3.connect("homework13.2.db") as conn:
        cursor = conn.cursor()
        delete_wrong_fees(cursor, "wrong_fees.csv")

# Задание 3
import datetime
import sqlite3

check_availability_query = """
SELECT EXISTS(SELECT * FROM 'birds' WHERE bird_name = ?)
"""

add_bird_query = """ 
INSERT INTO 'birds' (bird_name, time) VALUES (?, ?);
"""


def log_bird(cursor: sqlite3.Cursor, bird_name: str, date_time: str) -> None:
    cursor.execute(add_bird_query, (bird_name, date_time))
    print(f"Bird '{bird_name}' logged.")


def check_if_such_bird_already_seen(cursor: sqlite3.Cursor, bird_name: str) -> bool:
    cursor.execute(check_availability_query, (bird_name,))
    result = cursor.fetchone()
    return result[0]


if __name__ == "__main__":
    with sqlite3.connect("homework.db") as conn:
        cursor = conn.cursor()
        bird_name = input("Enter the bird's name:\n").lower()
        if not check_if_such_bird_already_seen(cursor, bird_name):
            log_bird(cursor, bird_name, str(datetime.datetime.now().time()))
        else:
            print(f"{bird_name} is already logged.")
