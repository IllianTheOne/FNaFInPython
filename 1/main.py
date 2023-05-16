# lib
import pygame
from colorama import init, Fore, Back
from version import ver
from mainSettings import *
from textures import *
from sounds import *
from save import *
import os

# colorama
init()
print(Fore.BLACK, Back.RED, ver, Fore.RESET, Back.RESET)

# save
if not change:
    with open('save.py', 'w') as f: f.write(saveDescription)
    os.system('python main.py')

# variables
run = True
clock = pygame.time.Clock()

choise = 1
nightCounter = night

choiseDeley, choiseDeleyTime = False, 5

freddyMainCounter = 0
firstNoiseCounter = 0
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

# animations, convert and set_colorkey
freddyMainAnimation = [pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '2.png').convert(),
                       pygame.image.load(freddyMainLink + '2.png').convert(),
                       pygame.image.load(freddyMainLink + '2.png').convert(),
                       pygame.image.load(freddyMainLink + '2.png').convert(),
                       pygame.image.load(freddyMainLink + '2.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '1.png').convert(),
                       pygame.image.load(freddyMainLink + '3.png').convert(),
                       pygame.image.load(freddyMainLink + '3.png').convert(),
                       pygame.image.load(freddyMainLink + '3.png').convert(),
                       pygame.image.load(freddyMainLink + '3.png').convert(),
                       pygame.image.load(freddyMainLink + '3.png').convert(),
                       pygame.image.load(freddyMainLink + '4.png').convert(),
                       pygame.image.load(freddyMainLink + '4.png').convert()]

firstNoiseAnimation = [pygame.image.load(firstNoiseLink + '1.png').convert_alpha(),
                       pygame.image.load(firstNoiseLink + '2.png').convert_alpha(),
                       pygame.image.load(firstNoiseLink + '3.png').convert_alpha(),
                       pygame.image.load(firstNoiseLink + '4.png').convert_alpha(),
                       pygame.image.load(firstNoiseLink + '5.png').convert_alpha(),
                       pygame.image.load(firstNoiseLink + '6.png').convert_alpha(),
                       pygame.image.load(firstNoiseLink + '7.png').convert_alpha(),
                       pygame.image.load(firstNoiseLink + '8.png').convert_alpha()]

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

nightTexture = [pygame.image.load(nightCounterLink + '1.png').convert_alpha(),
                pygame.image.load(nightCounterLink + '2.png').convert_alpha(),
                pygame.image.load(nightCounterLink + '3.png').convert_alpha(),
                pygame.image.load(nightCounterLink + '4.png').convert_alpha(),
                pygame.image.load(nightCounterLink + '5.png').convert_alpha(),
                pygame.image.load(nightCounterLink + '6.png').convert_alpha(),
                pygame.image.load(nightCounterLink + '7.png').convert_alpha()]

icon.convert(), FNaF.convert(), scott.convert()

FNaF.set_colorkey(colorKey), scott.set_colorkey(colorKey), Continue.set_colorkey(colorKey)
newGame.set_colorkey(colorKey), arrow.set_colorkey(colorKey)

# music
pygame.mixer.Sound(menuMusicLink).play(-1, 0, 0)

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

    if key[pygame.K_RETURN]:
        if choise == 1: choise = 3
        else: choise = 4
        run = False

    if not choiseDeley:
        if key[pygame.K_w]:
            if choise == 1: choise = 2
            else: choise = 1
            choiseDeley = True
            boopSound.play()
        if key[pygame.K_s]:
            if choise == 2: choise = 1
            else: choise = 2
            choiseDeley = True
            boopSound.play()

    # deleys
    if choiseDeley:
        if choiseDeleyTime == 0:
            choiseDeley = False
            choiseDeleyTime = 5
        else: choiseDeleyTime -= 1

    # text
    fontText = pygame.font.SysFont("FiveFontsatFreddy's-Regular.ttf", 24)
    verText = fontText.render(ver, True, WHITE)

    # blit
    win.blit(freddyMainAnimation[freddyMainCounter], (freddyMainX, freddyMainY))
    win.blit(firstNoiseAnimation[firstNoiseCounter], (firstNoiseX, firstNoiseX))
    win.blit(secondNoiseAnimation[secondNoiseCounter], (secondNoiseX, secondNoiseY))

    win.blit(FNaF, (FNaFX, FNaFY))
    win.blit(scott, (scottX, scottY))
    win.blit(verText, (verTextX, verTextY))

    win.blit(newGame, (newGameX, newGameY))
    win.blit(Continue, (ContinueX, ContinueY))
    if choise == 1: win.blit(arrow, (arrowX1, arrowY1))
    else:win.blit(arrow, (arrowX2, arrowY2)), win.blit(nightTexture[nightCounter-1], (nightTextureX, nightTextureY))

    # update
    pygame.display.update()

    freddyMainCounter += 1
    firstNoiseCounter += 1
    secondNoiseCounter += 1

    if freddyMainCounter >= len(freddyMainAnimation): freddyMainCounter = 0
    if firstNoiseCounter >= len(firstNoiseAnimation): firstNoiseCounter = 0
    if secondNoiseCounter >= len(secondNoiseAnimation): secondNoiseCounter = 0

# quit
pygame.quit()

if choise == 3:
    with open('save.py', 'w') as f: f.write(saveDescription)
    os.system('python night' + str(night) + '.py')
if choise == 4: os.system('python night' + str(night) + '.py')