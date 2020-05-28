# importing pygame library
import pygame

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)

# title and icon
pygame.display.set_caption("The helios attack")
icon = pygame.image.load('image/icon.png')
pygame.display.set_icon(icon)

# Game loop
running = True

poison = pygame.image.load('Image/32px/poison.png')
fire = pygame.image.load('Image/32px/fire.png')
plasma = pygame.image.load('Image/32px/plasma_small.png')
goc = pygame.image.load('Image/32px/space.png')


def spells():
    screen.blit(poison, (10, 660))
    screen.blit(fire, (50, 660))
    screen.blit(plasma, (90, 660))
    screen.blit(goc, (130, 660))


def troops():
    pass


while running:

    screen.fill((0, 0, 40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    spells()
    pygame.display.update()
