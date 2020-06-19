from Aurora.Packages.temp import *


# title and icon
pygame.display.set_caption("The Helios Attack")
icon = pygame.image.load('Images/icons/icon.png')
pygame.display.set_icon(icon)

poison = Spell(sw(1.83), sh(92.86), 'poison.png')
fire = Spell(sw(4.76), sh(92.86), 'fire.png')
plasma = Spell(sw(7.66), sh(92.86), 'plasma_small.png')
goc = Spell(sw(10.61), sh(92.86), 'space.png')

mercury = Planet('mercury.png', 1000)
venus = Planet('venus.png', 2000)
earth = Planet('earth.png', 6000)
mars = Planet('mars.png', 4000)
jupiter = Planet('jupiter.png', 15000)
saturn = Planet('saturn.png', 12000)
uranus = Planet('uranus.png', 8000)
neptune = Planet('neptune.png', 10000)

start = Control(sh(50)-100, 'start_icon.png')
high = Control(sh(50), 'high.png')
htp = Control(sh(50)+100, 'htp.png')
login = Control(sh(50)-100, 'login.png')
register = Control(sh(50), 'register.png')
play_as_guest = Control(sh(50)+100, 'play_as_guest.png')
cont = Control(sh(80), 'continue.png')
back = Control(sh(3), 'back.png', sw(97))

demogorgon = Troop(sw(88.65), sh(85.99), 'demogorgon.png', 1500)
elysium = Troop(sw(91.58), sh(85.99), 'elysium.png', 1200)
armada = Troop(sw(94.51), sh(85.99), 'armada.png', 1000)
nemesis = Troop(sw(97.51), sh(85.99), 'nemesis.png', 800)
mandalore = Troop(sw(88.65), sh(92.86), 'mandalore.png', 600)
benzamite = Troop(sw(91.58), sh(92.86), 'benzamite.png', 400)
tardis = Troop(sw(94.51), sh(92.86), 'tardis.png', 200)
delta = Troop(sw(97.51), sh(92.86), 'delta.png', 100)

# loading images
sun = pygame.image.load('Images/Planet/sun.png')


controls = [start, high, htp]
auth_controls = [login, register, play_as_guest]
attacks = [poison, fire, plasma, goc, demogorgon, elysium, armada, nemesis, mandalore, benzamite, tardis, delta][::-1]
levels = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]    # sun will be handled separately

# authentication labels
nickname = TextInput(sw(50), sh(30), 64)
capt = Text(sw(10), sh(30), 64)
capt.write('USERNAME')

"""
GAME LOOPS BELOW
"""


def menu():

    loop = MenuLoop()
    while loop.running:
        loop.set_screen()

        if loop.index == 'home':
            change_active_state(controls, True)
            change_active_state(auth_controls, False)
            batch_place(controls)
        elif loop.index == 'htp':
            pass
        elif loop.index == 'high':
            pass
        elif loop.index == 'start':
            change_active_state(controls, False)
            change_active_state(auth_controls, True)
            batch_place(auth_controls)
        elif loop.index == 'login':
            capt.render()
            nickname.render()
            cont.place()

        pygame.display.update()
        for event in pygame.event.get():
            loop.handle_quit(event)

            if loop.index == 'login':
                nickname.handle_events(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if start.is_active and start.rect.collidepoint(x, y):
                    loop.index = 'start'
                elif htp.is_active and htp.rect.collidepoint(x, y):
                    loop.index = 'htp'
                elif high.is_active and high.rect.collidepoint(x, y):
                    loop.index = 'high'
                elif login.is_active and login.rect.collidepoint(x, y):
                    loop.index = 'login'
                elif register.is_active and register.rect.collidepoint(x, y):
                    loop.index = 'register'
                elif play_as_guest.is_active and play_as_guest.rect.collidepoint(x, y):
                    game()
                    loop.running = False


# Main loop
def game():
    loop = GameLoop()
    while loop.running:
        loop.set_screen()
        batch_place(attacks)
        set_level(levels, 0)
        pygame.display.update()
        for event in pygame.event.get():
            loop.handle_quit(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                clicked(attacks, x, y)


"""
GAMES FLOW OF CONTROL
"""
menu()

pygame.quit()
