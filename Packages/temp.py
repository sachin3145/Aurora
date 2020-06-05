from Aurora.Packages.screen_dimensions import *


class Spell(object):
    def __init__(self, x, y, address):
        self.x = x
        self.y = y
        self.icon = pygame.image.load(address).convert_alpha()
        self.rect = self.icon.get_rect()

    def place(self):
        self.rect.top = self.y
        self.rect.left = self.x
        screen.blit(self.icon, self.rect)

    def attack(self):
        print(self)
        pass


class Planet(object):
    def __init__(self, address):
        self.icon = pygame.image.load(address).convert_alpha()
        self.x = int(sw(50) - (self.icon.get_width() / 2))
        self.y = int(sh(2) + 128 - (self.icon.get_height() / 2))
        self.rect = self.icon.get_rect()

    def place(self):
        self.rect.top = self.y
        self.rect.left = self.x
        screen.blit(self.icon, self.rect)

    def attack(self):
        pass


class Control(object):
    def __init__(self, y, address):
        self.icon = pygame.image.load(address).convert_alpha()
        self.x = int(sw(50) - (self.icon.get_width() / 2))
        self.y = y
        self.rect = self.icon.get_rect()

    def place(self):
        self.rect.top = self.y
        self.rect.left = self.x
        screen.blit(self.icon, self.rect)


class Troop(object):
    def __init__(self, x, y, address):
        self.x = x
        self.y = y
        self.icon = pygame.image.load(address).convert_alpha()
        self.rect = self.icon.get_rect()

    def place(self):
        self.rect.top = self.y
        self.rect.left = self.x
        screen.blit(self.icon, self.rect)

    def attack(self):
        print(self)
        pass


def clicked(attacks, x, y):
    for i in range(len(attacks)):
        if attacks[i].rect.collidepoint(x, y):
            attacks[i].attack()
            break


def place(seq):
    for i in range(len(seq)):
        seq[i].place()