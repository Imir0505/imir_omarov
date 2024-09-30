# Задача 1
from flask import Flask

app = Flask(__name__)

@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'

print("http://127.0.0.1:5000/hello_world")

if __name__ == '__main__':
    app.run(debug=True)

# Задача 2
from flask import Flask

app = Flask(__name__)

# Глобальный список машин
cars = ["Chevrolet", "Renault", "Ford", "Lada"]

@app.route('/cars')
def list_cars():
    return ', '.join(cars)

print("http://127.0.0.1:5000/cars")

if __name__ == '__main__':
    app.run(debug=True)

# Задача 3
from flask import Flask
import random

app = Flask(__name__)

# Список пород кошек в глобальной области видимости
cat_breeds = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]

@app.route('/cats')
def random_cat_breed():
    # Выбор случайной породы из списка
    breed = random.choice(cat_breeds)
    return f"<h1>Случайная порода кошки: {breed}</h1>"

print("http://127.0.0.1:5000/cats")

if __name__ == '__main__':
    app.run(debug=True)

# Задача 4
"Импорт библиотек"
from flask import Flask
from datetime import datetime

"Создание приложения"
app = Flask(__name__)

"Определение маршрута"
"декоратор, который связывает URL /get_time/now с функцией get_time."
@app.route('/get_time/now') 
def get_time():
    current_time = datetime.now().strftime('%H:%M:%S')  # Получаем текущее время в формате HH:MM:SS
    return f'Точное время: {current_time}'

print("http://127.0.0.1:5000/get_time/now")

"Запускается сервер"
if __name__ == '__main__':
    app.run(debug=True) #Режим откладки

# Задача 5
from flask import Flask
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/get_time/future')
def get_future_time():
    # Получаем текущее время
    current_time = datetime.now()
    # Добавляем один час с помощью timedelta
    future_time = current_time + timedelta(hours=1)
    # Форматируем время в виде HH:MM:SS
    current_time_after_hour = future_time.strftime('%H:%M:%S')
    # Возвращаем строку с будущим временем
    return f'Точное время через час будет {current_time_after_hour}'

print("http://127.0.0.1:5000/get_time/future")

if __name__ == '__main__':
    app.run(debug=True)

# Задача 6
from random import choice
from flask import Flask
import os
import re

app = Flask(__name__)

# Определяем  абсолютный путь к каталогу 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

def get_words_list():
    with open(BOOK_FILE, "r", encoding="utf-8") as file:
        text = file.read()
    words = re.findall(r"\b\w+\b", text)
    return words


WORDS_LIST = get_words_list()
@app.route("/get_random_word")
def get_random_word():
    return choice(WORDS_LIST)

print("http://127.0.0.1:5000/get_random_word")

if __name__ == "__main__":
    app.run(debug=True)

# Задача 7
from flask import Flask

app = Flask(__name__)

# Инициализация глобальной переменной для счетчика
counter = 0

@app.route('/counter')
def count_visits():
    global counter  # Указываем, что будем использовать глобальную переменную
    counter += 1
    return f'Страница была открыта {counter} раз(а)'

print("http://127.0.0.1:5000/counter")

if __name__ == '__main__':
    app.run(debug=True)
