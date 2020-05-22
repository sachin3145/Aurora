# importing pygame library
import pygame

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("The Helios Attack")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#RGB- reg, green, blue
    screen.fill((0, 0, 128))
    pygame.display.update()

