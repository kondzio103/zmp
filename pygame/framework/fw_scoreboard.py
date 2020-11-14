"""
####################################################################

Konrad Komorowski
####################################################################
"""
import json
import os

from framework.fw_helpers import get_scoreboard_path
from framework.fw_object import FrameworkObject


class ScoreBoard(FrameworkObject):
    """ Works with score board file """
    def __init__(self, limit=5):
        super().__init__('Scoreboard')
        self.scoreboard = {}
        self.read_scoreboard()
        self.limit = limit

    def read_scoreboard(self):
        """ Read score board file content into internal variable"""
        if os.path.exists(get_scoreboard_path()):
            with open(get_scoreboard_path(), 'r') as file:
                self.scoreboard = json.load(file)
            self._log_debug("Read scoreboard file.")
        else:
            self._log_debug("Score bord file do not exist. No scores ware read")

    def save_scoreboard(self):
        """ Save current scoreboard intral variable to the file """
        with open(get_scoreboard_path(), 'w') as file:
            json.dump(self.scoreboard, file, indent=4)
        self._log_debug("Saved scoreboard file")

    def updade_scoreboard(self, score, name):
        """ Upload scoreboard by adding new score
        Args:
            score (int): achieved points
            name (str): name associated with the achievement
        """
        score_list = list(self.scoreboard.values())
        score_list.append([score, name])
        score_list = sorted(score_list, reverse=True)

        self.scoreboard = dict()
        for i, value in enumerate(score_list, 1):
            self.scoreboard[i] = value
            if i == self.limit:
                break

        self._log_debug("Updated scoreboard")
        self.save_scoreboard()
