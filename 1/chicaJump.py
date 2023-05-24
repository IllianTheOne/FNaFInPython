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

chicaJumpScareCounter = 0
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
chicaJumpScareAnimation = [pygame.image.load(chicaFolder + '1.png').convert(),
                           pygame.image.load(chicaFolder + '2.png').convert(),
                           pygame.image.load(chicaFolder + '3.png').convert(),
                           pygame.image.load(chicaFolder + '4.png').convert(),
                           pygame.image.load(chicaFolder + '5.png').convert(),
                           pygame.image.load(chicaFolder + '6.png').convert(),
                           pygame.image.load(chicaFolder + '7.png').convert(),
                           pygame.image.load(chicaFolder + '8.png').convert(),
                           pygame.image.load(chicaFolder + '9.png').convert(),
                           pygame.image.load(chicaFolder + '10.png').convert(),
                           pygame.image.load(chicaFolder + '11.png').convert(),
                           pygame.image.load(chicaFolder + '12.png').convert(),
                           pygame.image.load(chicaFolder + '13.png').convert(),
                           pygame.image.load(chicaFolder + '14.png').convert(),
                           pygame.image.load(chicaFolder + '15.png').convert(),
                           pygame.image.load(chicaFolder + '16.png').convert()]

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

    win.blit(chicaJumpScareAnimation[chicaJumpScareCounter], (bonnyJumpScareX, bonnyJumpScareY))

    chicaJumpScareCounter += 1
    Counter += 1

    if Counter == 241:
        run = False

    if chicaJumpScareCounter == len(chicaJumpScareAnimation):
        chicaJumpScareCounter = 0

    # update
    pygame.display.update()

# quit
pygame.quit()
os.system('python die.py')