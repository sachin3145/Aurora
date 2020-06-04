from Aurora.Packages.temp import *


# title and icon
pygame.display.set_caption("The Helios Attack")
icon = pygame.image.load('Images/icon.png')
pygame.display.set_icon(icon)

poison = Spell(sw(0.73), sh(90.66), 'Images/32px/poison.png')
fire = Spell(sw(3.66), sh(90.66), 'Images/32px/fire.png')
plasma = Spell(sw(6.59), sh(90.66), 'Images/32px/plasma_small.png')
goc = Spell(sw(9.51), sh(90.66), 'Images/32px/space.png')

mercury = Planet('Images/Planet/mercury.png')
venus = Planet('Images/Planet/venus.png')
earth = Planet('Images/Planet/earth.png')
mars = Planet('Images/Planet/mars.png')
jupiter = Planet('Images/Planet/jupiter.png')
saturn = Planet('Images/Planet/saturn.png')
uranus = Planet('Images/Planet/uranus.png')
neptune = Planet('Images/Planet/neptune.png')

# loading images

demogorgon_ = pygame.image.load('Images/32px/demogorgonx32.png')
elysium_ = pygame.image.load('Images/32px/elysiumx32.png')
armada_ = pygame.image.load('Images/32px/armadax32.png')
nemesis_ = pygame.image.load('Images/32px/nemesisx32.png')
mandalore_ = pygame.image.load('Images/32px/mandalorex32.png')
benzamite_ = pygame.image.load('Images/32px/benzamitex32.png')
tardis_ = pygame.image.load('Images/32px/tardisx32.png')
delta_ = pygame.image.load('Images/32px/deltax32.png')
sun_ = pygame.image.load('Images/Planet/sun.png')
demogorgonT = pygame.image.load('Images/64px/demogorgonx64.png')
elysiumT = pygame.image.load('Images/64px/elysiumx64.png')
armadaT = pygame.image.load('Images/64px/armadax64.png')
nemesisT = pygame.image.load('Images/64px/nemesisx64.png')
mandaloreT = pygame.image.load('Images/64px/mandalorex64.png')
benzamiteT = pygame.image.load('Images/64px/benzamitex64.png')
tardisT = pygame.image.load('Images/64px/tardisx64.png')
deltaT = pygame.image.load('Images/64px/deltax64.png')
# ----------------------------------------------------------------------------------------------------------


# putting images on screen
def spells():
    poison.place()
    fire.place()
    plasma.place()
    goc.place()


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
    start = Control(sh(50)-167, 'Images/start_icon.png')
    high = Control(sh(50)-50, 'Images/highscores_icon.png')
    htp = Control(sh(50)+71, 'Images/how_to_play_icon.png')


# mouse click events
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
        mercury.place()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
#                print(x, y)

                # calling function if mouse is clicked when cursor is over dimensions of specific image
                if sw(0.73)+32 > x > sw(0.73) and sh(90.66)+32 > y > sh(90.66):
                    poison.attack()
                elif sw(3.66)+32 > x > sw(3.66) and sh(90.66)+32 > y > sh(90.66):
                    fire.attack()
                elif sw(6.59)+32 > x > sw(6.59) and sh(90.66)+32 > y > sh(90.66):
                    plasma.attack()
                elif sw(9.51)+32 > x > sw(9.51) and sh(90.66)+32 > y > sh(90.66):
                    goc.attack()
                elif sw(87.55) + 32 > x > sw(87.55) and sh(84.89) + 32 > y > sh(84.89):
                    demogorgon()
                elif sw(90.48) + 32 > x > sw(90.48) and sh(84.89) + 32 > y > sh(84.89):
                    elysium()
                elif sw(93.41) + 32 > x > sw(93.41) and sh(84.89) + 32 > y > sh(84.89):
                    armada()
                elif sw(96.34) + 32 > x > sw(96.34) and sh(84.89) + 32 > y > sh(84.89):
                    nemesis()
                elif sw(87.55) + 32 > x > sw(87.55) and sh(90.66) + 32 > y > sh(90.66):
                    mandalore()
                elif sw(90.48) + 32 > x > sw(90.48) and sh(90.66) + 32 > y > sh(90.66):
                    benzamite()
                elif sw(93.41) + 32 > x > sw(93.41) and sh(90.66) + 32 > y > sh(90.66):
                    tardis()
                elif sw(96.34) + 32 > x > sw(96.34) and sh(90.66) + 32 > y > sh(90.66):
                    delta()


# -------------------------------------------------------------------------------------------------------------------


'''
GAMES FLOW OF CONTROL
'''
menu()

pygame.quit()
