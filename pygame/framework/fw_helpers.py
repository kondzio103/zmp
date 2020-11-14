"""
####################################################################
Framework helpers library

Konrad Komorowski
####################################################################
"""


def get_framework_path():
    """ Returns absolute path to the main folder """
    return __file__.split('framework\\fw_helpers.py')[0]


def get_logs_path():
    """ Returns absolute path to the folder containing log files """
    return get_framework_path() + 'logs\\'


def get_scoreboard_path():
    """ Returns absolute path to the scoreboard file """
    return get_framework_path() + 'scoreboard.json'
