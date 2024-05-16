### Задание 1
import logging

def Calculate():
    s = input("Знак (+,-,*,/): ")
    logger.info(f"Считан знак операции: {s}")
    if s in ('+', '-', '*', '/'):
        x = float(input("x = "))
        logger.info(f"Считано первое число: {x}")
        y = float(input("y = "))
        logger.info(f"Считано второе число: {y}")
        if s == '+':
            print("%.2f" % (x+y))
            logger.info("Выполнилось сложение чисел")
        elif s == '-':
            print("%.2f" % (x-y))
            logger.info("Выполнилось вычитание чисел")
        elif s == '*':
            print("%.2f" % (x*y))
            logger.info("Выполнилось умножение чисел")
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
                logger.info("Выполнилось деление чисел")
            else:
                logger.error("Ошибка - деление на 0!")
                print("Деление на ноль!")
    else:
        print("Этот знак не поддерживается данным калькулятором!")
        logger.error("Ошибка ввода знака действия")

if __name__ == '__main__':
    logger = logging.getLogger("Calculate")
    Calculate()

### Задание 2
import logging
import sys

def CreateLogger(name):
    logger = logging.getLogger(name)
    handler = logging.StreamHandler(stream=sys.stdout)
    formatter = logging.Formatter("%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s")
    handler.setFormatter(formatter)
    logger.setLevel("DEBUG")
    logger.addHandler(handler)
    return logger

def Calculate():
    s = input("Знак (+,-,*,/): ")
    logger.info(f"Считан знак операции: {s}")
    if s in ('+', '-', '*', '/'):
        x = float(input("x = "))
        logger.info(f"Считано первое число: {x}")
        y = float(input("y = "))
        logger.info(f"Считано второе число: {y}")
        if s == '+':
            print("%.2f" % (x+y))
            logger.info("Выполнилось сложение чисел")
        elif s == '-':
            print("%.2f" % (x-y))
            logger.info("Выполнилось вычитание чисел")
        elif s == '*':
            print("%.2f" % (x*y))
            logger.info("Выполнилось умножение чисел")
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
                logger.info("Выполнилось деление чисел")
            else:
                logger.error("Ошибка - деление на 0!")
                print("Деление на ноль!")
    else:
        print("Этот знак не поддерживается данным калькулятором!")
        logger.error("Ошибка ввода знака действия")

if __name__ == '__main__':
    logger = CreateLogger("Calculate")
    Calculate()

### Задание 3
import logging
import sys
from customHandler import LevelHandler

def CreateLogger(name):
    logger = logging.getLogger(name)
    handler = LevelHandler()
    formatter = logging.Formatter("%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s")
    handler.setFormatter(formatter)
    logger.setLevel("DEBUG")
    logger.addHandler(handler)
    return logger

def Calculate():
    s = input("Знак (+,-,*,/): ")
    logger.info(f"Считан знак операции: {s}")
    if s in ('+', '-', '*', '/'):
        x = float(input("x = "))
        logger.info(f"Считано первое число: {x}")
        y = float(input("y = "))
        logger.info(f"Считано второе число: {y}")
        if s == '+':
            print("%.2f" % (x+y))
            logger.info("Выполнилось сложение чисел")
        elif s == '-':
            print("%.2f" % (x-y))
            logger.info("Выполнилось вычитание чисел")
        elif s == '*':
            print("%.2f" % (x*y))
            logger.info("Выполнилось умножение чисел")
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
                logger.info("Выполнилось деление чисел")
            else:
                logger.error("Ошибка - деление на 0!")
                print("Деление на ноль!")
    else:
        print("Этот знак не поддерживается данным калькулятором!")
        logger.error("Ошибка ввода знака действия")

if __name__ == '__main__':
    logger = CreateLogger("Calculate")
    Calculate()

### Задание 4
import logging
from dict_config import dict_config
import logging.config

def CreateLogger(name):
    logger = logging.getLogger(name)
    logging.config.dictConfig(dict_config)
    return logger

