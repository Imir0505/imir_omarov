###Задание 1 
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Email, NumberRange, Optional

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'


# Форма регистрации
class RegistrationForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            InputRequired(message='Email обязателен для заполнения'),
            Email(message='Неверный формат email')
        ]
    )
    phone = IntegerField(
        'Phone',
        validators=[
            InputRequired(message='Телефон обязателен для заполнения'),
            NumberRange(min=1000000000, max=9999999999, message='Телефон должен быть десятизначным положительным числом')
        ]
    )
    name = StringField(
        'Name',
        validators=[InputRequired(message='Имя обязательно для заполнения')]
    )
    address = StringField(
        'Address',
        validators=[InputRequired(message='Адрес обязателен для заполнения')]
    )
    index = IntegerField(
        'Index',
        validators=[InputRequired(message='Индекс обязателен для заполнения')]
    )
    comment = TextAreaField(
        'Comment',
        validators=[Optional()]  # Поле необязательно для заполнения
    )


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Обработка данных формы
        return redirect(url_for('success'))

    return render_template('registration.html', form=form)


@app.route('/success')
def success():
    return 'Регистрация прошла успешно!'

print("http://127.0.0.1:5000/registration")

if __name__ == '__main__':
    app.run(debug=True)
    
###Задание 2 
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired, Email, ValidationError
from typing import Optional

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Валидатор как функция
def number_length(min_length: int, max_length: int, message: Optional[str] = None):
    def _number_length(form: FlaskForm, field: IntegerField):
        number = field.data
        if number is not None:
            if not (min_length <= len(str(number)) <= max_length):
                raise ValidationError(message or f'Number must be between {min_length} and {max_length} digits long.')
    return _number_length

# Валидатор как класс
class NumberLength:
    def __init__(self, min_length: int, max_length: int, message: Optional[str] = None):
        self.min_length = min_length
        self.max_length = max_length
        self.message = message

    def __call__(self, form: FlaskForm, field: IntegerField):
        number = field.data
        if number is not None:
            if not (self.min_length <= len(str(number)) <= self.max_length):
                raise ValidationError(
                    self.message or f'Number must be between {self.min_length} and {self.max_length} digits long.')

# Форма с использованием валидаторов
class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message="Invalid email format")])
    phone = IntegerField('Phone (Function Validator)',
                         validators=[InputRequired(), number_length(7, 10, 'Phone number must be between 7 and 10 digits long.')])
    phone2 = IntegerField('Phone (Class Validator)',
                          validators=[InputRequired(), NumberLength(7, 10, 'Phone number must be between 7 and 10 digits long.')])
    name = StringField('Name', validators=[InputRequired()])
    address = StringField('Address', validators=[InputRequired()])
    index = IntegerField('Index', validators=[InputRequired()])
    comment = StringField('Comment (optional)')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        return f"Form submitted successfully! {form.data}"
    return render_template('registration.html', form=form)

print("http://127.0.0.1:5000/registration")

if __name__ == '__main__':
    app.run(debug=True)
    
###Задание 3
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired, Email, ValidationError
from typing import Optional

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Валидатор как функция
def number_length(min_length: int, max_length: int, message: Optional[str] = None):
    def _number_length(form: FlaskForm, field: IntegerField):
        number = field.data
        if number is not None:
            if not (min_length <= len(str(number)) <= max_length):
                raise ValidationError(message or f'Number must be between {min_length} and {max_length} digits long.')
    return _number_length

# Валидатор как класс
class NumberLength:
    def __init__(self, min_length: int, max_length: int, message: Optional[str] = None):
        self.min_length = min_length
        self.max_length = max_length
        self.message = message

    def __call__(self, form: FlaskForm, field: IntegerField):
        number = field.data
        if number is not None:
            if not (self.min_length <= len(str(number)) <= self.max_length):
                raise ValidationError(
                    self.message or f'Number must be between {self.min_length} and {self.max_length} digits long.')

# Форма с использованием валидаторов
class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message="Invalid email format")])
    phone = IntegerField('Phone (Function Validator)',
                         validators=[InputRequired(), number_length(7, 10, 'Phone number must be between 7 and 10 digits long.')])
    phone2 = IntegerField('Phone (Class Validator)',
                          validators=[InputRequired(), NumberLength(7, 10, 'Phone number must be between 7 and 10 digits long.')])
    name = StringField('Name', validators=[InputRequired()])
    address = StringField('Address', validators=[InputRequired()])
    index = IntegerField('Index', validators=[InputRequired()])
    comment = StringField('Comment (optional)')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        return f"Form submitted successfully! {form.data}"
    return render_template('registration.html', form=form)

print("http://127.0.0.1:5000/registration")
#python -m unittest test_registration.py

if __name__ == '__main__':
    app.run(debug=True)
