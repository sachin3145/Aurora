from Aurora.Packages.screen_dimensions import *


class Spell(object):
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


class Planet(object):
    def __init__(self, address):
        self.icon = pygame.image.load(address)
        self.x = int(sw(50) - (self.icon.get_width() / 2))
        self.y = int(sh(2) + 128 - (self.icon.get_height() / 2))

    def place(self):
        rect = self.icon.get_rect()
        screen.blit(self.icon, (self.x, self.y,))

    def attack(self):
        pass
