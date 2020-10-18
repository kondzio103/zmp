"""
####################################################################

Konrad Komorowski
####################################################################
"""
import framework.fw_logging as fw_logging
import logging


class FrameworkObject(object):
    """ Base FW object. """

    def __init__(self, name):
        self.name = name
        self.logger = fw_logging.create_logger(name)

    def _log(self, message, level=logging.INFO):
        self.logger.log(level, message)

    def _info(self, message):
        self.logger.info(message)

    def _log_warning(self, message):
        self.logger.warning(message)

    def _log_error(self, message):
        self.logger.error(message)
