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
