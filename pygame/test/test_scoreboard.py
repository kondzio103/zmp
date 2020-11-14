"""
####################################################################
Score Board Unit Tests

Konrad Komorowski
####################################################################
"""
import os
import pytest

import framework.fw_scoreboard as scr
import framework.fw_helpers as fw_helpers

SCR_FILE = fw_helpers.get_scoreboard_path()


def test_scoreboard(scoreboard_instance):
    """ Test if scoreboard are properly written to the file. """
    scores = {
        0: (60, 'Angelika'),
        1: (55, 'Konrad'),
        2: (37, 'Krystian'),
        3: (23, 'Kasia'),
        4: (20, 'Ignacy'),
        5: (7, 'Beatrycze'),
        6: (2, 'Lydia'),
    }

    scoreboard_instance.read_scoreboard()
    scoreboard_instance.updade_scoreboard(scores[3][0], scores[3][1])
    scoreboard_instance.updade_scoreboard(scores[6][0], scores[6][1])
    scoreboard_instance.updade_scoreboard(scores[2][0], scores[2][1])
    scoreboard_instance.updade_scoreboard(scores[1][0], scores[1][1])
    scoreboard_instance.updade_scoreboard(scores[4][0], scores[4][1])
    scoreboard_instance.updade_scoreboard(scores[5][0], scores[5][1])
    scoreboard_instance.read_scoreboard()

    for i, (scr_key, (scr_score, scr_name)) in enumerate(scoreboard_instance.scoreboard.items(), 1):
        scr_key = int(scr_key)
        assert scr_key in range(1, 6)
        assert scr_score == scores[i][0]
        assert scr_name == scores[i][1]


@pytest.fixture
def scoreboard_instance():
    if os.path.exists(SCR_FILE):
        os.remove(SCR_FILE)
    return scr.ScoreBoard(5)
