import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)


from apple import Apple
from constants import *
from math import floor
from random import randint
from snake import Body as Snake


def random(coord='x'):
    if coord == 'x':
        return randint(X_MIN, X_MAX)
    return randint(Y_MIN, Y_MAX)


# Initialize pygame
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Snake')

direction = (0, 0)

snake_body = Snake()
snake_body.add_part(random('x'), random('y'))

apple = Apple()
apple.set_coordinates(random('x'), random('y'))

running = True
prev_time = pygame.time.get_ticks()

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False 
        elif event.type == KEYDOWN:
            if event.key == K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == K_RIGHT and direction != (-1, 0):
                direction = (1, 0)
            elif event.key == K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == K_DOWN and direction != (0, -1):
                direction = (0, 1)

    screen.fill((0xCC, 0xCC, 0xCC))

    if snake_body.collides(apple.x, apple.y):
        snake_body.increase_length()
        apple.set_coordinates(random('x'), random('y'))

    if snake_body.collides_itself():
        snake_body.reset_length()

    snake_body.move_by(direction)
    snake_body.update()

    snake_body.draw(screen)
    apple.draw(screen)

    pygame.display.update()

    clock.tick(max(15.25 - 0.25 * len(snake_body.parts), 10))

pygame.quit()

