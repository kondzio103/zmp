"""
####################################################################
Logging library

Konrad Komorowski
####################################################################
"""
import logging
import framework.fw_helpers as fw_helpers

DEBUG_FORMAT = ' [%(asctime)s][%(levelname)-8s][%(name)s]: %(message)s'
ERROR_FORMAT = ' [%(asctime)s][%(levelname)-8s][%(name)s]: %(message)s'
STREAM_FORMAT = ' [%(levelname)-8s][%(name)s]: %(message)s'


def create_logger(name):
    """ Create logger with given name
    Args:
        name (str): Logger name
    """
    log_path = fw_helpers.get_logs_path()

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    s_handler = logging.StreamHandler()
    s_handler.setLevel(logging.DEBUG)
    s_handler.setFormatter(StreamFormatter())
    logger.addHandler(s_handler)

    f_handler_debug = logging.FileHandler(filename=log_path + 'debug.log', encoding='utf-8')
    f_handler_debug.setLevel(logging.DEBUG)
    f_handler_debug.setFormatter(logging.Formatter(DEBUG_FORMAT))
    logger.addHandler(f_handler_debug)

    f_handler_error = logging.FileHandler(filename=log_path + 'error.log', encoding='utf-8')
    f_handler_error.setLevel(logging.ERROR)
    f_handler_error.setFormatter(logging.Formatter(ERROR_FORMAT))
    logger.addHandler(f_handler_error)

    return logger


class StreamFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    DEBUG = '\033[2m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    CRITICAL = '\033[98m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    FORMAT = STREAM_FORMAT

    FORMATS = {
        logging.DEBUG: DEBUG + FORMAT + ENDC,
        logging.INFO: OKBLUE + FORMAT + ENDC,
        logging.WARNING: WARNING + FORMAT + ENDC,
        logging.ERROR: ERROR + FORMAT + ENDC,
        logging.CRITICAL: CRITICAL + FORMAT + ENDC
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
