from Aurora.Packages.temp import *


# title and icon
pygame.display.set_caption("The Helios Attack")
icon = pygame.image.load('Images\\icons\\icon.png')
pygame.display.set_icon(icon)

ray_of_sickness = Spell(sw(1.83), sh(92.86), 'ray_of_sickness.png')
incinerate = Spell(sw(4.76), sh(92.86), 'incinerate.png')
plasma_discharge = Spell(sw(7.66), sh(92.86), 'plasma_discharge.png')
god_of_chaos = Spell(sw(10.61), sh(92.86), 'god_of_chaos.png')

mercury = Planet('mercury.png', 500)
venus = Planet('venus.png', 1000)
earth = Planet('earth.png', 3000)
mars = Planet('mars.png', 2000)
jupiter = Planet('jupiter.png', 7500)
saturn = Planet('saturn.png', 6000)
uranus = Planet('uranus.png', 4000)
neptune = Planet('neptune.png', 12500)

start = Control(sh(50)-100, 'start_icon.png')
high = Control(sh(50), 'high.png')
htp = Control(sh(50)+100, 'htp.png')
login = Control(sh(50)-100, 'login.png')
register = Control(sh(50), 'register.png')
play_as_guest = Control(sh(50)+100, 'play_as_guest.png')
cont = Control(sh(80), 'continue.png')

delta = Troop(sw(97.51), sh(92.86), 'delta.png')
tardis = Troop(sw(94.51), sh(92.86), 'tardis.png')
benzamite = Troop(sw(91.58), sh(92.86), 'benzamite.png')
mandalore = Troop(sw(88.65), sh(92.86), 'mandalore.png')
nemesis = Troop(sw(97.51), sh(85.99), 'nemesis.png')
armada = Troop(sw(94.51), sh(85.99), 'armada.png')
elysium = Troop(sw(91.58), sh(85.99), 'elysium.png')
demogorgon = Troop(sw(88.65), sh(85.99), 'demogorgon.png')

# loading images
sun = pygame.image.load('Images\\Planet\\sun.png')


controls = [start, high, htp]
auth_controls = [login, register, play_as_guest]
troops = [delta, tardis, benzamite, mandalore, nemesis, armada, elysium, demogorgon]
spells = [ray_of_sickness, incinerate, plasma_discharge, god_of_chaos]
attacks = spells + troops
attacks = attacks[::-1]

levels = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]    # sun will be handled separately

# authentication input box
username = TextInput(sw(75), sh(30)-1, 64)

# how to play text
with open('./Documentation/HOWTOPLAY.txt') as text:
    htp_text_list = text.read().splitlines()

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
            change_active_state(controls, False)
            y = sw(5)
            for htp_text in htp_text_list:
                render_text(htp_text, sw(50), y)
                y += 40
        elif loop.index == 'high':
            pass
        elif loop.index == 'start':
            change_active_state(controls, False)
            change_active_state(auth_controls, True)
            batch_place(auth_controls)
        elif loop.index == 'login':
            change_active_state(auth_controls, False)
            render_text('USERNAME', sw(25), sh(30), 64)
            username.render()
            if player_exists(username.text.upper()):
                cont.is_active = True
                cont.place()
            else:
                render_text('PLEASE ENTER YOUR USERNAME', cont.rect.center[0], cont.rect.center[1], 32)
        elif loop.index == 'register':
            cont.is_active = True
            change_active_state(auth_controls, False)
            render_text('USERNAME', sw(25), sh(30), 64)
            username.render()
            if username.text.upper() != '' and not player_exists(username.text.upper()):
                cont.place()
            elif username.text.upper() == '':
                render_text('PLEASE CHOOSE A USERNAME', cont.rect.center[0], cont.rect.center[1], 32)
            else:
                render_text('USERNAME NOT AVAILABLE', cont.rect.center[0], cont.rect.center[1], 32)

        pygame.display.update()
        for event in pygame.event.get():
            loop.handle_quit(event)

            if loop.index in ('login', 'register'):
                username.handle_events(event)

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
                elif cont.is_active and cont.rect.collidepoint(x, y):
                    if loop.index == 'register':
                        create_player(username.text)
                    game(username.text)
                    loop.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if loop.index in ['start', 'high', 'htp']:
                        loop.index = 'home'
                    elif loop.index in ['login', 'register']:
                        loop.index = 'start'


pygame.time.set_timer(pygame.USEREVENT + 1, 5000)


# Main loop
def game(player_name='GUEST'):
    loop = GameLoop(player_name)
    loop.set_attributes(spells, 'spell')
    loop.set_attributes(troops, 'troop')
    loop.check_unlocks(troops, 'troop')
    loop.check_unlocks(spells, 'spell')
    while loop.running:
        loop.set_screen()
        Troop.update_troops()
        batch_place(attacks)
        loop.set_level(levels)
        if loop.index != 'options':
            loop.planet_health_bar()
            loop.energy_bar()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if loop.player_name != 'GUEST':
                    loop.save_progress('troop', troops)
                    loop.save_progress('spell', spells)
                    loop.save_progress('overall')
                p.close()
                db.close()
                loop.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                clicked(attacks, x, y)
                if loop.index == 'options' and sh(37.5) < y < sh(62.5):
                    loop.index = ''
                    if sw(0) < x < sw(50):
                        loop.index = 'upgrades'
                    else:
                        loop.player_level += 1
                        loop.update_unlocks(troops, 'troop')
                        loop.update_unlocks(spells, 'spell')
            elif event.type == pygame.USEREVENT+1:
                Cache.recover_energy()


def upgrades(player_name='GUEST'):

    pass


"""
GAMES FLOW OF CONTROL
"""

menu()
pygame.quit()
