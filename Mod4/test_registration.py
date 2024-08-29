import unittest
from main import app
from flask import json

class RegistrationFormTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()
        cls.app.testing = True

    def test_valid_registration(self):
        # Тестируем валидные данные
        response = self.app.post('/registration', data={
            'email': 'test@example.com',
            'phone': 1234567890,
            'name': 'John Doe',
            'address': '123 Main St',
            'index': 123456,
            'comment': 'This is a comment'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Registration successful', response.data)

    def test_invalid_email(self):
        # Тестируем некорректный email
        response = self.app.post('/registration', data={
            'email': 'invalid-email',
            'phone': 1234567890,
            'name': 'John Doe',
            'address': '123 Main St',
            'index': 123456,
            'comment': 'This is a comment'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid email format', response.data)

    def test_invalid_phone_length(self):
        # Тестируем некорректный номер телефона (менее 10 цифр)
        response = self.app.post('/registration', data={
            'email': 'test@example.com',
            'phone': 12345,  # Неправильная длина
            'name': 'John Doe',
            'address': '123 Main St',
            'index': 123456,
            'comment': 'This is a comment'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Phone number must be exactly 10 digits long.', response.data)

    def test_missing_name(self):
        # Тестируем отсутствие имени
        response = self.app.post('/registration', data={
            'email': 'test@example.com',
            'phone': 1234567890,
            'name': '',  # Пустое имя
            'address': '123 Main St',
            'index': 123456,
            'comment': 'This is a comment'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This field is required.', response.data)

    def test_invalid_index(self):
        # Тестируем некорректный индекс
        response = self.app.post('/registration', data={
            'email': 'test@example.com',
            'phone': 1234567890,
            'name': 'John Doe',
            'address': '123 Main St',
            'index': 'invalid-index',  # Неправильный индекс
            'comment': 'This is a comment'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Field must be of type integer.', response.data)

if __name__ == '__main__':
    unittest.main()
