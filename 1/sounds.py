# lib
import pygame
from link import *

# pygame init
pygame.init()
pygame.mixer.init()

# menu
boopSound = pygame.mixer.Sound(mainSoundsFolder + 'boop.mp3')

# office
lampSound = pygame.mixer.Sound(officeSoundsFolder + 'lamps.mp3')
doorSound = pygame.mixer.Sound(officeSoundsFolder + 'door.mp3')
lampSound = pygame.mixer.Sound(officeSoundsFolder + 'lamps.mp3')
doorSound = pygame.mixer.Sound(officeSoundsFolder + 'door.mp3')
call1Sounds = pygame.mixer.Sound(officeSoundsFolder + 'call1.mp3')
cameraSound = pygame.mixer.Sound(cameraSoundsFolder + 'put down.put up.mp3')