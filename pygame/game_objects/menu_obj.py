"""
####################################################################
Menu instance

Konrad Komorowski
####################################################################
"""

import pygame

from framework.fw_object import FrameworkObject
import game_objects.config as conf


class Menu(FrameworkObject):
    """ Menu Object """
    def __init__(self, game):
        super().__init__(name='Menu')
        self.game = game
        self.mid_w, self.mid_h = conf.SCREEN_WIDTH // 2, conf.SCREEN_HEIGHT // 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -80

    def draw_cursor(self):
        """ Drow selection cursor"""
        self.game.draw_text('X', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        """ Draw image """
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    """ Main Menu Object. """
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Start'
        self.menu_list = {
            'Start': {'x': self.mid_w, 'y': self.mid_h + 40},
            'ScoreBoard': {'x': self.mid_w, 'y': self.mid_h + 70},
            'Credits': {'x': self.mid_w, 'y': self.mid_h + 100},
            'Quit': {'x': self.mid_w, 'y': self.mid_h + 130},
        }

        self.start_x, self.start_y = self.mid_w, self.mid_h + 40
        self.score_x, self.score_y = self.mid_w, self.mid_h + 70
        self.credits_x, self.credits_y = self.mid_w, self.mid_h + 100
        self.quit_x, self.quit_y = self.mid_w, self.mid_h + 130
        self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)

    def display_menu(self):
        """ Display Main Menu"""
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(conf.BLACK)
            self.game.draw_text('Main Menu', 30, conf.SCREEN_WIDTH // 2, conf.SCREEN_HEIGHT // 2 - 20)
            self.game.draw_text('Start Game', 20, self.menu_list['Start']['x'], self.menu_list['Start']['y'])
            self.game.draw_text('Score Board', 20, self.menu_list['ScoreBoard']['x'], self.menu_list['ScoreBoard']['y'])
            self.game.draw_text('Credits', 20, self.menu_list['Credits']['x'], self.menu_list['Credits']['y'])
            self.game.draw_text('Quit', 20, self.menu_list['Quit']['x'], self.menu_list['Quit']['y'])
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        """ Move selection cursor """
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.state = 'ScoreBoard'
            elif self.state == 'ScoreBoard':
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.state = 'Quit'
            elif self.state == 'Quit':
                self.state = 'Start'

        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.state = 'Quit'
            elif self.state == 'ScoreBoard':
                self.state = 'Start'
            elif self.state == 'Credits':
                self.state = 'ScoreBoard'
            elif self.state == 'Quit':
                self.state = 'Credits'

        self.cursor_rect.midtop = (self.menu_list[self.state]['x'] + self.offset, self.menu_list[self.state]['y'])

    def check_input(self):
        """ Process use input """
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'ScoreBoard':
                self.game.curr_menu = self.game.score_board_menu
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            elif self.state == 'Quit':
                self.game.quit()

            self.run_display = False


class ScoreBoardMenu(Menu):
    """ Score Board Menu """
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        """ Display Score Board Menu"""
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(conf.BLACK)
            self.game.draw_text('Score: ', 25, conf.SCREEN_WIDTH // 2, conf.SCREEN_HEIGHT // 2 - 20)
            for key, value in self.game.score_board_obj.scoreboard.items():
                self.game.draw_text(f'{str(value[0]).zfill(4)}    {value[1]}', 20, conf.SCREEN_WIDTH // 3, conf.SCREEN_HEIGHT // 2 - 10 + 20 * int(key), False)
            self.blit_screen()


class CreditsMenu(Menu):
    """ Credits Menu """
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        """ Display Credits Menu"""
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(conf.BLACK)
            self.game.draw_text('Credits', 20, conf.SCREEN_WIDTH // 2, conf.SCREEN_HEIGHT // 2 - 20)
            self.game.draw_text('Konrad Komorowski', 15, conf.SCREEN_WIDTH // 2, conf.SCREEN_HEIGHT // 2 + 10)
            self.blit_screen()
