"""
####################################################################
Food

Konrad Komorowski
####################################################################
"""
import random
import pygame

from framework.fw_object import FrameworkObject
import game_objects.config as cfg


class Food(FrameworkObject):
    def __init__(self):
        super().__init__(name='Food')
        self.position = (0, 0)
        self.color = cfg.FOOD_COLOR
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, cfg.GRID_WIDTH - 1) * cfg.GRID_SIZE, random.randint(0, cfg.GRID_HEIGHT - 1) * cfg.GRID_SIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (cfg.GRID_SIZE, cfg.GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)
