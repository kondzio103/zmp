import logging


def create_logger(name):
    # create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter(' [%(asctime)s][%(levelname)-8s][%(name)s]: %(message)s')

    # add formatter to ch
    ch.setFormatter(CustomFormatter())

    # add ch to logger
    logger.addHandler(ch)

    return logger


class CustomFormatter(logging.Formatter):
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
    FORMAT = ' [%(asctime)s][%(levelname)-8s][%(name)s]: %(message)s'

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