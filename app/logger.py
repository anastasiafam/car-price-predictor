import logging
import pytz  # Импортируем pytz
import datetime
import os

# Получаем абсолютный путь к текущему файлу
current_file_path = os.path.abspath(__file__)
# Получаем путь к родительской директории
CWD = os.path.dirname(os.path.dirname(current_file_path)) + '/'

class Logger:
    def __init__(self, logger_name: str, log_file: str, timezone: str = 'Europe/Moscow'): #Добавил timezone
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)
        self.timezone = pytz.timezone(timezone) #Устанавливаем таймзону

        file_handler = logging.FileHandler(log_file)
        console_handler = logging.StreamHandler()

        # Create formatters and add it to handlers
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        self.logger.propagate = False

    def debug(self, message: str):
        self.logger.debug(message)

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)

    def critical(self, message: str):
        self.logger.critical(message)

# Определяем функцию для конвертации времени
def msk_time(*args):
    utc_dt = pytz.utc.localize(datetime.datetime.utcnow())
    converted = utc_dt.astimezone(pytz.timezone('Europe/Moscow'))
    return converted.timetuple()

logging.Formatter.converter = msk_time

logger = Logger('forecast_class_logger', CWD+'app/logs/car.log')

