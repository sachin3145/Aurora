from Aurora.Packages.dependencies import *


class Spells(object):
    def __init__(self, x, y, name, address):
        self.x = x
        self.y = y
        self.name = name
        self.icon = pygame.image.load(address)

    def place(self):
        rect = self.icon.get_rect()
        screen.blit(self.icon, (self.x, self.y,))

    def attack(self):
        print(self.name)
        pass

