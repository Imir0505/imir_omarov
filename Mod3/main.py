###Задание 1 
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


if __name__ == '__main__':
    app.run(debug=True)

###Задание 2 
import unittest
from decoder import decode

class TestDecoder(unittest.TestCase):

    def test_decode_empty(self):
        with self.subTest(decoded_string=""):
            self.assertEqual(decode(""), "")

    def test_decode_single_chars(self):
        test_cases = {
            "abracadabra": "абра-кадабра",
            "abra--..kadabra": "абра-кадабра",
            "abraу...-kadabra": "абра-кадабра",
            "abra......a.": "a",
            "1..2.3": "23",
            ".": ""
        }
        for encoded, expected in test_cases.items():
            with self.subTest(decoded_string=encoded):
                self.assertEqual(decode(encoded), expected)

    def test_decode_multiple_chars(self):
        test_cases = {
            "abraa..-кадабра": "абра-кадабра",
            "abraa..-.кадабра": "абра-кадабра",
            "1.......................": ""
        }
        for encoded, expected in test_cases.items():
            with self.subTest(decoded_string=encoded):
                self.assertEqual(decode(encoded), expected)

if __name__ == '__main__':
    unittest.main()

###Задание 3 
from flask import Flask, jsonify
from collections import defaultdict

app = Flask(__name__)

storage = defaultdict(lambda: defaultdict(int))
storage[2022][1] = 250
storage[2022]['total'] += 250


@app.route('/add/<date>/<int:number>')
def add_expense(date, number):
    try:
        year = int(date[:4])
        month = int(date[4:6])
        day = int(date[6:])
        if len(date) > 8:
            raise ValueError
    except ValueError:
        return 'Неверный формат даты'

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

###Задание 4
import datetime


class Person:
    def __init__(self, name, year_of_birth, address=''):
        self.name = name
        self.yob = year_of_birth
        self.address = address

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.yob

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def is_homeless(self):
        '''
        returns True if address is not set, false in other case
        '''
        return self.address is ""
