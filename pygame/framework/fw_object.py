"""
####################################################################

Konrad Komorowski
####################################################################
"""
import logging
import framework.fw_logging as fw_logging


class FrameworkObject:
    """ Base FW object. """

    def __init__(self, name):
        self.name = name
        self.logger = fw_logging.create_logger(name)

    def _log(self, message, level=logging.INFO):
        self.logger.log(level, message)

    def _log_debug(self, message):
        self.logger.debug(message)

    def _log_info(self, message):
        self.logger.info(message)

    def _log_warning(self, message):
        self.logger.warning(message)

    def _log_error(self, message):
        self.logger.error(message)

    def _log_critical(self, message):
        self.logger.critical(message)
