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

start = Control(sh(50)-167, 'Images/start_icon.png')
high = Control(sh(50)-50, 'Images/highscores_icon.png')
htp = Control(sh(50)+71, 'Images/how_to_play_icon.png')

demogorgon = Troop(sw(87.55), sh(84.89), 'Images/32px/demogorgonx32.png')
elysium = Troop(sw(90.48), sh(84.89), 'Images/32px/elysiumx32.png')
armada = Troop(sw(93.41), sh(84.89), 'Images/32px/armadax32.png')
nemesis = Troop(sw(96.34), sh(84.89), 'Images/32px/nemesisx32.png')
mandalore = Troop(sw(87.55), sh(90.66),'Images/32px/mandalorex32.png')
benzamite = Troop(sw(90.48), sh(90.66), 'Images/32px/benzamitex32.png')
tardis = Troop(sw(93.41), sh(90.66), 'Images/32px/tardisx32.png')
delta = Troop(sw(96.34), sh(90.66), 'Images/32px/deltax32.png')


controls = [start, high, htp]
attacks = [poison, fire, plasma, goc, demogorgon, elysium, armada, nemesis, mandalore, benzamite, tardis, delta][::-1]


# loading images

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

"""
GAME LOOPS BELOW
"""


# Menu Loop
def menu():
    active = True

    while active:
        screen.fill((0, 0, 40))
        place(controls)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if start.rect.collidepoint(x, y):
                    game()
                    active = False


# Main loop
def game():
    running = True
    while running:

        screen.fill((0, 0, 40))
        place(attacks)
        mercury.place()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                clicked(attacks, x, y)

'''
GAMES FLOW OF CONTROL
'''
menu()

pygame.quit()
