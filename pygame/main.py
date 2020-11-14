"""
####################################################################
Game Main Instance

Konrad Komorowski
####################################################################
"""

from game_objects.game_core import GameCore

if __name__ == '__main__':
    game = GameCore()
    game.logger.debug('Starting the game...')
    while game.running:
        game.curr_menu.display_menu()
        game.game_loop()
