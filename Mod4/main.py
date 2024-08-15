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
    
###Задание 2 Валидаторы. Создание

