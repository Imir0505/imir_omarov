import logging

# Настраиваем локальный логгер для utils
logger = logging.getLogger('utils')

def some_function():
    logger.info("Информация в utils: Вызвана some_function()")
