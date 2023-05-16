# lib
import pygame
from link import *

# pygame init
pygame.init()

# main
icon = pygame.image.load(iconLink)

# menu
FNaF = pygame.image.load(textFolder + 'text.png')
scott = pygame.image.load(textFolder + 'scott.png')
Continue = pygame.image.load(buttonsLink + 'continue.png')
newGame = pygame.image.load(buttonsLink + 'new_game.png')
arrow = pygame.image.load(textFolder + 'arrow.png')

# night1
night1Count = pygame.image.load(nightCounterLink + 'counter/1.png')

# night main
officeWithEnergy = pygame.image.load(officeFolder + '1.png')
officeLightLeft = pygame.image.load(officeFolder + '2.png')
officeLightRight = pygame.image.load(officeFolder + '3.png')

buttonLeftFalseFalse = pygame.image.load(buttonLeftFolder + '1.png')
buttonLeftTrueFalse = pygame.image.load(buttonLeftFolder + '2.png')
buttonLeftFalseTrue = pygame.image.load(buttonLeftFolder + '3.png')
buttonLeftTrueTrue = pygame.image.load(buttonLeftFolder + '4.png')

buttonRightFalseFalse = pygame.image.load(buttonRightFolder + '1.png')
buttonRightTrueFalse = pygame.image.load(buttonRightFolder + '2.png')
buttonRightFalseTrue = pygame.image.load(buttonRightFolder + '3.png')
buttonRightTrueTrue = pygame.image.load(buttonRightFolder + '4.png')

clock12AM = pygame.image.load(clockFolder + '12.png')
clock1AM = pygame.image.load(clockFolder + '1.png')
clock2AM = pygame.image.load(clockFolder + '2.png')
clock3AM = pygame.image.load(clockFolder + '3.png')
clock4AM = pygame.image.load(clockFolder + '4.png')
clock5AM = pygame.image.load(clockFolder + '5.png')
clock6AM = pygame.image.load(clockFolder + '6.png')

night1Night1 = pygame.image.load(nightCounterLink + '1.png')

usage = pygame.image.load(batteryFolder + 'usage.png')
powerLeft = pygame.image.load(batteryFolder + 'power.png')
interest = pygame.image.load(batteryFolder + 'interest.png')

powerLeft1 = pygame.image.load(batteryFolder + '1.png')
powerLeft2 = pygame.image.load(batteryFolder + '2.png')
powerLeft3 = pygame.image.load(batteryFolder + '3.png')
powerLeft4 = pygame.image.load(batteryFolder + '4.png')
powerLeft5 = pygame.image.load(batteryFolder + '5.png')