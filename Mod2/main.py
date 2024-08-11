###Задание 1
def get_summary_rss(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()[1☺ # Пропускаем первую строку с заголовком
        total_bytes = 0

        for line in lines:
            columns = line.split()
            rss = int(columns[5]) # Получаем значение столбца rss

            total_bytes += rss

        units = ['б', 'кб', 'мб', 'гб']
        unit_index = 0

        while total_bytes >= 1024 and unit_index < len(units) - 1:
            total_bytes /= 1024
            unit_index += 1

        return f"{total_bytes} {units[unit_index]}"

if __name__ == "__main__":
    file_path = "output_file.txt"
    summary_rss = get_summary_rss(file_path)
    print(summary_rss)

###Задание 2
def get_mean_size(data):
    sizes = []
    for line in data:
        words = line.split()
        if len(words) >= 5:
            size = int(words[4])
            sizes.append(size)

    if sizes:
        mean_size = sum(sizes) / len(sizes)
        return mean_size

    return 0

###Задание 3
def decrypt(cipher):
    decrypted = []
    i = 0

    while i < len(cipher):
        if cipher[i].isalpha():
            decrypted.append(cipher[i])
            i += 1
        elif cipher[i:i+2] == '..':
            decrypted.pop()
            i += 2
        else:
            i += 1

    return ''.join(decrypted)

import sys

for line in sys.stdin:
    print(decrypt(line.strip()))

###Задание 4
from flask import Flask
from datetime import datetime

app = Flask(__name__)


def get_weekday_greeting(name: str) -> str:
    weekdays = (
        "понедельника",
        "вторника",
        "среды",
        "четверга",
        "пятницы",
        "субботы",
        "воскресенья"
    )
    weekday = datetime.today().weekday()
    if weekday in [2, 4, 5]:
        return f"Привет, {name}. Хорошей {weekdays[weekday]}!"
    return f"Привет, {name}. Хорошего {weekdays[weekday]}!"


@app.route('/hello-world/<name>')
def hello_world(name):
    return get_weekday_greeting(name)

print("http://127.0.0.1:5000/hello-world/Имир")

if __name__ == '__main__':
    app.run(debug=True)

###Задание 5
from flask import Flask

app = Flask(__name__)


@app.route('/max_number/<path:number_string>')
def max_number(number_string):
    numbers = number_string.split('/')

    # Проверка на то, что все элементы являются числами
    try:
        numbers = [int(num) for num in numbers]
    except ValueError:
        return "Ошибка: переданы не числа"

    max_num = max(numbers)

    return f"Максимальное переданное число: {max_num}"

print('http://127.0.0.1:5000/max_number/10/2/9/1')

if __name__ == '__main__':
    app.run()

###Задание 6
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

###Задание 7
from flask import Flask, jsonify
from collections import defaultdict

app = Flask(__name__)

storage = defaultdict(lambda: defaultdict(int))


@app.route('/add/<date>/<int:number>')
def add_expense(date, number):
    try:
        year = int(date[:4])
        month = int(date[4:6])
        day = int(date[6:])
        if len(date) > 8:
            raise ValueError
    except ValueError:
        return jsonify({'error': 'Неверный формат даты'}), 400

    storage[year][month] += number
    storage[year]['total'] += number

    return "Затраты добавлены."


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
