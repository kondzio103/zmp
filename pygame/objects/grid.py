import pygame

from framework.fw_object import FrameworkObject
import objects.config as cfg


class Grid(FrameworkObject):
    def __init__(self):
        super(Grid, self).__init__(name='Grid')

    @staticmethod
    def draw(surface):
        for y in range(0, cfg.GRID_HEIGHT):
            for x in range(0, cfg.GRID_WIDTH):
                rect = pygame.Rect((x * cfg.GRID_SIZE, y * cfg.GRID_SIZE), (cfg.GRID_SIZE, cfg.GRID_SIZE))
                pygame.draw.rect(surface, cfg.GRID_COLOR[(x + y) % 2], rect)
