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

firstNoiseCounter = 0
Counter = 0
Counter1 = 0

# pygame init
pygame.init()
pygame.font.init()
pygame.mixer.init()

# pygame display
win = pygame.display.set_mode((win_width, win_height), pygame.SCALED | pygame.FULLSCREEN | pygame.HWSURFACE)
pygame.display.set_caption(winCaption)
pygame.display.set_icon(icon)
pygame.mouse.set_visible(False)

# animations, convert and set_colorkey
firstNoiseAnimation = [pygame.image.load(thirdNoiseLink + '1.png').convert_alpha(),
                       pygame.image.load(thirdNoiseLink + '2.png').convert_alpha(),
                       pygame.image.load(thirdNoiseLink + '3.png').convert_alpha(),
                       pygame.image.load(thirdNoiseLink + '4.png').convert_alpha(),
                       pygame.image.load(thirdNoiseLink + '5.png').convert_alpha(),
                       pygame.image.load(thirdNoiseLink + '6.png').convert_alpha(),
                       pygame.image.load(thirdNoiseLink + '7.png').convert_alpha(),
                       pygame.image.load(thirdNoiseLink + '8.png').convert_alpha()]

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

    if Counter == 50:
        if Counter1 <= 600:
            win.blit(end, (endX, endY))
        else:
            run = False

        Counter1 += 1
    else:
        win.blit(firstNoiseAnimation[firstNoiseCounter], (firstNoiseX, firstNoiseY))

        firstNoiseCounter += 1

        if firstNoiseCounter == len(firstNoiseAnimation):
            firstNoiseCounter = 0
            Counter += 1
    # update
    pygame.display.update()

# quit
pygame.quit()
os.system('python main.py')