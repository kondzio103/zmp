"""
####################################################################
Framework helpers library

Konrad Komorowski
####################################################################
"""


def get_framework_path():
    return __file__.split('framework\\fw_helpers.py')[0]


def get_logs_path():
    return get_framework_path() + 'logs\\'

