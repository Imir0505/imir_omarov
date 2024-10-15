# Задание 3
import logging


def create_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Обработчик для логов уровня DEBUG
    debug_handler = logging.FileHandler("calc_debug.log", encoding='utf-8')
    debug_handler.setLevel(logging.DEBUG)
    debug_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    debug_handler.setFormatter(debug_formatter)

    # Обработчик для логов уровня ERROR
    error_handler = logging.FileHandler("calc_error.log", encoding='utf-8')
    error_handler.setLevel(logging.ERROR)
    error_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    error_handler.setFormatter(error_formatter)

    # Добавляем обработчики в логгер
    logger.addHandler(debug_handler)
    logger.addHandler(error_handler)

    return logger


def calculate_operation(s, x, y):
    logger = logging.getLogger('main')
    logger.info(f"Начата операция: {s}, с числами {x} и {y}")

    if s == '+':
        return x + y
    elif s == '-':
        return x - y
    elif s == '*':
        return x * y
    elif s == '/':
        if y != 0:
            return x / y
        else:
            logger.error("Попытка деления на ноль")
            print("Деление на ноль!")
            return None
    else:
        logger.error(f"Некорректная операция: {s}")
        return None

# Задание 4
import logging
import logging.config
from dict_config import dict_config  # импортируем конфигурацию


def create_logger(name):
    # Применяем конфигурацию логгера через словарь
    logging.config.dictConfig(dict_config)

    # Возвращаем сконфигурированный логгер
    logger = logging.getLogger(name)

    return logger


def calculate_operation(s, x, y):
    logger = logging.getLogger('main')
    logger.info(f"Начата операция: {s}, с числами {x} и {y}")

    if s == '+':
        return x + y
    elif s == '-':
        return x - y
    elif s == '*':
        return x * y
    elif s == '/':
        if y != 0:
            return x / y
        else:
            logger.error("Попытка деления на ноль")
            print("Деление на ноль!")
            return None
    else:
        logger.error(f"Некорректная операция: {s}")
        return None


