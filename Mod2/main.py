# Задание 1
# Использование команд на Linux
from typing import List


def get_summary_rss(file_path: str) -> str:
    with open(file_path, 'r') as file:
        lines: List[str] = file.readlines()[1:]

    total_bytes: int = 0

    for line in lines:
        columns: List[str] = line.split()
        rss: int = int(columns[5])
        total_bytes += rss

    def format_bytes(bytes_: int) -> str:
        for unit in ['Б', 'Кб', 'Мб', 'Гб']:
            if bytes_ < 1024:
                return f"{bytes_} {unit}"
            bytes_ /= 1024
        return f"{bytes_} Тб"

    return format_bytes(total_bytes)


if __name__ == "__main__":
    file_path: str = "task2.1.txt"
    print(get_summary_rss(file_path))

# Задание 4
from flask import Flask
from datetime import datetime

app = Flask(__name__)

"Функция принимает строку name и возвращает приветственное сообщение в зависимости от дня недели"
def get_weekday_greeting(name: str) -> str:
    "Кортеж weekdays содержит названия дней недели"
    weekdays = (
        "понедельника",
        "вторника",
        "среды",
        "четверга",
        "пятницы",
        "субботы",
        "воскресенья"
    )
    "Метод weekday() возвращает номер текущего дня недели"
    weekday = datetime.today().weekday()
    if weekday in [2, 4, 5]:
        return f"Привет, {name}. Хорошей {weekdays[weekday]}!"
    return f"Привет, {name}. Хорошего {weekdays[weekday]}!"

#Декоратор связывает URL /hello-world/<name> с функцией hello_world, которая принимает параметр name. 
#Эта функция вызывает get_weekday_greeting и возвращает полученное сообщение
@app.route('/hello-world/<name>')
def hello_world(name):
    return get_weekday_greeting(name)

print("http://127.0.0.1:5000/hello-world/%D0%98%D0%B2%D0%B0%D0%BD")

if __name__ == '__main__':
    app.run(debug=True)

# Задание 5
from flask import Flask
from typing import List

app = Flask(__name__)


@app.route('/max_number/<path:number_string>')
def max_number(number_string: str):
    numbers: List[int] = [int(num) for num in number_string.split('/') if num.isdigit()]

    if numbers:
        max_num: int = max(numbers)
        return f"Максимальное число: {max_num}"
    else:
        return "Неверный формат чисел в запросе."


if __name__ == '__main__':
    app.run(debug=True)

# Задание 6
from flask import Flask
import os

app = Flask(__name__)


@app.route('/preview/<int:size>/<path:relative_path>')
def preview(size, relative_path):
    abs_path = os.path.abspath(relative_path)

    try:
        with open(abs_path, 'r') as file:
            content = file.read(size)
            result_size = len(content)
            file_info = f"<b>{abs_path}</b> {result_size}<br>"
            return f"{file_info}\n{content}"
    except FileNotFoundError:
        return "Файл не найден."

print("http://127.0.0.1:5000/preview/5/task2.6_file.txt")

if __name__ == '__main__':
    app.run(debug=True)

# Задание 7
from flask import Flask, jsonify
from collections import defaultdict

app = Flask(__name__)

#Используется defaultdict для автоматического создания вложенных словарей:
storage = defaultdict(lambda: defaultdict(int))

#Этот маршрут позволяет добавлять затраты по дате и сумме:
@app.route('/add/<date>/<int:number>')
def add_expense(date, number):
    #Проверка формата даты:
    try:
        year = int(date[:4])
        month = int(date[4:6])
        day = int(date[6:])
        if len(date) > 8:
            raise ValueError
    except ValueError:
        return jsonify({'error': 'Неверный формат даты'}), 400
        
    #Добавление затрат в хранилище:
    storage[year][month] += number
    storage[year]['total'] += number

    return "Затраты добавлены."

#Маршруты для расчета затрат:
@app.route('/calculate/<int:year>')
def calculate_year(year):
    if year in storage:
        return f"Суммарные траты за {year} год: {storage[year]['total']}"
    else:
        return "Нет данных о затратах за указанный год."


@app.route('/calculate/<int:year>/<int:month>')
def calculate_month(year, month):
    if year in storage and month in storage[year]:
        return f"Суммарные траты за {month}.{year}: {storage[year][month]}"
    else:
        return "Нет данных о затратах за указанный месяц."

print("http://127.0.0.1:5000/add/20240705/300")
print("http://127.0.0.1:5000/calculate/2024")
print("http://127.0.0.1:5000/calculate/2024/7")

if __name__ == '__main__':
    app.run(debug=True)
