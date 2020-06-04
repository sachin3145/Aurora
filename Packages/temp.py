from Aurora.Packages.screen_dimensions import *


class Spell(object):
    def __init__(self, x, y, address):
        self.x = x
        self.y = y
        self.icon = pygame.image.load(address).convert_alpha()

    def place(self):
        rect = self.icon.get_rect()
        screen.blit(self.icon, (self.x, self.y,))

    def attack(self):
        print(self)
        pass


class Planet(object):
    def __init__(self, address):
        self.icon = pygame.image.load(address).convert_alpha()
        self.x = int(sw(50) - (self.icon.get_width() / 2))
        self.y = int(sh(2) + 128 - (self.icon.get_height() / 2))

    def place(self):
        rect = self.icon.get_rect()
        screen.blit(self.icon, (self.x, self.y,))

    def attack(self):
        pass


class Control(object):
    def __init__(self, y, address):
        self.icon = pygame.image.load(address).convert_alpha()
        self.x = int(sw(50) - (self.icon.get_width() / 2))
        self.y = y
        screen.blit(self.icon, (self.x, self.y,))


class Troop(object):
    def __init__(self, x, y, address):
        self.x = x
        self.y = y
        self.icon = pygame.image.load(address).convert_alpha()

    def place(self):
        rect = self.icon.get_rect()
        screen.blit(self.icon, (self.x, self.y,))

    def attack(self):
        print(self)
        pass