def Calculate():
    s = input("Знак (+,-,*,/): ")
    logger.info(f"Считан знак операции: {s}")
    if s in ('+', '-', '*', '/'):
        x = float(input("x = "))
        logger.info(f"Считано первое число: {x}")
        y = float(input("y = "))
        logger.info(f"Считано второе число: {y}")
        if s == '+':
            print("%.2f" % (x+y))
            logger.info("Выполнилось сложение чисел")
        elif s == '-':
            print("%.2f" % (x-y))
            logger.info("Выполнилось вычитание чисел")
        elif s == '*':
            print("%.2f" % (x*y))
            logger.info("Выполнилось умножение чисел")
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
                logger.info("Выполнилось деление чисел")
            else:
                logger.error("Ошибка - деление на 0!")
                print("Деление на ноль!")
    else:
        print("Этот знак не поддерживается данным калькулятором!")
        logger.error("Ошибка ввода знака действия")

if __name__ == '__main__':
    logger = CreateLogger("Calculate")
    Calculate()

### Задание 5
import logging
from dict_config import dict_config
import logging.config

def CreateLogger(name):
    logger = logging.getLogger(name)
    logging.config.dictConfig(dict_config)
    return logger

def Calculate():
    s = input("Знак (+,-,*,/): ")
    logger.info(f"Считан знак операции: {s}")
    if s in ('+', '-', '*', '/'):
        x = float(input("x = "))
        logger.info(f"Считано первое число: {x}")
        y = float(input("y = "))
        logger.info(f"Считано второе число: {y}")
        if s == '+':
            print("%.2f" % (x+y))
            logger.info("Выполнилось сложение чисел")
        elif s == '-':
            print("%.2f" % (x-y))
            logger.info("Выполнилось вычитание чисел")
        elif s == '*':
            print("%.2f" % (x*y))
            logger.info("Выполнилось умножение чисел")
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
                logger.info("Выполнилось деление чисел")
            else:
                logger.error("Ошибка - деление на 0!")
                print("Деление на ноль!")
    else:
        print("Этот знак не поддерживается данным калькулятором!")
        logger.error("Ошибка ввода знака действия")
    Calculate()

if __name__ == '__main__':
    logger = CreateLogger("Calculate")
    Calculate()

### Задание 6
import logging
import sys

import logging_tree
import contextlib
from logging_tree import printout

logging.getLogger('a')
logging.getLogger('a.b').setLevel(logging.DEBUG)
logging.getLogger('x.c')

with open("logging_tree.txt", "w") as f:
    with contextlib.redirect_stdout(f):
        printout()

### Задание 7
import logging
from dict_config import dict_config
import logging.config

def CreateLogger(name):
    logger = logging.getLogger(name)
    logging.config.dictConfig(dict_config)
    return logger

def Calculate():
    s = input("Знак (+,-,*,/): ")
    logger.info(f"Считан знак операции: {s}")
    if s in ('+', '-', '*', '/'):
        x = float(input("x = "))
        logger.info(f"Считано первое число: {x}")
        y = float(input("y = "))
        logger.info(f"Считано второе число: {y}")
        if s == '+':
            print("%.2f" % (x+y))
            logger.info("Выполнилось сложение чисел")
        elif s == '-':
            print("%.2f" % (x-y))
            logger.info("Выполнилось вычитание чисел")
        elif s == '*':
            print("%.2f" % (x*y))
            logger.info("Выполнилось умножение чисел")
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
                logger.info("Выполнилось деление чисел")
            else:
                logger.error("Ошибка - деление на 0!")
                print("Деление на ноль!")
    else:
        print("Этот знак не поддерживается данным калькулятором!")
        logger.error("Ошибка ввода знака действия")
        logger.info("ОШИБКА ASCII Ø∏‡°⁄·°")
    Calculate()

if __name__ == '__main__':
    logger = CreateLogger("Calculate")
    Calculate()
