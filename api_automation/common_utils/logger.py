import datetime
import inspect
import logging
import os

current_time = datetime.datetime.now().strftime("_%Y_%m_%d_%H_%M_%S.log")

LOGFILE_NAME = f"local_{current_time}"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
LOG_MSG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
Log_FILE_DIRECTORY = "logs"
LOG_PROJECT_NAME = "API_TEST"
LOG_TYPE = "API"
LOG_IS_STDOUT = True

# Decide what level log should be display.
LOGGER_LEVEL = os.getenv("LOG_LEVEL", 'INFO').upper()
DIR_PATH = os.path.join(Log_FILE_DIRECTORY)


class LoggerManager(object):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Logger()
        return cls.instance

    @classmethod
    def reset_instance(cls):
        cls.instance = None


class Logger(object):
    def __init__(self):
        formatter = logging.Formatter(fmt=LOG_MSG_FORMAT, datefmt=LOG_DATE_FORMAT)
        self.logger = self.set_logger(
            "{project}-{type}".format(project=LOG_PROJECT_NAME, type=LOG_TYPE),
            formatter,
            LOGGER_LEVEL,
            LOGFILE_NAME,
            std_out=LOG_IS_STDOUT,
        )

    @staticmethod
    def set_logger(logger_name, formatter, level, file_name, std_out=False):
        logger = logging.getLogger(logger_name)
        if not os.path.exists(DIR_PATH):
            os.makedirs(DIR_PATH)
        file_handler = logging.FileHandler(os.path.join(DIR_PATH, file_name), mode="a")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(level)
        if std_out:
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            logger.addHandler(stream_handler)
        return logger

    @staticmethod
    def change_text_by_logger(msg):
        frame = inspect.stack()[2]
        module = inspect.getmodule(frame[0])
        info = inspect.getframeinfo(frame[0])

        text = "[{module}@line:{lineno}][{msg}]".format(
            module=module.__name__,
            lineno=info.lineno,
            msg=msg,
        )
        return text

    def critical(self, msg):
        self.logger.critical(self.change_text_by_logger(msg))

    def error(self, msg):
        self.logger.error(self.change_text_by_logger(msg))

    def warning(self, msg):
        self.logger.warning(self.change_text_by_logger(msg))

    def info(self, msg):
        self.logger.info(self.change_text_by_logger(msg))

    def debug(self, msg):
        self.logger.debug(self.change_text_by_logger(msg))
