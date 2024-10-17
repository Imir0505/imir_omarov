# Задание 1
import logging
import threading
import random
import time
from typing import List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Philosopher(threading.Thread):
    is_running = True

    def __init__(self, left_fork: threading.Lock, right_fork: threading.Lock) -> None:
        super().__init__()
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self) -> None:
        while self.is_running:
            logger.info(f"Philosopher {self.name} starts thinking.")
            time.sleep(random.randint(1, 10))
            logger.info(f"Philosopher {self.name} is hungry.")
            with self.left_fork, self.right_fork:
                logger.info(f"Philosopher {self.name} acquired forks.")
                self.dine()

    def dine(self) -> None:
        logger.info(f"Philosopher {self.name} starts eating.")
        time.sleep(random.randint(1, 10))
        logger.info(
            f"Philosopher {self.name} finishes eating and goes back to thinking."
        )


def main() -> None:
    forks: List[threading.Lock] = [threading.Lock() for _ in range(5)]
    philosophers: List[Philosopher] = [
        Philosopher(forks[i % 5], forks[(i + 1) % 5]) for i in range(5)
    ]
    Philosopher.is_running = True
    for philosopher in philosophers:
        philosopher.start()
    time.sleep(200)
    Philosopher.is_running = False
    logger.info("Program finished.")


if __name__ == "__main__":
    main()

# Задание 2
import requests
import sqlite3
import time
from concurrent.futures import ThreadPoolExecutor


def fetch_character_data(character_url):
    response = requests.get(character_url)
    if response.status_code == 200:
        data = response.json()
        character_data = {
            "name": data["name"],
            "age": data["birth_year"],
            "gender": data["gender"],
        }
        return character_data
    else:
        return None


def store_character_data(character_data):
    if character_data:
        conn = sqlite3.connect("characters.db")
        c = conn.cursor()
        insert_query = "INSERT INTO characters (name, age, gender) VALUES (?, ?, ?)"
        c.execute(
            insert_query,
            (character_data["name"], character_data["age"], character_data["gender"]),
        )
        conn.commit()
        conn.close()


def initialize_database():
    conn = sqlite3.connect("characters.db")
    c = conn.cursor()
    create_table_query = (
        "CREATE TABLE IF NOT EXISTS characters (name TEXT, age TEXT, gender TEXT)"
    )
    c.execute(create_table_query)
    conn.commit()
    conn.close()


# 1. Функция для последовательной загрузки данных (без потоков)
def download_characters_sequential():
    character_urls = [f"https://swapi.dev/api/people/{i}/" for i in range(1, 21)]
    characters = []
    for url in character_urls:
        character_data = fetch_character_data(url)
        if character_data:
            characters.append(character_data)
            store_character_data(character_data)
    return characters


# 2. Функция для параллельной загрузки данных (с потоками)
def download_characters_parallel():
    character_urls = [f"https://swapi.dev/api/people/{i}/" for i in range(1, 21)]
    characters = []
    with ThreadPoolExecutor() as executor:
        results = executor.map(fetch_character_data, character_urls)
        for result in results:
            if result:
                characters.append(result)
                store_character_data(result)
    return characters


# Функция для замера времени выполнения
def measure_execution_time(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print(f"Execution time for {func.__name__}: {end_time - start_time:.2f} seconds")


def main():
    initialize_database()

    # 3. Замер времени для последовательной загрузки
    print("Sequential download:")
    measure_execution_time(download_characters_sequential)

    # 4. Замер времени для параллельной загрузки
    print("\nParallel download:")
    measure_execution_time(download_characters_parallel)


if __name__ == "__main__":
    main()



