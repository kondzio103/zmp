import pygame

from framework.fw_object import FrameworkObject
from objects.config import SCREEN_WIDTH, SCREEN_HEIGHT
from objects.food import Food
from objects.snake import Snake
from objects.grid import Grid


class SnakeGame(FrameworkObject):
    def __init__(self):
        super(SnakeGame, self).__init__(name='Game')

    @staticmethod
    def run():
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
            snake.move()
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
