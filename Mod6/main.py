### Задание 1
import logging

# Настройка логгера
logging.basicConfig(
    level=logging.INFO,  # Уровень логирования INFO и выше
    format='%(asctime)s - %(levelname)s - %(message)s',  # Форматирование сообщений
    datefmt='%H:%M:%S',  # Формат времени HH:MM:SS
    handlers=[logging.FileHandler("stderr.txt", mode='w')]  # Запись в файл stderr.txt
)

# Примеры использования логгера
logging.debug('Это сообщение отладки и не будет записано в файл.')
logging.info('Это сообщение уровня INFO.')
logging.warning('Это сообщение уровня WARNING.')
logging.error('Это сообщение уровня ERROR.')
logging.critical('Это сообщение уровня CRITICAL.')

### Задание 2

