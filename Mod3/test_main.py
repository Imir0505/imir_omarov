# Запуск тестов:
# python -m unittest test_main.py
# Задание 1
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

# Задание 3
import unittest
from main import app


class TestFinanceApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        cls.app = app.test_client()
        cls.storage = {
            2022: {
                1: {
                    1: 100,
                    2: 150
                },
                'total': 250
            }
        }

    def test_add_expense(self):
        response = self.app.get('/add/20220103/50')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Затраты добавлены.')

    def test_calculate_year(self):
        response = self.app.get('/calculate/2022')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Суммарные траты за 2022 год: 300')

    def test_calculate_month(self):
        response = self.app.get('/calculate/2022/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Суммарные траты за 1.2022: 300')

    def test_invalid_date_format(self):
        response = self.app.get('/add/202201/50')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Неверный формат даты')

    def test_empty_storage_year(self):
        response = self.app.get('/calculate/2023')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Нет данных о затратах за указанный год.')

    def test_empty_storage_month(self):
        response = self.app.get('/calculate/2022/2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Нет данных о затратах за указанный месяц.')


if __name__ == '__main__':
    unittest.main()

# Задание 4
import unittest
from datetime import datetime
from main import Person


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person = Person('John', 1990, '123 Main St')

    def test_get_age(self):
        current_year = datetime.now().year
        expected_age = current_year - 1990
        self.assertEqual(self.person.get_age(), expected_age)

    def test_get_name(self):
        self.assertEqual(self.person.get_name(), 'John')

    def test_set_name(self):
        self.person.set_name('Jane')
        self.assertEqual(self.person.get_name(), 'Jane')

    def test_set_address(self):
        self.person.set_address('456 Elm St')
        self.assertEqual(self.person.get_address(), '456 Elm St')

    def test_get_address(self):
        self.assertEqual(self.person.get_address(), '123 Main St')

    def test_is_homeless(self):
        self.assertFalse(self.person.is_homeless())

    def test_is_homeless_when_address_not_set(self):
        homeless_person = Person('Homeless', 1980)
        self.assertTrue(homeless_person.is_homeless())


if __name__ == '__main__':
    unittest.main()
