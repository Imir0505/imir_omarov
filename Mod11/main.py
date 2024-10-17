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

# Задание 3
import logging
import random
import threading
import time
from typing import List

TOTAL_TICKETS: int = 10

logging.basicConfig(level=logging.INFO)
logger: logging.Logger = logging.getLogger(__name__)


class Seller(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore, cv: threading.Condition) -> None:
        super().__init__()
        self.sem: threading.Semaphore = semaphore
        self.cv: threading.Condition = cv
        self.tickets_sold: int = 0
        logger.info("Seller started work")

    def run(self) -> None:
        global TOTAL_TICKETS
        while True:
            self._work()
            with self.sem:
                if TOTAL_TICKETS <= 0:
                    break
                self._sell_ticket()
                self._notify_director_if_needed()

    def _work(self) -> None:
        self._random_sleep()

    def _sell_ticket(self) -> None:
        global TOTAL_TICKETS
        self.tickets_sold += 1
        TOTAL_TICKETS -= 1
        logger.info(f"{self.name} sold one; {TOTAL_TICKETS} left")

    def _notify_director_if_needed(self) -> None:
        global TOTAL_TICKETS
        if TOTAL_TICKETS <= 1:
            with self.cv:
                self.cv.notify_all()

    def _random_sleep(self) -> None:
        time.sleep(random.randint(0, 1))


class Director(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore, cv: threading.Condition) -> None:
        super().__init__()
        self.sem: threading.Semaphore = semaphore
        self.cv: threading.Condition = cv

    def run(self) -> None:
        while True:
            with self.cv:
                self.cv.wait()
                if self._need_more_tickets():
                    self._add_tickets()
                    self._release_tickets()

    def _need_more_tickets(self) -> bool:
        global TOTAL_TICKETS
        return TOTAL_TICKETS <= 1

    def _add_tickets(self) -> None:
        global TOTAL_TICKETS
        added_tickets = random.randint(1, 10)
        logger.info(f"Director added {added_tickets} tickets")
        TOTAL_TICKETS += added_tickets

    def _release_tickets(self) -> None:
        with self.sem:
            self.sem.release()


def main() -> None:
    semaphore: threading.Semaphore = threading.Semaphore()
    condition_variable: threading.Condition = threading.Condition()
    sellers: List[Seller] = []
    for _ in range(3):
        seller = Seller(semaphore, condition_variable)
        seller.start()
        sellers.append(seller)

    director = Director(semaphore, condition_variable)
    director.start()

    for seller in sellers:
        seller.join()

    director.join()


if __name__ == "__main__":
    main()

# Задание 4
import threading
import time
from queue import PriorityQueue


class Producer(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        print("Producer: Running")
        tasks = self._generate_tasks()
        self._put_tasks(tasks)
        print("Producer: Done")

    def _generate_tasks(self):
        return [
            (0, "Task(priority=0)."),
            (2, "Task(priority=2)."),
            (1, "Task(priority=1)."),
            (4, "Task(priority=4)."),
            (3, "Task(priority=3)."),
            (6, "Task(priority=6)."),
        ]

    def _put_tasks(self, tasks):
        for priority, task in tasks:
            self.queue.put((priority, task))
            time.sleep(0.5)


class Consumer(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        print("Consumer: Running")
        self._consume_tasks()
        print("Consumer: Done")

    def _consume_tasks(self):
        while True:
            priority, task = self.queue.get()
            if task is None:
                self.queue.task_done()
                break
            self._process_task(priority, task)
            self.queue.task_done()

    def _process_task(self, priority, task):
        print(f">{task}          sleep({priority * 0.1})")
        time.sleep(priority * 0.1)


def main():
    queue = PriorityQueue()
    producer = Producer(queue)
    consumer = Consumer(queue)

    producer.start()
    consumer.start()

    producer.join()
    queue.put((None, None))
    queue.join()
    consumer.join()


if __name__ == "__main__":
    main()



