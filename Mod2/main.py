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

def get_weekday_greeting():
    weekdays = {
        0: "понедельника”,
        1: "вторника”,
        2: "среды",
        3: "четверга”,
        4: "пятницы",
        5: "субботы",
        6: "воскресенья"
    }
    weekday = datetime.today().weekday()
    return f"Хорошего {weekdays.get(weekday)}!"

@app.route('/hello-world/<name>')
def hello_world(name)
    greeting = get_weekday_greeting()
    return f"Привет, {name}. {greeting}"

if __name__ == '__main__':
    app.run()

###Задание 5
from flask import Flask

app = Flask (__name__)

@app.route('/max_number/<path:number_string>')
def max_number (number_string):
    numbers = number_string.split('/')
    # Проверка на то, что все элементы являются числами
    try:
        numbers = [int(num) for num in numbers]
    except ValueError:
        return "Ошибка: переданы не числа"
        
    max_num = max(numbers)

    return f"Максимальное переданное число: {max_num}"

if __name__ == '__main__':
    app.run()

###Задание 6
from fask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/preview/<int:size>/<path:relative_path>')
def file_preview(size, relative_path):
    # Получаем абсолютный путь до файла
    abs_path = os.path.abspath(relative_path)

    # Читаем первые size символов из файла
    with open (abs_path, 'r') as file:
        content = file.read(size)
        content_size = len(content)

    return render_template('preview.html', abs_path=abs_path, content_size=content_size, content=content)

if __name__ == '__main__':
    app.run()
