# lib
import pygame
from colorama import init, Fore, Back
from version import ver
from night1Settings import *
from textures import *
from sounds import *
from save import *
import os

# colorama
init()
print(Fore.BLACK, Back.RED, ver, Fore.RESET, Back.RESET)

# variables
run = True
clock = pygame.time.Clock()

Counter = 0
secondNoiseCounter = 0

# pygame init
pygame.init()
pygame.font.init()
pygame.mixer.init()

# pygame display
win = pygame.display.set_mode((win_width, win_height), pygame.SCALED | pygame.FULLSCREEN | pygame.HWSURFACE)
pygame.display.set_caption(winCaption)
pygame.display.set_icon(icon)
pygame.mouse.set_visible(False)

# animations, convert, set_colorkey
newspaperAnimation = [pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),
            pygame.image.load(textFolder + 'newspaper.png').convert(),]

secondNoiseAnimation = [pygame.image.load(secondNoiseLink + '1.png').convert_alpha(),
                        pygame.image.load(secondNoiseLink + '2.png').convert_alpha(),
                        pygame.image.load(secondNoiseLink + '3.png').convert_alpha(),
                        pygame.image.load(secondNoiseLink + '4.png').convert_alpha(),
                        pygame.image.load(secondNoiseLink + '5.png').convert_alpha(),
                        pygame.image.load(secondNoiseLink + '6.png').convert_alpha(),
                        pygame.image.load(secondNoiseLink + '7.png').convert_alpha(),
                        pygame.image.load(secondNoiseLink + '8.png').convert_alpha(),
                        pygame.image.load(secondNoiseLink + '9.png').convert_alpha(),
                        pygame.image.load(secondNoiseLink + '10.png').convert_alpha(),
                        pygame.image.load(secondNoiseLink + '11.png').convert_alpha(),
                        pygame.image.load(secondNoiseLink + '12.png').convert_alpha(),
                        pygame.image.load(secondNoiseLink + '13.png').convert_alpha(),
                        pygame.image.load(secondNoiseLink + '14.png').convert_alpha(),
                        pygame.image.load(secondNoiseLink + '15.png').convert_alpha()]

night1Count.convert()
night1Count.set_colorkey(colorKey)

# display
while run:
    # update
    clock.tick(newspapperFPS)
    win.fill(BLACK)

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False

    key = pygame.key.get_pressed()

    if key[pygame.K_BACKSPACE]: run = False

    if Counter == 275:
        boopSound.play()
        run = False

    # blit
    if 275 > Counter > 215: win.blit(night1Count, (night1CountX, night1CountY))

    if Counter < 200:
        win.blit(newspaperAnimation[Counter], (newspaperX, newspaperY))
    elif 215 > Counter > 200:
        win.blit(secondNoiseAnimation[secondNoiseCounter], (secondNoiseX, secondNoiseX))

    # update
    pygame.display.update()

    if Counter < 275: Counter += 1
    if 215 > Counter > 200:
        secondNoiseCounter += 1

    if Counter == 200: boopSound.play()

# quit
pygame.quit()

os.system('python night1.py')