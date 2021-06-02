import pygame
from constants import *


class BodyPart:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        if self.x < X_MIN:
            self.x += X_MAX + 1
        elif self.x > X_MAX:
            self.x -= X_MAX + 1

        if self.y < Y_MIN:
            self.y += Y_MAX + 1
        elif self.y > Y_MAX:
            self.y -= Y_MAX + 1

    def draw(self, screen):
        surface = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        surface.fill(SNAKE_COLOR)
        screen.blit(surface, (self.x * BLOCK_SIZE, self.y * BLOCK_SIZE))

    def collides(self, x, y):
        return self.x == x and self.y == y


class Body:
    def __init__(self):
        self.length = 1
        self.parts = []
        self._tail_last_pos = None

    def add_part(self, x, y):
        self.parts.append(BodyPart(x, y))

        if len(self.parts) == 1:
            self._tail_last_pos = self.parts[0]

    def increase_length(self):
        self.add_part(self._tail_last_pos.x, self._tail_last_pos.y)

    def collides_itself(self):
        for part in self.parts[:-2]:
            if self.parts[-1].collides(part.x, part.y):
                return True

        return False
    
    def reset_length(self):
        self.parts = self.parts[-1:]
        self._tail_last_pos = None

    def collides(self, x, y):
        head = self.parts[-1]
        return head.collides(x, y)

    def draw(self, screen):
        for part in self.parts:
            part.draw(screen)

    def update(self):
        for part in self.parts:
            part.update()

    def move_by(self, direction):
        last = self.parts[0]
        first = self.parts[-1]

        self._tail_last_pos = last

        self.parts.pop(0)
        
        last.x = first.x + direction[0]
        last.y = first.y + direction[1]
        self.parts.append(last)

