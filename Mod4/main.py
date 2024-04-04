###Задание 1 Валидаторы. Добавление.
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Email, Length

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email format')])
    phone = IntegerField('Phone', validators=[InputRequired(), Length(min=10, max=10, message='Phone number must be 10 digits')])
    name = StringField('Name', validators=[InputRequired()])
    address = StringField('Address', validators=[InputRequired()])
    index = IntegerField('Index', validators=[InputRequired()])
    comment = StringField('Comment')
###Задание 2 Валидаторы. Создание
###1 вариант Использование валидатора на основе функций
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired, ValidationError

def number_length(min_length=None, max_length=None, message=None):
    def _number_length(form, field):
        if min_length is not None and len(str(field.data)) < min_length:
            raise ValidationError(message or f'Field must be at least {min_length} digits')
        if max_length is not None and len(str(field.data)) > max_length:
            raise ValidationError(message or f'Field cannot exceed {max_length} digits')
    return _number_length

class Number(FlaskForm):
    phone = IntegerField('Phone', validators=[InputRequired(), number_length(min_length=5, max_length=10, message='Invalid phone number')])

###2 вариант Использование валидатора на основе классов
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired, ValidationError

class NumberLength:
    def __init__(self, min_length=None, max_length=None, message=None):
        self.min_length = min_length
        self.max_length = max_length
        self.message = message

    def __call__(self, form, field):
        if self.min_length is not None and len(str(field.data)) < self.min_length:
            raise ValidationError(self.message or f'Field must be at least {self.min_length} digits')
        if self.max_length is not None and len(str(field.data)) > self.max_length:
            raise ValidationError(self.message or f'Field cannot exceed {self.max_length} digits')

class Number(FlaskForm):
    phone = IntegerField('Phone', validators=[InputRequired(), NumberLength(min_length=5, max_length=10, message='Invalid phone number')])

###Задание 3 Валидаторы. Тестирование
import unittest
from flask import Flask, request
from my_app import app # Импортируем наше Flask-приложение

class RegistrationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client() # Инициализируем тестовый клиент приложения

    def test_username_validator_pass(self):
        response = self.app.post('/registration', data={'username': 'valid_username'})
        self.assertEqual(response.status_code, 200) # Проверяем, что ответ сервера имеет статус 200
        self.assertIn(b'Success', response.data) # Проверяем наличие сообщения об успехе

    def test_username_validator_fail(self):
        response = self.app.post('/registration', data={'username': 'invalid username'})
        self.assertEqual(response.status_code, 400) # Проверяем, что ответ сервера имеет статус 400
        self.assertIn(b'Invalid username', response.data) # Проверяем наличие сообщения об ошибке

    def test_email_validator_pass(self):
        response = self.app.post('/registration', data={'email': 'valid_email@example.com'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Success', response.data)

    def test_email_validator_fail(self):
        response = self.app.post('/registration', data={'email': 'invalidemail'})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid email', response.data)

if __name__ == '__main__':
    unittest.main()

###Задание 4
from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/uptime')
def get_uptime():
    result = subprocess.run(['uptime'], capture_output=True, text=True)
    uptime = result.stdout.strip() # Получаем только значение uptime без лишней информации
    return f"current uptime is {uptime}"

if __name__ == '__main__':
    app.run()
