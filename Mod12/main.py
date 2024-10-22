# Задание 1
import requests
import sqlite3
import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool


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


def save_character_data_to_db(character_data):
    if character_data:
        conn = sqlite3.connect("characters.db")
        c = conn.cursor()
        c.execute(
            "INSERT INTO characters (name, age, gender) VALUES (?, ?, ?)",
            (character_data["name"], character_data["age"], character_data["gender"]),
        )
        conn.commit()
        conn.close()


def create_database_if_not_exists():
    conn = sqlite3.connect("characters.db")
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS characters (name TEXT, age TEXT, gender TEXT)"
    )
    conn.commit()
    conn.close()


def download_characters_with_thread_pool():
    characters = []
    character_urls = [f"https://swapi.dev/api/people/{i}/" for i in range(1, 21)]

    with ThreadPoolExecutor() as executor:
        results = executor.map(fetch_character_data, character_urls)

        for result in results:
            characters.append(result)
            save_character_data_to_db(result)

    return characters


def download_characters_with_process_pool():
    characters = []
    character_urls = [f"https://swapi.dev/api/people/{i}/" for i in range(1, 21)]

    with Pool() as pool:
        results = pool.map(fetch_character_data, character_urls)

        for result in results:
            characters.append(result)
            save_character_data_to_db(result)

    return characters


def measure_time_execution(func, pool_type):
    start_time = time.time()
    func()
    end_time = time.time()
    print(f"Execution time ({pool_type}): {end_time - start_time} seconds")


def main():
    create_database_if_not_exists()
    measure_time_execution(download_characters_with_thread_pool, "ThreadPoolExecutor")
    measure_time_execution(download_characters_with_process_pool, "Pool")


if __name__ == "__main__":
    main()

# Задание 3
from threading import Semaphore, Thread
import time

semaphore = Semaphore()
exit_flag = False


def worker_1():
    global exit_flag
    while not exit_flag:
        semaphore.acquire()
        print(1)
        semaphore.release()
        time.sleep(0.25)


def worker_2():
    global exit_flag
    while not exit_flag:
        semaphore.acquire()
        print(2)
        semaphore.release()
        time.sleep(0.25)


# Используйте флаг для завершения потоков при нажатии Ctrl+C
def signal_handler():
    global exit_flag
    exit_flag = True
    print("\nKeyboard interrupt, quit.")


if __name__ == "__main__":
    try:
        thread_1 = Thread(target=worker_1)
        thread_2 = Thread(target=worker_2)

        thread_1.start()
        thread_2.start()

        while True:  # Основной цикл, ожидающий завершения потоков
            time.sleep(1)  # Ожидание 1 секунду
    except KeyboardInterrupt:
        signal_handler()  # Обработка нажатия Ctrl+C
    finally:
        # Ожидание завершения потоков
        thread_1.join()
        thread_2.join()
        print("Threads have been joined, exiting program.")

# Задание 4
# Сперва нужно запустить сервер, а затем основную программу
import requests
import time
from threading import Thread, Lock
from queue import Queue

log_lock = Lock()
task_queue = Queue()

def fetch_timestamp_from_server(timestamp):
    response = requests.get(f"http://127.0.0.1:8080/timestamp/{timestamp}")
    if response.status_code == 200:
        return response.text
    else:
        return None

def write_log_entry(timestamp, date):
    log_line = f"{timestamp} {date}"
    with log_lock:
        with open("logs.txt", "a") as file:
            file.write(log_line + "\n")

def worker_thread():
    while True:
        timestamp = task_queue.get()
        if timestamp is None:
            break
        current_timestamp = time.time()
        date = fetch_timestamp_from_server(current_timestamp)
        if date is None:
            break
        write_log_entry(current_timestamp, date)
        time.sleep(1)
        task_queue.task_done()

if __name__ == "__main__":
    start_timestamp = int(time.time())
    threads = []
    for i in range(10):
        task_queue.put(start_timestamp + i)

    for _ in range(10):
        thread = Thread(target=worker_thread)
        thread.start()
        threads.append(thread)

    task_queue.join()

    for _ in range(10):
        task_queue.put(None)

    for thread in threads:
        thread.join()




