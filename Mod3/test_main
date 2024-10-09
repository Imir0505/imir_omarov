###Задание 1 
import unittest
from freezegun import freeze_time
from main import app


class TestHelloWorldEndpoint(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/hello-world/'

    @freeze_time("2024-03-14")
    def test_hello_world_with_name_thursday(self):
        response = self.app.get('/hello-world/Alice')
        text = response.data.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Alice. Хорошего четверга!', text)

    @freeze_time("2024-03-15")
    def test_hello_world_with_name_friday(self):
        response = self.app.get('/hello-world/Bob')
        text = response.data.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Bob. Хорошей пятницы!', text)

    @freeze_time("2024-03-16")
    def test_hello_world_without_name_saturday(self):
        response = self.app.get('/hello-world/Alex')
        text = response.data.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Alex. Хорошей субботы!', text)

    @freeze_time("2024-03-17")
    def test_hello_world_without_name_sunday(self):
        response = self.app.get('/hello-world/Alex')
        text = response.data.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Alex. Хорошего воскресенья!', text)

    @freeze_time("2024-03-18")
    def test_hello_world_without_name_monday(self):
        response = self.app.get('/hello-world/Alex')
        text = response.data.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Alex. Хорошего понедельника!', text)

    @freeze_time("2024-03-19")
    def test_hello_world_without_name_tuesday(self):
        response = self.app.get('/hello-world/Alex')
        text = response.data.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Alex. Хорошего вторника!', text)

    @freeze_time("2024-03-20")
    def test_hello_world_without_name_wednesday(self):
        response = self.app.get('/hello-world/Alex')
        text = response.data.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Alex. Хорошей среды!', text)

    @freeze_time("2024-03-20")
    def test_hello_world_without_name_correct(self):
        response = self.app.get('/hello-world/Хорошей среды')
        text = response.data.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn('Привет, Хорошей среды. Хорошей среды!', text)

if __name__ == '__main__':
    unittest.main()

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
