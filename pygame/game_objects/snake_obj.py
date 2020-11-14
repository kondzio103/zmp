"""
####################################################################
Snake Game Objects

Konrad Komorowski
####################################################################
"""
import random
import pygame
import sys

from framework.fw_object import FrameworkObject
import game_objects.config as cfg


UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


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


class Snake(FrameworkObject):
    def __init__(self):
        super().__init__(name='Snake')
        self.color = cfg.SNAKE_COLOR
        self.length = None
        self.positions = None
        self.direction = None

        self.reset()

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * cfg.GRID_SIZE)) % cfg.SCREEN_WIDTH), (cur[1] + (y * cfg.GRID_SIZE)) % cfg.SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            return -1

        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()
        return 0

    def reset(self):
        self.length = 1
        self.positions = [((cfg.SCREEN_WIDTH / 2), (cfg.SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((int(p[0]), int(p[1])), (cfg.GRID_SIZE, cfg.GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)


class Grid(FrameworkObject):
    def __init__(self):
        super(Grid, self).__init__(name='Grid')

    @staticmethod
    def draw(surface):
        for y in range(0, cfg.GRID_HEIGHT):
            for x in range(0, cfg.GRID_WIDTH):
                rect = pygame.Rect((x * cfg.GRID_SIZE, y * cfg.GRID_SIZE), (cfg.GRID_SIZE, cfg.GRID_SIZE))
                pygame.draw.rect(surface, cfg.GRID_COLOR[(x + y) % 2], rect)
