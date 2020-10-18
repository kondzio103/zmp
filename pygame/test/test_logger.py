"""
####################################################################
Logger Unit Tests

Konrad Komorowski
####################################################################
"""
import os

import framework.fw_helpers as fw_helpers
import framework.fw_logging as fw_logging


DEBUG_FILE = fw_helpers.get_logs_path() + 'debug.log'
ERROR_FILE = fw_helpers.get_logs_path() + 'error.log'


def test_file_loggers():
    """ Test if logs are properly written to the files. """
    log_table = {
        0: ['<< Debug Message >>', '[DEBUG   ][UnitLogger]: << Debug Message >>\n'],
        1: ['<< Info Message >>', '[INFO    ][UnitLogger]: << Info Message >>\n'],
        2: ['<< Warning Message >>', '[WARNING ][UnitLogger]: << Warning Message >>\n'],
        3: ['<< Error Message >>', '[ERROR   ][UnitLogger]: << Error Message >>\n'],
        4: ['<< Critical Message >>', '[CRITICAL][UnitLogger]: << Critical Message >>\n'],
    }
    if os.path.exists(DEBUG_FILE):
        os.remove(DEBUG_FILE)
    if os.path.exists(ERROR_FILE):
        os.remove(ERROR_FILE)

    logger = fw_logging.create_logger('UnitLogger')

    logger.debug(log_table[0][0])
    logger.info(log_table[1][0])
    logger.warning(log_table[2][0])
    logger.error(log_table[3][0])
    logger.critical(log_table[4][0])

    with open(DEBUG_FILE, encoding='utf-8') as file:
        for i, line in enumerate(file):
            line_str = line[26:]
            assert line_str in log_table[i][1]

    with open(ERROR_FILE, encoding='utf-8') as file:
        for i, line in enumerate(file, 3):
            line_str = line[26:]
            print('file' + line_str)
            print('orgi' + log_table[i][1])
            assert line_str in log_table[i][1]
