from Aurora.Packages.screen_dimensions import *


def hover_place(icon, rect):
    if rect.collidepoint(pygame.mouse.get_pos()):
        hicon = icon.copy()
        hicon.fill((32, 32, 32), special_flags=pygame.BLEND_RGB_SUB)
        screen.blit(hicon, rect)
    else:
        screen.blit(icon, rect)


class Spell(object):
    def __init__(self, x, y, file):
        base_dir = 'Images/32px/'
        self.x = x
        self.y = y
        self.icon = pygame.image.load(os.path.join(base_dir, file)).convert_alpha()
        self.rect = self.icon.get_rect()
        self.rect.top = self.y
        self.rect.left = self.x

    def place(self):
        hover_place(self.icon, self.rect)

    def attack(self):
        print(self)
        pass


class Planet(object):
    def __init__(self, file):
        base_dir = 'Images/Planet/'
        self.icon = pygame.image.load(os.path.join(base_dir, file)).convert_alpha()
        self.x = int(sw(50) - (self.icon.get_width() / 2))
        self.y = int(sh(2) + 128 - (self.icon.get_height() / 2))
        self.rect = self.icon.get_rect()
        self.rect.top = self.y
        self.rect.left = self.x

    def place(self):
        screen.blit(self.icon, self.rect)

    def attack(self):
        pass


class Control(object):
    def __init__(self, y, file):
        base_dir = 'Images/icons/'
        self.icon = pygame.image.load(os.path.join(base_dir, file)).convert_alpha()
        self.x = int(sw(50) - (self.icon.get_width() / 2))
        self.y = y
        self.rect = self.icon.get_rect()
        self.rect.top = self.y
        self.rect.left = self.x

    def place(self):
        hover_place(self.icon, self.rect)


class Troop(object):
    def __init__(self, x, y, file):
        base_dir = 'Images/32px/'
        self.x = x
        self.y = y
        self.icon = pygame.image.load(os.path.join(base_dir, file)).convert_alpha()
        self.rect = self.icon.get_rect()
        self.rect.top = self.y
        self.rect.left = self.x
        troop_dir = 'Images/64px/'
        self.img = pygame.image.load(os.path.join(troop_dir, file)).convert_alpha()
        self.rectT = self.img.get_rect()

    def place(self):
        hover_place(self.icon, self.rect)

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


class Text(object):

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.font = pygame.font.Font(None, self.size)
        self.text = ''
        self.color = (255, 255, 255)

    def write(self, txt):
        self.text += txt

    def render(self):
        text_surface = self.font.render(self.text, True, self.color)
        screen.blit(text_surface, (self.x, self.y))


class GameLoop(object):
    def __init__(self):
        self.running = True
        self.color = (0, 0, 40)

    def if_quit(self):
        if pygame.event.type == pygame.QUIT:
            self.running = False

    def execute(self):
        while self.running:
            screen.fill(self.color)
            pygame.display.update()
