import pygame
from ctypes import windll

# --------------------------------------------------------------------------------------------------------
user32 = windll.user32
screen_width, screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1) - 40
screensize = screen_width, screen_height


def sh(percentage):
    return int(percentage*screen_height/100)


def sw(percentage):
    return int(percentage*screen_width/100)


def pix_w(pix):
    return pix*(100/screen_width)


def pix_h(pix):
    return pix*(100/screen_height)

# -----------------------------------------------------------------------------------------------------------


# initializing pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)

# title and icon
pygame.display.set_caption("The Helios Attack")
icon = pygame.image.load('image/icon.png')
pygame.display.set_icon(icon)

# loading images
poison_ = pygame.image.load('Image/32px/poison.png')
fire_ = pygame.image.load('Image/32px/fire.png')
plasma_ = pygame.image.load('Image/32px/plasma_small.png')
goc_ = pygame.image.load('Image/32px/space.png')
start_ = pygame.image.load('Image/start_icon.png')
startH_ = pygame.image.load('Image/start_icon_hover.png')

# ----------------------------------------------------------------------------------------------------------


# putting images on screen
def spells():
    screen.blit(poison_, (sw(0.73), sh(90.66)))
    screen.blit(fire_, (sw(3.66), sh(90.66)))
    screen.blit(plasma_, (sw(6.59), sh(90.66)))
    screen.blit(goc_, (sw(9.51), sh(90.66)))


def troops():
    pass


def controls():
    screen.blit(start_, (sw(50)-148, sh(50)-132))

# ------------------------------------------------------------------------------------------------------------


# mouse click events
def poison():
    print('Poison')
    pass


def fire():
    print('Incinerate')
    pass


def plasma():
    print('Plasma')
    pass


def goc():
    print('God of Chaos')
    pass

# -------------------------------------------------------------------------------------------------------------------


"""
GAME LOOPS BELOW
"""


# Menu Loop
def menu():
    active = True
    while active:
        screen.fill((0, 0, 40))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(x, y)
                if sw(45.31)+296 > x > sw(45.31) and sh(28.11)+294 > y > sh(28.11):
                    game()
                    active = False


        controls()
        pygame.display.update()


# Main loop
def game():
    running = True
    while running:

        screen.fill((0, 0, 40))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                print(x, y)

                # calling function if mouse is clicked when cursor is over dimensions of specific image
                if sw(0.73)+32 > x > sw(0.73) and sh(90.66)+32 > y > sh(90.66):
                    poison()
                elif sw(3.66)+32 > x > sw(3.66) and sh(90.66)+32 > y > sh(90.66):
                    fire()
                elif sw(6.59)+32 > x > sw(6.59) and sh(90.66)+32 > y > sh(90.66):
                    plasma()
                elif sw(9.51)+32 > x > sw(9.51) and sh(90.66)+32 > y > sh(90.66):
                    goc()

        spells()
        pygame.display.update()

# -------------------------------------------------------------------------------------------------------------------


'''
GAMES FLOW OF CONTROL
'''
menu()

pygame.quit()
