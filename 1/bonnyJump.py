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

bonnyJumpScareCounter = 0
Counter = 0

# pygame init
pygame.init()
pygame.font.init()
pygame.mixer.init()

# pygame display
win = pygame.display.set_mode((win_width, win_height), pygame.SCALED | pygame.FULLSCREEN | pygame.HWSURFACE)
pygame.display.set_caption(winCaption)
pygame.display.set_icon(icon)
pygame.mouse.set_visible(False)

# animations
bonnyJumpScareAnimation = [pygame.image.load(bonnyFolder + '1.png').convert(),
                           pygame.image.load(bonnyFolder + '2.png').convert(),
                           pygame.image.load(bonnyFolder + '3.png').convert(),
                           pygame.image.load(bonnyFolder + '4.png').convert(),
                           pygame.image.load(bonnyFolder + '5.png').convert(),
                           pygame.image.load(bonnyFolder + '6.png').convert(),
                           pygame.image.load(bonnyFolder + '7.png').convert(),
                           pygame.image.load(bonnyFolder + '8.png').convert(),
                           pygame.image.load(bonnyFolder + '9.png').convert(),
                           pygame.image.load(bonnyFolder + '10.png').convert(),
                           pygame.image.load(bonnyFolder + '11.png').convert()]

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
    if Counter == 1:
        scareSound.play()

    win.blit(bonnyJumpScareAnimation[bonnyJumpScareCounter], (bonnyJumpScareX, bonnyJumpScareY))

    bonnyJumpScareCounter += 1
    Counter += 1

    if Counter == 241:
        run = False

    if bonnyJumpScareCounter == len(bonnyJumpScareAnimation):
        bonnyJumpScareCounter = 0

    # update
    pygame.display.update()

# quit
pygame.quit()
os.system('python die.py')