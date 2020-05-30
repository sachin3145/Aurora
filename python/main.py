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
high_ = pygame.image.load('Image/highscores_icon.png')
htp_ = pygame.image.load('Image/how_to_play_icon.png')
demogorgon_ = pygame.image.load('Image/32px/demogorgonx32.png')
elysium_ = pygame.image.load('Image/32px/elysiumx32.png')
armada_ = pygame.image.load('Image/32px/armadax32.png')
nemesis_ = pygame.image.load('Image/32px/nemesisx32.png')
mandalore_ = pygame.image.load('Image/32px/mandalorex32.png')
benzamite_ = pygame.image.load('Image/32px/benzamitex32.png')
tardis_ = pygame.image.load('Image/32px/tardisx32.png')
delta_ = pygame.image.load('Image/32px/deltax32.png')
# ----------------------------------------------------------------------------------------------------------


# putting images on screen
def spells():
    screen.blit(poison_, (sw(0.73), sh(90.66)))
    screen.blit(fire_, (sw(3.66), sh(90.66)))
    screen.blit(plasma_, (sw(6.59), sh(90.66)))
    screen.blit(goc_, (sw(9.51), sh(90.66)))


def troops():
    screen.blit(demogorgon_, (sw(87.55), sh(84.89)))
    screen.blit(elysium_, (sw(90.48), sh(84.89)))
    screen.blit(armada_, (sw(93.41), sh(84.89)))
    screen.blit(nemesis_, (sw(96.34), sh(84.89)))
    screen.blit(mandalore_, (sw(87.55), sh(90.66)))
    screen.blit(benzamite_, (sw(90.48), sh(90.66)))
    screen.blit(tardis_, (sw(93.41), sh(90.66)))
    screen.blit(delta_, (sw(96.34), sh(90.66)))


def controls():
    screen.blit(start_, (sw(50)-132, sh(50)-167))
    screen.blit(high_, (sw(50)-149, sh(50)-50))
    screen.blit(htp_, (sw(50)-168, sh(50)+71))
# -----------------------------------------------------------------------------------------------------------


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


def demogorgon():
    print("demogorgon")
    pass


def elysium():
    print("elysium")
    pass


def armada():
    print("armada")
    pass


def nemesis():
    print("nemesis")
    pass


def mandalore():
    print("mandalore")
    pass


def benzamite():
    print("benzamite")
    pass


def tardis():
    print("tardis")
    pass


def delta():
    print("delta")
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
        controls()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
#                print(x, y)
                if sw(50)+132 > x > sw(50)-132 and sh(50)-167+97 > y > sh(50)-167:
                    game()
                    active = False


# Main loop
def game():
    running = True
    while running:

        screen.fill((0, 0, 40))
        spells()
        troops()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
#                print(x, y)

                # calling function if mouse is clicked when cursor is over dimensions of specific image
                if sw(0.73)+32 > x > sw(0.73) and sh(90.66)+32 > y > sh(90.66):
                    poison()
                elif sw(3.66)+32 > x > sw(3.66) and sh(90.66)+32 > y > sh(90.66):
                    fire()
                elif sw(6.59)+32 > x > sw(6.59) and sh(90.66)+32 > y > sh(90.66):
                    plasma()
                elif sw(9.51)+32 > x > sw(9.51) and sh(90.66)+32 > y > sh(90.66):
                    goc()
                elif sw(87.55)+32 > x > sw(87.55) and sh(84.89)+32 > y > sh(84.89):
                    demogorgon()
                elif sw(90.48)+32 > x > sw(90.48) and sh(84.89)+32 > y > sh(84.89):
                    elysium()
                elif sw(93.41)+32 > x > sw(93.41) and sh(84.89)+32 > y > sh(84.89):
                    armada()
                elif sw(96.34)+32 > x > sw(96.34) and sh(84.89)+32 > y > sh(84.89):
                    nemesis()

# -------------------------------------------------------------------------------------------------------------------


'''
GAMES FLOW OF CONTROL
'''
menu()

pygame.quit()
