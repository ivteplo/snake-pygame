import pygame
from constants import *


class Apple:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        surface = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.circle(
            screen,
            APPLE_COLOR,
            (self.x * BLOCK_SIZE + BLOCK_SIZE / 2, self.y * BLOCK_SIZE + BLOCK_SIZE / 2),
            BLOCK_SIZE / 2
        )

