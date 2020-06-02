import pygame
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
screen_height = screen.get_height() - 40
screen_width = screen.get_width()


def sh(percentage):
    return int(percentage*screen_height/100)


def sw(percentage):
    return int(percentage*screen_width/100)


def pix_w(pix):
    return pix*(100/screen_width)


def pix_h(pix):
    return pix*(100/screen_height)
