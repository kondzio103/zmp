"""
####################################################################
Game core instance

Konrad Komorowski
####################################################################
"""
import pygame

import game_objects.config as conf
from game_objects.menu_obj import MainMenu, ScoreBoardMenu, CreditsMenu
from game_objects.snake_runner import SnakeGame

from framework.fw_scoreboard import ScoreBoard
from framework.fw_object import FrameworkObject


class GameCore(FrameworkObject):
    """ Core game wrapper """
    def __init__(self):
        super().__init__(name='GameCore')
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.display = pygame.Surface((conf.SCREEN_WIDTH, conf.SCREEN_HEIGHT))
        self.window = pygame.display.set_mode((conf.SCREEN_WIDTH, conf.SCREEN_HEIGHT))
        self.font_name = pygame.font.get_default_font()

        self.main_menu = MainMenu(self)
        self.score_board_menu = ScoreBoardMenu(self)
        self.credits = CreditsMenu(self)

        self.curr_menu = self.main_menu
        self.score_board_obj = ScoreBoard(5)

    def game_loop(self):
        """ Main game wrapper loop """
        play_state, name, score = 'pre_game', '', None
        while self.playing:
            text = self.check_events()
            if self.START_KEY:
                if play_state == 'pre_game':
                    play_state = 'game'
                elif play_state == 'post_game':
                    self.playing = False
                    self.score_board_obj.updade_scoreboard(score, name)

            if play_state == 'pre_game':
                self.display.fill(conf.BLACK)
                self.draw_text('PRESS START TO PLAY', 20, conf.SCREEN_WIDTH // 2, conf.SCREEN_HEIGHT // 2)
                self.window.blit(self.display, (0, 0))
                pygame.display.update()

            if play_state == 'game':
                self._log_debug('Started Snake game instance')
                score = SnakeGame.run()
                self._log_debug(f'Finished Snake game instance with score {score}')
                play_state = 'post_game'

            if play_state == 'post_game':
                if text:
                    name += text

                self.display.fill(conf.BLACK)
                self.draw_text(f'Your score is: {score}', 50, conf.SCREEN_WIDTH // 2, conf.SCREEN_HEIGHT // 2)
                self.draw_text('Type Your name:', 20, conf.SCREEN_WIDTH // 2, conf.SCREEN_HEIGHT // 2 + 50)
                self.draw_text(f'{name}', 40, conf.SCREEN_WIDTH // 2, conf.SCREEN_HEIGHT // 2 + 100)
                self.window.blit(self.display, (0, 0))
                pygame.display.update()
            self.reset_keys()

    def check_events(self):
        """ Get in game events and writen text
         Returns:
             text (str): writen text
         """
        text = ""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                elif event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                elif event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                elif event.key == pygame.K_UP:
                    self.UP_KEY = True
                else:
                    text += event.unicode
            return text

    def reset_keys(self):
        """ Reset saved key states """
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y, center=True):
        """ Draw text
        Args:
            text (str): input text
            size (int): text size
            x (int): x position
            y (int): y position
            center (bool): whether given position is the center of the txt or left up corner
        """
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, conf.WHITE)
        if center:
            text_rect = text_surface.get_rect()
            text_rect.center = (x, y)
            self.display.blit(text_surface, text_rect)
        else:
            self.display.blit(text_surface, (x, y))

    def quit(self):
        """ Quites the game """
        self.running, self.playing = False, False
        self.curr_menu.run_display = False
