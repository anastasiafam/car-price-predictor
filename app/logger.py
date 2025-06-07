import datetime
import logging
import os

import pytz

current_file_path = os.path.abspath(__file__)

CWD = os.path.dirname(os.path.dirname(current_file_path)) + "/"


class Logger:
    def __init__(
        self,
        logger_name: str,
        log_file: str,
        timezone: str = "Europe/Moscow",
    ):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)
        self.timezone = pytz.timezone(timezone)

        file_handler = logging.FileHandler(log_file)
        console_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

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


def msk_time(*args):
    utc_dt = pytz.utc.localize(datetime.datetime.utcnow())
    converted = utc_dt.astimezone(pytz.timezone("Europe/Moscow"))
    return converted.timetuple()


logging.Formatter.converter = msk_time

logger = Logger("forecast_class_logger", CWD + "app/logs/car.log")
