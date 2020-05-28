# initializing pygame
import pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)

# title and icon
pygame.display.set_caption("The helios attack")
icon = pygame.image.load('image/icon.png')
pygame.display.set_icon(icon)

# loading images
poison_ = pygame.image.load('Image/32px/poison.png')
fire_ = pygame.image.load('Image/32px/fire.png')
plasma_ = pygame.image.load('Image/32px/plasma_small.png')
goc_ = pygame.image.load('Image/32px/space.png')


# putting images on screen
def spells():
    screen.blit(poison_, (10, 660))
    screen.blit(fire_, (50, 660))
    screen.blit(plasma_, (90, 660))
    screen.blit(goc_, (130, 660))


def troops():
    pass


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


"""
GAME LOOPS BELOW
"""


# Menu Loop
def menu():
    active = True
    while active:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False


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
                if 10+32 > x > 10 and 660+32 > y > 660:
                    poison()
                elif 50+32 > x > 10 and 660+32 > y > 660:
                    fire()
                elif 90+32 > x > 10 and 660+32 > y > 660:
                    plasma()
                elif 130+32 > x > 10 and 660+32 > y > 660:
                    goc()

        spells()
        pygame.display.update()


'''
GAMES FLOW OF CONTROL
'''
pygame.quit()
