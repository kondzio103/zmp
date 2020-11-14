"""
####################################################################

Konrad Komorowski
####################################################################
"""
import json

from framework.fw_helpers import get_scoreboard_path
from framework.fw_object import FrameworkObject


class ScoreBoard(FrameworkObject):
    def __init__(self, limit=5):
        super().__init__('Scoreboard')
        self.scoreboard = None
        self.read_scoreboard()
        self.limit = limit

    def read_scoreboard(self):
        with open(get_scoreboard_path(), 'r') as file:
            self.scoreboard = json.load(file)
        self._log_debug("Read scoreboard file.")

    def save_scoreboard(self):
        with open(get_scoreboard_path(), 'w') as file:
            json.dump(self.scoreboard, file, indent=4)
        self._log_debug("Saved scoreboard file")

    def updade_scoreboard(self, score, name):
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
