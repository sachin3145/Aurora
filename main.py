from Aurora.Packages.temp import *


# title and icon
pygame.display.set_caption("The Helios Attack")
icon = pygame.image.load('Images/icons/icon.png')
pygame.display.set_icon(icon)

poison = Spell(sw(0.73), sh(90.66), 'poison.png')
fire = Spell(sw(3.66), sh(90.66), 'fire.png')
plasma = Spell(sw(6.59), sh(90.66), 'plasma_small.png')
goc = Spell(sw(9.51), sh(90.66), 'space.png')

mercury = Planet('mercury.png', 1000)
venus = Planet('venus.png', 2000)
earth = Planet('earth.png', 6000)
mars = Planet('mars.png', 4000)
jupiter = Planet('jupiter.png', 15000)
saturn = Planet('saturn.png', 12000)
uranus = Planet('uranus.png', 8000)
neptune = Planet('neptune.png', 10000)

start = Control(sh(50)-167, 'start_icon.png')
high = Control(sh(50)-50, 'high.png')
htp = Control(sh(50)+71, 'htp.png')

demogorgon = Troop(sw(87.55), sh(84.89), 'demogorgon.png', 1500)
elysium = Troop(sw(90.48), sh(84.89), 'elysium.png', 1200)
armada = Troop(sw(93.41), sh(84.89), 'armada.png', 1000)
nemesis = Troop(sw(96.34), sh(84.89), 'nemesis.png', 800)
mandalore = Troop(sw(87.55), sh(90.66), 'mandalore.png', 600)
benzamite = Troop(sw(90.48), sh(90.66), 'benzamite.png', 400)
tardis = Troop(sw(93.41), sh(90.66), 'tardis.png', 200)
delta = Troop(sw(96.34), sh(90.66), 'delta.png', 100)


controls = [start, high, htp]
attacks = [poison, fire, plasma, goc, demogorgon, elysium, armada, nemesis, mandalore, benzamite, tardis, delta][::-1]


# loading images
sun_ = pygame.image.load('Images/Planet/sun.png')


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


"""
GAMES FLOW OF CONTROL
"""
menu()

pygame.quit()
