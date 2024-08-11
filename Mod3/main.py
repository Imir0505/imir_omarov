###Задание 1 Хорошего дня!
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

print("http://127.0.0.1:5000/hello-world/%D0%98%D0%B2%D0%B0%D0%BD")

if __name__ == '__main__':
    app.run(debug=True)

###Задание 2 Дешифратор
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
