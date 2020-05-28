# importing pygame library
import pygame

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)

# title and icon
pygame.display.set_caption("The helios attack")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Game loop
running = True


planet_img = pygame.image.load('plasma_small.png')
planetX = 625
planetY = 100
position = planetX, planetY


def planet():
    screen.blit(planet_img, tuple(position))


while running:

    screen.fill((0, 0, 40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    planet()
    pygame.display.update()
