# Задача 4
"Импорт библиотек"
from flask import Flask
from datetime import datetime

"Создание приложения"
app = Flask(__name__)

"Определение маршрута"
"декоратор, который связывает URL /get_time/now с функцией get_time."
@app.route('/get_time/now') 
def get_time():
    current_time = datetime.now().strftime('%H:%M:%S')  # Получаем текущее время в формате HH:MM:SS
    return f'Точное время: {current_time}'

print("http://127.0.0.1:5000/get_time/now")

"Запускается сервер"
if __name__ == '__main__':
    app.run(debug=True) #Режим откладки

# Задача 5
from flask import Flask
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/get_time/future')
def get_future_time():
    # Получаем текущее время
    current_time = datetime.now()
    # Добавляем один час с помощью timedelta
    future_time = current_time + timedelta(hours=1)
    # Форматируем время в виде HH:MM:SS
    current_time_after_hour = future_time.strftime('%H:%M:%S')
    # Возвращаем строку с будущим временем
    return f'Точное время через час будет {current_time_after_hour}'

print("http://127.0.0.1:5000/get_time/future")

if __name__ == '__main__':
    app.run(debug=True)

# Задача 7
from flask import Flask

app = Flask(__name__)

# Инициализация глобальной переменной для счетчика
counter = 0

@app.route('/counter')
def count_visits():
    global counter  # Указываем, что будем использовать глобальную переменную
    counter += 1
    return f'Страница была открыта {counter} раз(а)'

print("http://127.0.0.1:5000/counter")

if __name__ == '__main__':
    app.run(debug=True)
