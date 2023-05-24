# lib
import pygame
from colorama import init, Fore, Back
from version import ver
from night1Settings import *
from textures import *
from sounds import *
from save import *
import os
import random

# colorama
init()
print(Fore.BLACK, Back.RED, ver, Fore.RESET, Back.RESET)

# variables
run = True
clock = pygame.time.Clock()

fiveX, fiveY = 415, 180
sixX, sixY = 415, 300

Counter = 1
night2 = night
night2 += 1

# pygame init
pygame.init()
pygame.font.init()
pygame.mixer.init()

# pygame display
win = pygame.display.set_mode((win_width, win_height), pygame.SCALED | pygame.FULLSCREEN | pygame.HWSURFACE)
pygame.display.set_caption(winCaption)
pygame.display.set_icon(icon)
pygame.mouse.set_visible(False)

# display
while run:
    # update
    clock.tick(FPS)
    win.fill(BLACK)

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False

    key = pygame.key.get_pressed()

    if key[pygame.K_BACKSPACE]: run = False

    # blit
    win.blit(five, (fiveX, fiveY))
    win.blit(six, (sixX, sixY))
    win.blit(Background, (BackgroundX, BackgroundY))

    if fiveY >= 100:
        fiveY -= 0.5
    if sixY >= 180:
        sixY -= 0.5

    if Counter == 1:
        clockSounds.play()
    elif Counter == 300:
        childrenSounds.play()
    elif Counter == 485:
        run = False

    Counter += 1

    # update
    pygame.display.update()

# quit
pygame.quit()

with open('save.py', 'w') as f:
    f.write('change = True\nnight = ' + str(night2))

os.system('python main.py')