###Задание 4
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

###Задание 5
from flask import Flask

app = Flask(__name__)

#Декоратор связывает URL /max_number/<path:number_string> с функцией max_number, которая принимает параметр number_string. 
#Использование <path:...> позволяет передавать строки, содержащие символы /.
@app.route('/max_number/<path:number_string>')
def max_number(number_string):
    "Метод split('/') разбивает строку number_string на список подстрок по символу /"
    numbers = number_string.split('/')

    # Проверка на то, что все элементы являются числами
    try: #В блоке try происходит попытка преобразовать каждую подстроку в целое число
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

#Декоратор связывает URL /preview/<int:size>/<path:relative_path> с функцией preview, 
#которая принимает два параметра: size (целое число) и relative_path (строка, представляющая относительный путь к файлу)
@app.route('/preview/<int:size>/<path:relative_path>')
def preview(size, relative_path):
    #Получение абсолютного пути к файлу:
    abs_path = os.path.abspath(relative_path)
    #Чтение файла:
    try:
        with open(abs_path, 'r') as file:
            content = file.read(size)
            result_size = len(content)
            file_info = f"<b>{abs_path}</b> {result_size}<br>"
            return f"{file_info}\n{content}"
    except FileNotFoundError:
        return "Файл не найден."

print("http://127.0.0.1:5000/preview/5/task2.6_file.txt")
#Этот код создает веб-приложение Flask, которое позволяет пользователям запрашивать определенное количество символов из указанного файла по относительному пути. 
#Если файл не найден, приложение возвращает соответствующее сообщение об ошибке.
if __name__ == '__main__':
    app.run(debug=True)

###Задание 7
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
