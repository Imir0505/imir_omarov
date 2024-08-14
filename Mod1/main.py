from flask import Flask
import datetime
import random
import os
import re

app = Flask(__name__)

# Задача 2: Список машин
CARS = ['Chevrolet', 'Renault', 'Ford', 'Lada']

# Задача 3: Список пород кошек
CATS = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']

# Задача 6: Подготовка списка слов из книги "Война и мир"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

def get_words_from_book():
    if not hasattr(get_words_from_book, 'words'):
        with open(BOOK_FILE, 'r', encoding='utf-8') as book:
            text = book.read()
            # Используем регулярное выражение для извлечения слов без знаков препинания
            get_words_from_book.words = re.findall(r'\b\w+\b', text)
    return get_words_from_book.words

# Задача 7: Счётчик посещений
@app.route('/counter')
def counter():
    counter.visits += 1
    return f"Страница была открыта {counter.visits} раз(а)."

counter.visits = 0

# Задача 1: /hello_world
@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'

# Задача 2: /cars
@app.route('/cars')
def cars():
    return ', '.join(CARS)

# Задача 3: /cats
@app.route('/cats')
def cats():
    return random.choice(CATS)

# Задача 4: /get_time/now
@app.route('/get_time/now')
def get_time_now():
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"Точное время: {current_time}"

# Задача 5: /get_time/future
@app.route('/get_time/future')
def get_time_future():
    future_time = (datetime.datetime.now() + datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
    return f"Точное время через час будет {future_time}"

# Задача 6: /get_random_word
@app.route('/get_random_word')
def get_random_word():
    words = get_words_from_book()
    random_word = random.choice(words)
    return random_word

print("http://127.0.0.1:5000/get_time/now")
print("http://127.0.0.1:5000/get_time/future")
print("http://127.0.0.1:5000/counter")

if __name__ == '__main__':
    app.run(debug=True)
