from Aurora.Packages.dependencies import *

# -------------------------------------------------------------

screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
screen_height = screen.get_height() - 40
screen_width = screen.get_width()


def sh(percentage):
    """Takes fraction of screen height in percentage
     and returns the corresponding value in pixels."""
    return int(percentage*screen_height/100)


def sw(percentage):
    """Takes fraction of screen width in percentage
    and returns the corresponding value in pixels."""
    return int(percentage*screen_width/100)


def pix_w(pix):
    """Takes fraction of screen width in pixels
    and returns the corresponding value in percentage."""
    return pix*(100/screen_width)


def pix_h(pix):
    """Takes fraction of screen height in pixels
    and returns the corresponding value in percentage."""
    return pix*(100/screen_height)


def position_troop(x):
    """This function should return coordinates where a troop should be placed by taking its x co-ordinate
    formula to be referred : y = -sqrt{r^{2}-x^{2}}"""
    pass


def set_level(levels, n):
    levels[n].place()
# ----------------------------------------------------------


def hover_place(icon, rect, hover=True):
    """This function places an image over a rect,
    The images placed have a default hover effect which can be removed."""
    if hover and rect.collidepoint(pygame.mouse.get_pos()):
        hicon = icon.copy()
        hicon.fill((32, 32, 32), special_flags=pygame.BLEND_RGB_SUB)
        screen.blit(hicon, rect)
    else:
        screen.blit(icon, rect)


def clicked(attacks, x, y):
    """Calls the attack method of a image in a given sequence if it has been clicked"""
    for i in range(len(attacks)):
        if attacks[i].rect.collidepoint(x, y):
            attacks[i].attack()
            break


def batch_place(seq):
    """Places an array of images on screen"""
    for i in range(len(seq)):
        seq[i].place()


def change_active_state(seq, val):
    for x in seq:
        x.is_active = val


# ----------------------------------------------------------
class GameLoop(object):
    def __init__(self):
        self.running = True
        self.index = 'home'
        self.color = (0, 0, 40)

    def set_screen(self):
        screen.fill(self.color)

    def handle_quit(self, event):
        if event.type == pygame.QUIT:
            self.running = False


class Control(object):
    """Class to manage all control icons"""
    def __init__(self, y, file, x=sw(50)):
        base_dir = 'Images/icons/'
        self.icon = pygame.image.load(os.path.join(base_dir, file)).convert_alpha()
        self.x = int(x - (self.icon.get_width() / 2))
        self.y = int(y - (self.icon.get_height() / 2))
        self.rect = self.icon.get_rect()
        self.rect.top = self.y
        self.rect.left = self.x
        self.is_active = False

    def place(self):
        """Place an instance of the class on specified rect"""
        hover_place(self.icon, self.rect)


class Text(object):
    """Class to handle to Text Output"""
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.font = pygame.font.SysFont('showcardgothic', self.size)
        self.text = ''
        self.color = (255, 255, 255)

    def write(self, txt):
        """Add to string"""
        self.text += txt

    def clear(self):
        """Clear the text string"""
        self.text = ''

    def render(self):
        """Renders text on the screen"""
        text_surface = self.font.render(self.text, True, self.color)
        screen.blit(text_surface, (self.x, self.y))


class TextInput(Text):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)
        self.width = 500
        self.rect = pygame.Rect(self.x, self.y, self.width, size+2)
        self.active_color = pygame.Color('green')
        self.passive_color = pygame.Color('lightskyblue')
        self.color = self.passive_color
        self.is_selected = False

    def try_selecting(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if self.rect.collidepoint(x, y):
                self.is_selected = True
                self.color = self.active_color
            else:
                self.is_selected = False
                self.color = self.passive_color

    def take_input(self, event):
        if event.type == pygame.KEYDOWN:
            if self.is_selected:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.write(event.unicode)

    def handle_events(self, event):
        self.try_selecting(event)
        self.take_input(event)

    def render(self):
        pygame.draw.rect(screen, self.color, self.rect, 1)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 3))
        self.rect.w = max(self.width, text_surface.get_width() + 15)


class Planet(object):
    """Class to manage Planets"""
    def __init__(self, file, base_rating):
        base_dir = 'Images/Planet/'
        self.icon = pygame.image.load(os.path.join(base_dir, file)).convert_alpha()
        self.x = int(sw(50) - (self.icon.get_width() / 2))
        self.y = int(sh(2) + 128 - (self.icon.get_height() / 2))
        self.rect = self.icon.get_rect()
        self.rect.top = self.y
        self.rect.left = self.x

        self.base_rating = base_rating
        self.damage = base_rating*0.1
        self.health = base_rating
        self.defence = base_rating*0.01

    def place(self):
        screen.blit(self.icon, self.rect)

    def attack(self):
        pass


class Attacks(object):
    """Parent class for Troop and Spell class"""
    def __init__(self, x, y, file, base_dir, base_rating):
        self.x = x
        self.y = y
        self.icon = pygame.image.load(os.path.join(base_dir, file)).convert_alpha()
        self.rect = self.icon.get_rect()
        self.rect.top = self.y - self.icon.get_width()/2
        self.rect.left = self.x - self.icon.get_height()/2
        self.base_Rating = base_rating
        self.damage = self.base_Rating

    def place(self):
        hover_place(self.icon, self.rect)

    def attack(self):
        print(self)
        pass


class Spell(Attacks):
    """Class to manage Spells
    Parent class : Attacks"""
    def __init__(self, x, y, file, base_rating=0):
        base_dir = 'Images/32px/'
        super().__init__(x, y, file, base_dir, base_rating)


class Troop(Attacks):
    """Class to manage Troops
    Parent class : Attacks"""
    def __init__(self, x, y, file, base_rating):
        base_dir = 'Images/32px/'
        # calling initializer of parent class to set common variables up
        super().__init__(x, y, file, base_dir, base_rating)
        self.defence = self.base_Rating*0.5
        self.health = self.base_Rating*0.75

        # loading corresponding troop images
        troop_dir = 'Images/64px/'
        self.img = pygame.image.load(os.path.join(troop_dir, file)).convert_alpha()
        self.rectT = self.img.get_rect()
