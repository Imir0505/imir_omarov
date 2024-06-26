### Задание 1-2
import getpass
import hashlib
import logging
import re

logger = logging.getLogger("password_checker")


def is_weak_password(password: str, words: str) -> bool:
    password = password.lower()
    result = re.findall("\D{4,}", password)
    for word in result:
        if word in words:
            return True
    return False


def input_and_check_password() -> bool:
    logger.debug("Начало input_and_check_password")
    password: str = getpass.getpass()

    if not password:
        logger.warning("Вы ввели пустой пароль.")
        return False
    elif is_weak_password(password, word_data):
        logger.warning("Вы ввели слишком слабый пароль")
        return False

    try:
        hasher = hashlib.md5()

        hasher.update(password.encode("latin-1"))

        if hasher.hexdigest() == "098f6bcd4621d373cade4e832627b4f6":
            return True
    except ValueError as ex:
        logger.exception("Вы ввели некорректный символ ", exc_info=ex)

    return False


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename='stderr.txt', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%I:%M:%S')
    logger.info("Вы пытаетесь аутентифицироваться в Skillbox")
    count_number: int = 3
    logger.info(f"У вас есть {count_number} попыток")

    with open('/usr/share/dict/words', 'r') as word_file:
        word_data = word_file.read()

    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1

    logger.error("Пользователь трижды ввёл не правильный пароль!")
    exit(1)

### Задание 3
import json
import logging


class JsonAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        msg = msg.replace('"', '\\"')
        return msg, kwargs


if __name__ == "__main__":
    logger = JsonAdapter(logging.getLogger(__name__))
    logger.info('Сообщение')
    fmtstring = "%(asctime)s - %(levelname)s - %(message)s".split(' - ')
    fmtdct = dict()
    fmtdct["time"] = fmtstring[0]
    fmtdct["level"] = fmtstring[1]
    fmtdct["message"] = fmtstring[2]
    logging.basicConfig(level=logging.DEBUG, filename="skillbox_json_messages.log",
                        format=json.dumps(fmtdct), datefmt='%I:%M:%S')
    json.dumps(logger.info("test"))
    logger.info('singlequoted')
    logger.error('"quoted"')
    logger.debug("another test")
    logger.debug("""""""")
