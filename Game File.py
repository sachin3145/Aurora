# importing pygame library
import pygame

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((1024, 720))

# title and icon
pygame.display.set_caption("The helios attack")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((240, 248, 255))
    pygame.display.update()
