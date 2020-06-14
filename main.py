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

start = Control(sh(50)-118, 'start_icon.png')
high = Control(sh(50), 'high.png')
htp = Control(sh(50)+129, 'htp.png')
login = Control(sh(50)-100, 'login.png')
register = Control(sh(50), 'register.png')
play_as_guest = Control(sh(50)+100, 'play_as_guest.png')
cont = Control(sh(80), 'continue.png')

demogorgon = Troop(sw(88.65), sh(85.99), 'demogorgon.png', 1500)
elysium = Troop(sw(91.58), sh(85.99), 'elysium.png', 1200)
armada = Troop(sw(94.51), sh(85.99), 'armada.png', 1000)
nemesis = Troop(sw(97.51), sh(85.99), 'nemesis.png', 800)
mandalore = Troop(sw(88.65), sh(92.86), 'mandalore.png', 600)
benzamite = Troop(sw(91.58), sh(92.86), 'benzamite.png', 400)
tardis = Troop(sw(94.51), sh(92.86), 'tardis.png', 200)
delta = Troop(sw(97.51), sh(92.86), 'delta.png', 100)


controls = [start, high, htp]
auth_controls = [login, register, play_as_guest]
attacks = [poison, fire, plasma, goc, demogorgon, elysium, armada, nemesis, mandalore, benzamite, tardis, delta][::-1]


# loading images
sun_ = pygame.image.load('Images/Planet/sun.png')


"""
GAME LOOPS BELOW
"""


# Menu Loop
def menu():
    loop = GameLoop()
    while loop.running:
        loop.set_screen()

        if loop.index == 'home':
            batch_place(controls)
        elif loop.index == 'htp':
            pass
            # code to get text from htp file and render it over screen

        pygame.display.update()

        for event in pygame.event.get():
            loop.handle_quit(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start.rect.collidepoint(pygame.mouse.get_pos()):
                    auth()
                    loop.running = False
                elif htp.rect.collidepoint(pygame.mouse.get_pos()):
                    loop.index = 'htp'


def auth():
    """UNDER DEVELOPMENT NOT YET READY EVEN FOR BETA TESTS"""
    nickname = TextInput(sw(50), sh(30), 64)
    capt = Text(sw(10), sh(30), 64)
    capt.write('NICKNAME')
    loop = GameLoop()
    while loop.running:
        loop.set_screen()
        if loop.index == 'home':
            change_active_state(auth_controls, True)
            batch_place(auth_controls)
        elif loop.index == 'login':
            change_active_state(auth_controls, False)
            capt.render()
            nickname.render()
        elif loop.index == 'register':
            change_active_state(auth_controls, False)
            pass

        pygame.display.update()
        for event in pygame.event.get():
            loop.handle_quit(event)
            nickname.handle_events(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if login.is_active and login.rect.collidepoint(x, y):
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
        mercury.place()
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
