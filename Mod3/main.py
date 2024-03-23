###Задание 1 Хорошего дня!
import unittest
from freezegun import freeze_time
from your_module import get_weekday

class TestWeekdayFunction(unittest.TestCase):

"2022-03-22" # Замораживаем текущую дату на 22 марта 2022 года
def test_get_weekday(self):
    self.assertEqual(get_weekday(), "Вторник") # Проверяем корректность возвращаемого дня

"2022-03-23" # Замораживаем текущую дату на 23 марта 2022 года
def test_get_specific_weekday(self):
    self.assertEqual(get_weekday(), "Среда") # Проверяем корректность возвращаемого дня

"2022-03-24" # Замораживаем текущую дату на 24 марта 2022 года
def test_get_specific_weekday(self):
    self.assertEqual(get_weekday(),"Четверг") # Проверяем корректность возвращаемого дня
"2022-03-25" # Замораживаем текущую дату на 25 марта 2022 года
def test_get_specific_weekday(self):
    self.assertEqual(get_weekday(),"Пятница") # Проверяем корректность возвращаемого дня
"2022-03-26" # Замораживаем текущую дату на 26 марта 2022 года
def test_get_specific_weekday(self):
    self.assertEqual(get_weekday(),"Суббота") # Проверяем корректность возвращаемого дня
"2022-03-27" # Замораживаем текущую дату на 27 марта 2022 года
def test_get_specific_weekday(self):
    self.assertEqual(get_weekday(),"Воскресенье") # Проверяем корректность возвращаемого дня
"2022-03-28" # Замораживаем текущую дату на 28 марта 2022 года
def test_get_specific_weekday(self):
    self.assertEqual(get_weekday(),"Понедельник") # Проверяем корректность возвращаемого дня
if __name__ == '__main__':
    unittest.main()

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