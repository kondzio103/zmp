"""
####################################################################
Snake runner instance

Konrad Komorowski
####################################################################
"""


import pygame

from framework.fw_object import FrameworkObject
from game_objects.config import SCREEN_WIDTH, SCREEN_HEIGHT
from game_objects.snake_obj import Food, Snake, Grid


class SnakeGame(FrameworkObject):
    """ Snake Game main class"""
    def __init__(self):
        super().__init__(name='Game')

    @staticmethod
    def run():
        """ Start Snake game instance """
        pygame.init()

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

        surface = pygame.Surface(screen.get_size())
        surface = surface.convert()

        grid = Grid()
        snake = Snake()
        food = Food()

        my_font = pygame.font.SysFont("monospace", 16)

        while True:
            clock.tick(10)
            snake.handle_keys()
            grid.draw(surface)
            if snake.move() != 0:
                return snake.length
            if snake.get_head_position() == food.position:
                snake.length += 1
                food.randomize_position()
            snake.draw(surface)
            food.draw(surface)
            screen.blit(surface, (0, 0))
            text = my_font.render(f"Score: {snake.length}", 1, (0, 0, 0))
            screen.blit(text, (5, 10))
            pygame.display.update()


if __name__ == '__main__':
    SnakeGame().run()
