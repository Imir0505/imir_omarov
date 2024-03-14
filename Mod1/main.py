from flask import Flask
import random

app = Flask(__name__)

@app.route("/hello_world")
def hello_world():
    return "привет, мир!"

@app.route("/cars")
def cars():
    return "chevrolet, renault, ford, lada"

@app.route("/cats")
def cats():
    cat_breeds = ["Maine Coon", "Persian", "Siamese", "Sphynx", "British Shorthair"]
    random_breed = random.choice(cat_breeds)
    return f"Случайная порода кошек: {random_breed}"

@app.route("/get_time/now")
def get_time_now():
    current_time = "12:34" # Вставьте здесь функцию для получения текущего времени
    return f"Точное время {current_time}"

@app.route("/get_time/future")
def get_time_future():
    future_time = "13:34" # Вставьте здесь функцию для получения времени через час
    return f"Точное время через час будет {future_time}"

@app.route("/get_random_word")
def get_random_word():
    with open("war_and_peace.txt", "r") as f:
        words = f.read().split()
        random_word = random.choice(words)
    return random_word

if __name__ == "__main__":
    app.run()
