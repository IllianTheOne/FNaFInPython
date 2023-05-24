# lib
import pygame
from link import *

# pygame init
pygame.init()
pygame.mixer.init()

# menu
boopSound = pygame.mixer.Sound(mainSoundsFolder + 'boop.mp3')
scareSound = pygame.mixer.Sound(mainSoundsFolder + 'scream.mp3')
wallkingSound = pygame.mixer.Sound(mainSoundsFolder + 'Animatronics/wallking.mp3')
windowscareSound = pygame.mixer.Sound(mainSoundsFolder + 'Animatronics/windowscare.mp3')
boop2 = pygame.mixer.Sound(mainSoundsFolder + 'boop2.mp3')

# office
lampSound = pygame.mixer.Sound(officeSoundsFolder + 'lamps.mp3')
doorSound = pygame.mixer.Sound(officeSoundsFolder + 'door.mp3')
call1Sounds = pygame.mixer.Sound(officeSoundsFolder + 'call1.mp3')
cameraSound = pygame.mixer.Sound(cameraSoundsFolder + 'put down.put up.mp3')
cameraIdleSound = pygame.mixer.Sound(cameraSoundsFolder + 'CameraIdle.mp3')
powerdownSound = pygame.mixer.Sound(officeSoundsFolder + 'powerdown.mp3')

# freddy
musicboxSound = pygame.mixer.Sound(freedySoundsFolder + 'musicbox.mp3')

# chica
kitchenSound1 = pygame.mixer.Sound(chicaFolderSounds + 'kitchen1.mp3')
kitchenSound2 = pygame.mixer.Sound(chicaFolderSounds + 'kitchen2.mp3')
kitchenSound3 = pygame.mixer.Sound(chicaFolderSounds + 'kitchen3.mp3')
kitchenSound4 = pygame.mixer.Sound(chicaFolderSounds + 'kitchen4.mp3')

# end
clockSounds = pygame.mixer.Sound(Am6 + 'Clock.mp3')
childrenSounds = pygame.mixer.Sound(Am6 + 'Children.mp3')