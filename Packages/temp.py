from Aurora.Packages.screen_dimensions import *


class Spell(object):
    def __init__(self, x, y, address):
        self.x = x
        self.y = y
        self.icon = pygame.image.load(address).convert_alpha()

    def place(self):
        rect = self.icon.get_rect()
        rect.top = self.y
        rect.left = self.x
        screen.blit(self.icon, rect)

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
        rect.top = self.y
        rect.left = self.x
        screen.blit(self.icon, rect)

    def attack(self):
        pass


class Control(object):
    def __init__(self, y, address):
        self.icon = pygame.image.load(address).convert_alpha()
        self.x = int(sw(50) - (self.icon.get_width() / 2))
        self.y = y
        rect = self.icon.get_rect()
        rect.top = self.y
        rect.left = self.x
        screen.blit(self.icon, rect)


class Troop(object):
    def __init__(self, x, y, address):
        self.x = x
        self.y = y
        self.icon = pygame.image.load(address).convert_alpha()

    def place(self):
        rect = self.icon.get_rect()
        rect.top = self.y
        rect.left = self.x
        screen.blit(self.icon, rect)

    def attack(self):
        print(self)
        pass
