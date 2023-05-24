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

Counter = 0
left = True
tick = 0 # The End: 32040
power = 100
usageNow = 1
usageDeley = 500
cameraOn = False
cameraBlackFill = False
cameraNow = 'A'
bonnyLocation = 'A'
chicaLocation = 'A'
freddyLocation = 'A'
foxyLocation = 'G'
foxyStage = 1
goldenFreddy = None
camImageXMove = None
zeroUsage = False
die = False
bonnyScream = False
chicaScream = False
DeleyBonny = 0
DeleyChica = 0

FRandint = True
FRandintValue = None
LRandint = True
LRandintValue = None
GRandint = True
GRandintValue = None
ORandint = True
ORandintValue = None
PRandint = True
PRandintValue = None
ARandint = True
ARandintValue = None

buttonLeftDoor = False
buttonLeftLight = False
buttonRightDoor = False
buttonRightLight = False

thirdNoiseCounter = 8-1
firstNoiseCounter = 0
secondNoiseCounter = 0
fanCounter = 0
leftDoorCounter = 15-1
rightDoorCounter = 15-1
camFlipCounter = 11-1
pointCounter = 0
pointCounter1 = False
leftHallwayCounter = 0
call1SkipDeley = 0
freddyJumpScareCounter = 0
bonnyJumpScareCounter = 0
chicaJumpScareCounter = 0
zeroUsageDeley = 0
foxyDeley = 0 # 2700

buttonLeftDoorDeley, buttonLeftDoorDeleyTime = False, 20
buttonLeftLightDeley, buttonLeftLightDeleyTime = False, 20
buttonRightDoorDeley, buttonRightDoorDeleyTime = False, 20
buttonRightLightDeley, buttonRightLightDeleyTime = False, 20
cameraDeley, cameraDeleyTime = False, 15
boop2Deley, boop2DeleyTime = False, 10

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
if True: # This is necessary so that during development it is possible to hide it, and it does not take up space on the monitor
    firstNoiseAnimation = [pygame.image.load(thirdNoiseLink + '1.png').convert_alpha(),
                           pygame.image.load(thirdNoiseLink + '2.png').convert_alpha(),
                           pygame.image.load(thirdNoiseLink + '3.png').convert_alpha(),
                           pygame.image.load(thirdNoiseLink + '4.png').convert_alpha(),
                           pygame.image.load(thirdNoiseLink + '5.png').convert_alpha(),
                           pygame.image.load(thirdNoiseLink + '6.png').convert_alpha(),
                           pygame.image.load(thirdNoiseLink + '7.png').convert_alpha(),
                           pygame.image.load(thirdNoiseLink + '8.png').convert_alpha()]

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

    thirdNoiseAnimation = [pygame.image.load(secondNoiseLink + '1.png').convert_alpha(),
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
                            pygame.image.load(secondNoiseLink + '15.png').convert_alpha(),
                            pygame.image.load(secondNoiseLink + '16.png').convert_alpha()]

    fanAnimation = [pygame.image.load(fanFolder + '1.png').convert(),
                    pygame.image.load(fanFolder + '2.png').convert(),
                    pygame.image.load(fanFolder + '3.png').convert()]

    leftDoorCloseAnimation = [pygame.image.load(doorLeftCloseFolder + '1.png').convert(),
                              pygame.image.load(doorLeftCloseFolder + '2.png').convert(),
                              pygame.image.load(doorLeftCloseFolder + '3.png').convert(),
                              pygame.image.load(doorLeftCloseFolder + '4.png').convert(),
                              pygame.image.load(doorLeftCloseFolder + '5.png').convert(),
                              pygame.image.load(doorLeftCloseFolder + '6.png').convert(),
                              pygame.image.load(doorLeftCloseFolder + '7.png').convert(),
                              pygame.image.load(doorLeftCloseFolder + '8.png').convert(),
                              pygame.image.load(doorLeftCloseFolder + '9.png').convert(),
                              pygame.image.load(doorLeftCloseFolder + '10.png').convert(),
                              pygame.image.load(doorLeftCloseFolder + '11.png').convert(),
                              pygame.image.load(doorLeftCloseFolder + '12.png').convert(),
                              pygame.image.load(doorLeftCloseFolder + '13.png').convert(),
                              pygame.image.load(doorLeftCloseFolder + '14.png').convert(),
                              pygame.image.load(doorLeftCloseFolder + '15.png').convert()]

    rightDoorCloseAnimation = [pygame.image.load(doorRightCloseFolder + '1.png').convert(),
                              pygame.image.load(doorRightCloseFolder + '2.png').convert(),
                              pygame.image.load(doorRightCloseFolder + '3.png').convert(),
                              pygame.image.load(doorRightCloseFolder + '4.png').convert(),
                              pygame.image.load(doorRightCloseFolder + '5.png').convert(),
                              pygame.image.load(doorRightCloseFolder + '6.png').convert(),
                              pygame.image.load(doorRightCloseFolder + '7.png').convert(),
                              pygame.image.load(doorRightCloseFolder + '8.png').convert(),
                              pygame.image.load(doorRightCloseFolder + '9.png').convert(),
                              pygame.image.load(doorRightCloseFolder + '10.png').convert(),
                              pygame.image.load(doorRightCloseFolder + '11.png').convert(),
                              pygame.image.load(doorRightCloseFolder + '12.png').convert(),
                              pygame.image.load(doorRightCloseFolder + '13.png').convert(),
                              pygame.image.load(doorRightCloseFolder + '14.png').convert(),
                              pygame.image.load(doorRightCloseFolder + '15.png').convert()]

    leftDoorOpenAnimation = [pygame.image.load(doorLeftFolder + '14.png').convert(),
                              pygame.image.load(doorLeftFolder + '13.png').convert(),
                              pygame.image.load(doorLeftFolder + '12.png').convert(),
                              pygame.image.load(doorLeftFolder + '11.png').convert(),
                              pygame.image.load(doorLeftFolder + '10.png').convert(),
                              pygame.image.load(doorLeftFolder + '9.png').convert(),
                              pygame.image.load(doorLeftFolder + '8.png').convert(),
                              pygame.image.load(doorLeftFolder + '7.png').convert(),
                              pygame.image.load(doorLeftFolder + '6.png').convert(),
                              pygame.image.load(doorLeftFolder + '5.png').convert(),
                              pygame.image.load(doorLeftFolder + '4.png').convert(),
                              pygame.image.load(doorLeftFolder + '3.png').convert(),
                              pygame.image.load(doorLeftFolder + '2.png').convert(),
                              pygame.image.load(doorLeftFolder + '1.png').convert(),
                              pygame.image.load(doorLeftFolder + '15.png').convert()]

    rightDoorOpenAnimation = [pygame.image.load(doorRightFolder + '14.png').convert(),
                              pygame.image.load(doorRightFolder + '13.png').convert(),
                              pygame.image.load(doorRightFolder + '12.png').convert(),
                              pygame.image.load(doorRightFolder + '11.png').convert(),
                              pygame.image.load(doorRightFolder + '10.png').convert(),
                              pygame.image.load(doorRightFolder + '9.png').convert(),
                              pygame.image.load(doorRightFolder + '8.png').convert(),
                              pygame.image.load(doorRightFolder + '7.png').convert(),
                              pygame.image.load(doorRightFolder + '6.png').convert(),
                              pygame.image.load(doorRightFolder + '5.png').convert(),
                              pygame.image.load(doorRightFolder + '4.png').convert(),
                              pygame.image.load(doorRightFolder + '3.png').convert(),
                              pygame.image.load(doorRightFolder + '2.png').convert(),
                              pygame.image.load(doorRightFolder + '1.png').convert(),
                              pygame.image.load(doorRightFolder + '15.png').convert()]

    camFlipOpen = [pygame.image.load(flipFolder + '1.png').convert_alpha(),
                   pygame.image.load(flipFolder + '2.png').convert_alpha(),
                   pygame.image.load(flipFolder + '3.png').convert_alpha(),
                   pygame.image.load(flipFolder + '4.png').convert_alpha(),
                   pygame.image.load(flipFolder + '5.png').convert_alpha(),
                   pygame.image.load(flipFolder + '6.png').convert_alpha(),
                   pygame.image.load(flipFolder + '7.png').convert_alpha(),
                   pygame.image.load(flipFolder + '8.png').convert_alpha(),
                   pygame.image.load(flipFolder + '9.png').convert_alpha(),
                   pygame.image.load(flipFolder + '10.png').convert_alpha(),
                   pygame.image.load(flipFolder + '11.png').convert_alpha()]

    camFlipClose = [pygame.image.load(flipFolder + '10.png').convert_alpha(),
                   pygame.image.load(flipFolder + '9.png').convert_alpha(),
                   pygame.image.load(flipFolder + '8.png').convert_alpha(),
                   pygame.image.load(flipFolder + '7.png').convert_alpha(),
                   pygame.image.load(flipFolder + '6.png').convert_alpha(),
                   pygame.image.load(flipFolder + '5.png').convert_alpha(),
                   pygame.image.load(flipFolder + '4.png').convert_alpha(),
                   pygame.image.load(flipFolder + '3.png').convert_alpha(),
                   pygame.image.load(flipFolder + '2.png').convert_alpha(),
                   pygame.image.load(flipFolder + '1.png').convert_alpha(),
                   pygame.image.load(flipFolder + '11.png').convert_alpha()]

    leftHallwayWithoutBonnyAnimation = [pygame.image.load(LeftHallwayFolder + '2.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '1.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '1.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '1.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '1.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '2.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '2.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '1.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '1.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '1.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '1.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '2.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '2.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '2.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '1.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '1.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '1.png').convert()]

    leftHallwayWithBonnyAnimation = [pygame.image.load(LeftHallwayFolder + '3.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '1.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '1.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '1.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '1.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '3.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '3.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '1.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '1.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '1.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '1.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '3.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '3.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '3.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '1.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '1.png').convert(),
                                        pygame.image.load(LeftHallwayFolder + '1.png').convert()]

    freddyJumpScareAnimation = [pygame.image.load(freedyFolder + '1.png').convert(),
                                pygame.image.load(freedyFolder + '2.png').convert(),
                                pygame.image.load(freedyFolder + '3.png').convert(),
                                pygame.image.load(freedyFolder + '4.png').convert(),
                                pygame.image.load(freedyFolder + '5.png').convert(),
                                pygame.image.load(freedyFolder + '6.png').convert(),
                                pygame.image.load(freedyFolder + '7.png').convert(),
                                pygame.image.load(freedyFolder + '8.png').convert(),
                                pygame.image.load(freedyFolder + '9.png').convert(),
                                pygame.image.load(freedyFolder + '10.png').convert(),
                                pygame.image.load(freedyFolder + '11.png').convert(),
                                pygame.image.load(freedyFolder + '12.png').convert(),
                                pygame.image.load(freedyFolder + '13.png').convert(),
                                pygame.image.load(freedyFolder + '14.png').convert(),
                                pygame.image.load(freedyFolder + '15.png').convert(),
                                pygame.image.load(freedyFolder + '16.png').convert(),
                                pygame.image.load(freedyFolder + '17.png').convert(),
                                pygame.image.load(freedyFolder + '18.png').convert(),
                                pygame.image.load(freedyFolder + '19.png').convert(),
                                pygame.image.load(freedyFolder + '20.png').convert(),
                                pygame.image.load(freedyFolder + '21.png').convert(),
                                pygame.image.load(freedyFolder + '20.png').convert(),
                                pygame.image.load(freedyFolder + '19.png').convert(),
                                pygame.image.load(freedyFolder + '18.png').convert(),
                                pygame.image.load(freedyFolder + '17.png').convert(),
                                pygame.image.load(freedyFolder + '16.png').convert(),
                                pygame.image.load(freedyFolder + '21.png').convert(),
                                pygame.image.load(freedyFolder + '15.png').convert(),
                                pygame.image.load(freedyFolder + '14.png').convert(),
                                pygame.image.load(freedyFolder + '13.png').convert(),
                                pygame.image.load(freedyFolder + '12.png').convert(),
                                pygame.image.load(freedyFolder + '11.png').convert(),
                                pygame.image.load(freedyFolder + '10.png').convert(),
                                pygame.image.load(freedyFolder + '9.png').convert(),
                                pygame.image.load(freedyFolder + '8.png').convert(),
                                pygame.image.load(freedyFolder + '9.png').convert(),
                                pygame.image.load(freedyFolder + '10.png').convert(),
                                pygame.image.load(freedyFolder + '11.png').convert(),
                                pygame.image.load(freedyFolder + '12.png').convert(),
                                pygame.image.load(freedyFolder + '13.png').convert(),
                                pygame.image.load(freedyFolder + '14.png').convert(),
                                pygame.image.load(freedyFolder + '15.png').convert(),
                                pygame.image.load(freedyFolder + '16.png').convert(),
                                pygame.image.load(freedyFolder + '17.png').convert(),
                                pygame.image.load(freedyFolder + '18.png').convert(),
                                pygame.image.load(freedyFolder + '19.png').convert(),
                                pygame.image.load(freedyFolder + '20.png').convert(),
                                pygame.image.load(freedyFolder + '21.png').convert()]

officeWithEnergy.convert(), night1Night1.convert()
clock12AM.convert(), clock1AM.convert(), clock2AM.convert()
clock3AM.convert(), clock4AM.convert(), clock5AM.convert()
clock6AM.convert()
usage.convert(), powerLeft.convert(), interest.convert()
powerLeft1.convert(), powerLeft2.convert(), powerLeft3.convert()
powerLeft4.convert(), powerLeft5.convert()
buttonLeftFalseFalse.convert(), buttonLeftTrueFalse.convert(), buttonLeftFalseTrue.convert()
buttonLeftTrueTrue.convert()
buttonRightFalseFalse.convert(), buttonRightTrueFalse.convert(), buttonRightFalseTrue.convert()
buttonRightTrueTrue.convert()
CamA.convert_alpha(), CamD.convert_alpha(), CamF.convert_alpha()
CamG.convert_alpha(), CamH.convert_alpha(), CamJ.convert_alpha()
CamK.convert_alpha(), CamL.convert_alpha(), CamO.convert_alpha()
CamP.convert_alpha(), CamS.convert_alpha(), CamOverlay.convert_alpha()
CamPoint.convert()
officeLightLeft.convert(), officeLightRight.convert()
officeWithoutEnergyWithFreddy.convert(), officeLightRightChica.convert()
officeLightLeftBonny.convert()

diningRoom1.convert(), diningRoom2.convert(), diningRoom3.convert()
diningRoom4.convert(), diningRoom5.convert(), diningRoom6.convert()
diningRoomText.convert()

employeesOnly1.convert(), employeesOnly2.convert(), employeesOnly3.convert()
employeesOnly4.convert(), employeesOnlyText.convert()

kitchen1.convert(), kitchenText.convert()

leftCorner1.convert(), leftCorner2.convert(), leftCorner3.convert()
leftCorner4.convert(), leftCorner5.convert(), leftCorner6.convert()
leftCornerText.convert()

leftHallwayText.convert()

pirateCove1.convert(), pirateCove2.convert(), pirateCove3.convert()
pirateCove4.convert(), pirateCove5.convert(), pirateCoveText.convert()

rightCorner1.convert(), rightCorner2.convert(), rightCorner3.convert()
rightCorner4.convert(), rightCorner5.convert(), rightCorner6.convert()
rightCorner7.convert(), rightCorner8.convert(), rightCorner9.convert()
rightCornerText.convert()

rightHallway1.convert(), rightHallway2.convert(), rightHallway3.convert()
rightHallway4.convert(), rightHallway5.convert(), rightHallway6.convert()
rightHallwayText.convert()

stage1.convert(), stage2.convert(), stage3.convert()
stage4.convert(), stage5.convert(), stage6.convert()
stage7.convert(), stageText.convert()

toilets1.convert(), toilets2.convert(), toilets3.convert()
toilets4.convert(), toiletsText.convert()

utilityCloset1.convert(), utilityCloset2.convert(), utilityClosetText.convert()

night1Count.set_colorkey(colorKey)
buttonLeftFalseFalse.set_colorkey(BLACK), buttonLeftTrueFalse.set_colorkey(BLACK)
buttonLeftFalseTrue.set_colorkey(BLACK), buttonLeftTrueTrue.set_colorkey(BLACK)
buttonRightFalseFalse.set_colorkey(BLACK), buttonRightTrueFalse.set_colorkey(BLACK)
buttonRightFalseTrue.set_colorkey(BLACK), buttonRightTrueTrue.set_colorkey(BLACK)
usage.set_colorkey(colorKey), powerLeft.set_colorkey(colorKey), interest.set_colorkey(colorKey)
powerLeft1.set_colorkey(BLACK), powerLeft2.set_colorkey(BLACK), powerLeft3.set_colorkey(BLACK)
powerLeft4.set_colorkey(BLACK), powerLeft5.set_colorkey(BLACK)
CamPoint.set_colorkey(BLACK)

diningRoomText.set_colorkey(colorKey), employeesOnlyText.set_colorkey(colorKey)
kitchenText.set_colorkey(colorKey), leftCornerText.set_colorkey(colorKey)
leftHallwayText.set_colorkey(colorKey), pirateCoveText.set_colorkey(colorKey)
rightCornerText.set_colorkey(colorKey), rightHallwayText.set_colorkey(colorKey)
stageText.set_colorkey(colorKey), toiletsText.set_colorkey(colorKey)
utilityClosetText.set_colorkey(colorKey), kitchen1.set_colorkey(colorKey)

ambienceSoundVolume = pygame.mixer.music.load(officeSoundsFolder + 'ambience.mp3')
fanSoundVolume = pygame.mixer.music.load(officeSoundsFolder + 'fan.mp3')
pygame.mixer.music.set_volume(0.9)
pygame.mixer.music.play(-1)
call1Sounds.play()

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

    if not cameraOn:
        if key[pygame.K_a]:
            left = True
            if buttonRightLight:
                usageNow -= 1
                lampSound.stop()
        if key[pygame.K_d]:
            left = False
            if buttonLeftLight:
                usageNow -= 1
                lampSound.stop()

        if usage != 0:
            if not buttonLeftDoorDeley and not buttonRightDoorDeley:
                if key[pygame.K_q]:
                    if left and buttonLeftDoor: usageNow -= 1
                    elif left and not buttonLeftDoor: usageNow += 1
                    if not left and buttonRightDoor: usageNow -= 1
                    elif not left and not buttonRightDoor: usageNow += 1
            if not buttonLeftLightDeley and not buttonRightLightDeley:
                if key[pygame.K_e]:
                    if left and buttonLeftLight: usageNow -= 1
                    elif left and not buttonLeftLight: usageNow += 1
                    if not left and buttonRightLight: usageNow -= 1
                    elif not left and not buttonRightLight: usageNow += 1

            if left:
                if not buttonLeftDoorDeley:
                    if key[pygame.K_q]:
                        if buttonLeftDoor:
                            doorSound.play()
                            buttonLeftDoor = False
                        else:
                            doorSound.play()
                            buttonLeftDoor = True
                        buttonLeftDoorDeley = True
                        leftDoorCounter = 0
                if not buttonLeftLightDeley:
                    if key[pygame.K_e]:
                        if buttonLeftLight:
                            buttonLeftLight = False
                            lampSound.stop()
                        else:
                            buttonLeftLight = True
                            lampSound.play(-1)
                        buttonLeftLightDeley = True
            else:
                if not buttonRightDoorDeley:
                    if key[pygame.K_q]:
                        if buttonRightDoor:
                            buttonRightDoor = False
                            doorSound.play()
                        else:
                            buttonRightDoor = True
                            doorSound.play()
                        buttonRightDoorDeley = True
                        rightDoorCounter = 0
                if not buttonRightLightDeley:
                    if key[pygame.K_e]:
                        if buttonRightLight:
                            buttonRightLight = False
                            lampSound.stop()
                        else:
                            buttonRightLight = True
                            lampSound.play(-1)
                        buttonRightLightDeley = True

    if power != 0:
        if key[pygame.K_SPACE] or key[pygame.K_c]:
            if not cameraDeley:
                if not cameraOn:
                    cameraOn = True
                    camFlipCounter = 0
                    usageNow += 1
                    FRandint = True
                    LRandint = True
                    GRandint = True
                    ORandint = True
                    PRandint = True
                    ARandint = True
                    cameraSound.play()
                    cameraIdleSound.play(-1)
                    if buttonLeftLight:
                        buttonLeftLight = False
                        usageNow -= 1
                        lampSound.stop()
                    elif buttonRightLight:
                        buttonRightLight = False
                        usageNow -= 1
                        lampSound.stop()
                    if bonnyLocation == 'door' and not buttonLeftDoor:
                        run = False
                        die = 'bonny'
                    if chicaLocation == 'door' and not buttonRightDoor:
                        run = False
                        die = 'chica'
                else:
                    cameraOn = False
                    camFlipCounter = 0
                    cameraBlackFill = False
                    usageNow -= 1
                    cameraSound.play()
                    cameraIdleSound.stop()
                    if bonnyLocation == 'door' and not buttonRightDoor:
                        DeleyBonny -= 300
                    if chicaLocation == 'door' and not buttonLeftDoor:
                        DeleyChica -= 300
                cameraDeley = True

    if key[pygame.K_x]:
        call1SkipDeley = 401
        call1Sounds.stop()

    if cameraDeley:
        if cameraDeleyTime == 0:
            cameraDeley = False
            cameraDeleyTime = 15
        else:
            cameraDeleyTime -= 1

    if buttonLeftDoorDeley:
        if buttonLeftDoorDeleyTime == 0:
            buttonLeftDoorDeley = False
            buttonLeftDoorDeleyTime = 20
        else:
            buttonLeftDoorDeleyTime -= 1
    if buttonLeftLightDeley:
        if buttonLeftLightDeleyTime == 0:
            buttonLeftLightDeley = False
            buttonLeftLightDeleyTime = 20
        else:
            buttonLeftLightDeleyTime -= 1

    if buttonRightDoorDeley:
        if buttonRightDoorDeleyTime == 0:
            buttonRightDoorDeley = False
            buttonRightDoorDeleyTime = 20
        else:
            buttonRightDoorDeleyTime -= 1
    if buttonRightLightDeley:
        if buttonRightLightDeleyTime == 0:
            buttonRightLightDeley = False
            buttonRightLightDeleyTime = 20
        else:
            buttonRightLightDeleyTime -= 1

    if usageDeley == 0 and usageNow == 1:
        usageDeley = 576
        power -= 1
    elif usageDeley == 0 and usageNow == 2:
        usageDeley = 288
        power -= 1
    elif usageDeley == 0 and usageNow == 3:
        usageDeley = 192
        power -= 1
    elif usageDeley == 0 and usageNow == 4:
        usageDeley = 144
        power -= 1
    elif usageDeley == 0 and usageNow == 5:
        usageDeley = 72
        power -= 1

    if left:
        if buttonRightLight: buttonRightLight = False
    else:
        if buttonLeftLight: buttonLeftLight = False

    if camImageX == -320: camImageXMove = False
    elif camImageX == 0: camImageXMove = True

    if 32040 >= tick >= 0: freddyLocation = 'A'

    if 32040 >= tick >= 0:
        foxyLocation = 'G'
        foxyStage = 1

    if 17180 >= tick >= 0: bonnyLocation = 'A'
    elif 17880 >= tick >= 17180: bonnyLocation = 'S2'
    elif 20040 >= tick >= 17880: bonnyLocation = 'F'
    elif 22380 >= tick >= 20040: bonnyLocation = 'K'
    elif 22800 >= tick >= 22380: bonnyLocation = 'L'
    elif 27000 >= tick >= 22800: bonnyLocation = 'door'
    elif 29520 >= tick >= 27000: bonnyLocation = 'K'
    elif 32040 >= tick >= 29520: bonnyLocation = 'J'

    if tick == 20040: wallkingSound.play()
    elif tick == 22380: wallkingSound.play()
    elif tick == 22800: wallkingSound.play()
    elif tick == 27000: wallkingSound.play()
    elif tick == 29520: wallkingSound.play()

    if 24420 >= tick >= 0: chicaLocation = 'A'
    elif 28680 >= tick >= 24420: chicaLocation = 'S1'
    elif 31020 >= tick >= 28680: chicaLocation = 'H'
    elif 32040 >= tick >= 31020: chicaLocation = 'P1'

    if tick == 28680:
        chicaSound = random.randrange(1, 4)
        if chicaSound == 1: kitchenSound1.play()
        elif chicaSound == 2: kitchenSound2.play()
        elif chicaSound == 3: kitchenSound3.play()
        elif chicaSound == 4: kitchenSound4.play()
    elif tick == 29580:
        chicaSound = random.randrange(1, 4)
        if chicaSound == 1: kitchenSound1.play()
        elif chicaSound == 2: kitchenSound2.play()
        elif chicaSound == 3: kitchenSound3.play()
        elif chicaSound == 4: kitchenSound4.play()
    elif tick == 30480:
        chicaSound = random.randrange(1, 4)
        if chicaSound == 1: kitchenSound1.play()
        elif chicaSound == 2: kitchenSound2.play()
        elif chicaSound == 3: kitchenSound3.play()
        elif chicaSound == 4: kitchenSound4.play()

    if tick == 32040:
        run = False
        die = 'win'

    if buttonLeftLight and not bonnyScream and bonnyLocation == 'door':
        bonnyScream = True
        windowscareSound.play()
    if bonnyScream and bonnyLocation != 'door': bonnyScream = False

    if buttonRightLight and not chicaScream and chicaLocation == 'door':
        chicaScream = True
        windowscareSound.play()
    if chicaScream and chicaLocation != 'door': chicaScream = False

    if bonnyLocation == 'door' and not buttonLeftDoor:
        if not cameraOn and DeleyBonny >= 420:
            die = 'bonny'
            run = False
        elif cameraOn and DeleyBonny >= 420:
            die = 'bonny'
            run = False
        DeleyBonny += 1
    else:
        DeleyBonny = 0

    if chicaLocation == 'door' and not buttonRightDoor:
        if not cameraOn and DeleyChica >= 420:
            die = 'chica'
            run = False
        elif cameraOn and DeleyChica >= 420:
            die = 'chica'
            run = False
        DeleyChica += 1
    else:
        DeleyChica = 0

    if key[pygame.K_y] and not boop2Deley:
        boop2.play()
        boop2Deley = True

    if boop2Deley:
        if boop2DeleyTime == 0:
            boop2Deley = False
            boop2DeleyTime = 10
        else:
            boop2DeleyTime -= 1

    # text
    fontText = pygame.font.SysFont("FiveFontsatFreddy's-Regular.ttf", 32)
    powerText = fontText.render(str(power), True, WHITE)
    callSkipText = fontText.render('Skip call - X', True, WHITE)

    # blit
    if power != -1:
        if left:
            if buttonLeftLight:
                if bonnyLocation != 'door':
                    win.blit(officeLightLeft, (officeXLeft, officeYLeft))
                else:
                    win.blit(officeLightLeftBonny, (officeXLeft, officeYLeft))
            else:
                win.blit(officeWithEnergy, (officeXLeft, officeYLeft))

            win.blit(fanAnimation[fanCounter], (fanXRight, fanYRight))

            if buttonLeftLight:
                if buttonLeftDoor:
                    win.blit(buttonLeftTrueTrue, (buttonLeftX, buttonLeftY))
                else:
                    win.blit(buttonLeftFalseTrue, (buttonLeftX, buttonLeftY))
            else:
                if buttonLeftDoor:
                    win.blit(buttonLeftTrueFalse, (buttonLeftX, buttonLeftY))
                else:
                    win.blit(buttonLeftFalseFalse, (buttonLeftX, buttonLeftY))

            if buttonLeftDoor: win.blit(leftDoorCloseAnimation[leftDoorCounter],
                                        (leftDoorAnimationX, leftDoorAnimationY))
            if not buttonLeftDoor: win.blit(leftDoorOpenAnimation[leftDoorCounter],
                                            (leftDoorAnimationX, leftDoorAnimationY))
        else:
            if buttonRightLight:
                if chicaLocation != 'door':
                    win.blit(officeLightRight, (officeXRight, officeYRight))
                else:
                    win.blit(officeLightRightChica, (officeXRight, officeYRight))
            else:
                win.blit(officeWithEnergy, (officeXRight, officeYRight))

            win.blit(fanAnimation[fanCounter], (fanXLeft, fanYLeft))

            if buttonRightLight:
                if buttonRightDoor:
                    win.blit(buttonRightTrueTrue, (buttonRightX, buttonRightY))
                else:
                    win.blit(buttonRightFalseTrue, (buttonRightX, buttonRightY))
            else:
                if buttonRightDoor:
                    win.blit(buttonRightTrueFalse, (buttonRightX, buttonRightY))
                else:
                    win.blit(buttonRightFalseFalse, (buttonRightX, buttonRightY))

            if buttonRightDoor: win.blit(rightDoorCloseAnimation[rightDoorCounter],
                                         (rightDoorAnimationX, rightDoorAnimationY))
            if not buttonRightDoor: win.blit(rightDoorOpenAnimation[rightDoorCounter],
                                             (rightDoorAnimationX, rightDoorAnimationY))

        if cameraOn and not cameraDeley:
            if key[pygame.K_a]:
                cameraNow, thirdNoiseCounter = 'A', 0
                boopSound.play()
                cameraDeley = True
            if key[pygame.K_d]:
                cameraNow, thirdNoiseCounter = 'D', 0
                boopSound.play()
                cameraDeley = True
            if key[pygame.K_f]:
                cameraNow, thirdNoiseCounter = 'F', 0
                boopSound.play()
                cameraDeley = True
            if key[pygame.K_g]:
                cameraNow, thirdNoiseCounter = 'G', 0
                boopSound.play()
                cameraDeley = True
            if key[pygame.K_h]:
                cameraNow, thirdNoiseCounter = 'H', 0
                boopSound.play()
                cameraDeley = True
            if key[pygame.K_j]:
                cameraNow, thirdNoiseCounter = 'J', 0
                boopSound.play()
                cameraDeley = True
            if key[pygame.K_k]:
                cameraNow, thirdNoiseCounter = 'K', 0
                boopSound.play()
                cameraDeley = True
            if key[pygame.K_l]:
                cameraNow, thirdNoiseCounter = 'L', 0
                boopSound.play()
                cameraDeley = True
            if key[pygame.K_o]:
                cameraNow, thirdNoiseCounter = 'O', 0
                boopSound.play()
                cameraDeley = True
            if key[pygame.K_p]:
                cameraNow, thirdNoiseCounter = 'P', 0
                boopSound.play()
                cameraDeley = True
            if key[pygame.K_s]:
                cameraNow, thirdNoiseCounter = 'S', 0
                boopSound.play()
                cameraDeley = True

        if cameraBlackFill:
            win.fill(BLACK)

            if cameraNow == 'A':
                if ARandint:
                    ARandintValue = random.choices([True, False], weights=[15, 85])
                    ARandint = False

                if bonnyLocation == 'A' and chicaLocation == 'A' and freddyLocation == 'A' and ARandintValue == [False]:
                    win.blit(stage1, (camImageX, camImageY))
                elif bonnyLocation == 'A' and chicaLocation == 'A' and freddyLocation == 'A' and ARandintValue == [
                    True]:
                    win.blit(stage2, (camImageX, camImageY))
                elif bonnyLocation != 'A' and chicaLocation == 'A' and freddyLocation == 'A':
                    win.blit(stage3, (camImageX, camImageY))
                elif bonnyLocation == 'A' and chicaLocation != 'A' and freddyLocation == 'A':
                    win.blit(stage4, (camImageX, camImageY))
                elif bonnyLocation != 'A' and chicaLocation != 'A' and freddyLocation == 'A' and ARandintValue == [
                    False]:
                    win.blit(stage5, (camImageX, camImageY))
                elif bonnyLocation != 'A' and chicaLocation != 'A' and freddyLocation == 'A' and ARandintValue == [
                    True]:
                    win.blit(stage6, (camImageX, camImageY))
                elif bonnyLocation != 'A' and chicaLocation != 'A' and freddyLocation != 'A':
                    win.blit(stage7, (camImageX, camImageY))
            elif cameraNow == 'D':
                if chicaLocation == 'D1' and chicaLocation != 'D2' and freddyLocation != 'D':
                    win.blit(toilets2, (camImageX, camImageY))
                elif chicaLocation != 'D1' and chicaLocation == 'D2' and freddyLocation != 'D':
                    win.blit(toilets3, (camImageX, camImageY))
                elif chicaLocation != 'D1' and chicaLocation != 'D2' and freddyLocation == 'D':
                    win.blit(toilets4, (camImageX, camImageY))
                else:
                    win.blit(toilets1, (camImageX, camImageY))
            elif cameraNow == 'F':
                if FRandint:
                    FRandintValue = random.choices([True, False], weights=(5, 95))
                    FRandint = False

                if bonnyLocation != 'F' and FRandintValue == [True]:
                    win.blit(employeesOnly4, (camImageX, camImageY))
                elif bonnyLocation == 'F' and FRandintValue == [False]:
                    win.blit(employeesOnly2, (camImageX, camImageY))
                elif bonnyLocation == 'F' and FRandintValue == [True]:
                    win.blit(employeesOnly3, (camImageX, camImageY))
                else:
                    win.blit(employeesOnly1, (camImageX, camImageY))
            elif cameraNow == 'G':
                if GRandint:
                    GRandintValue = random.choices([True, False], weights=[10, 90])
                    GRandint = False
                if cameraOn: foxyDeley = 0
                if foxyStage == 4: foxyLocation = 'G2'

                if foxyLocation == 'G' and foxyStage == 1:
                    win.blit(pirateCove1, (camImageX, camImageY))
                elif foxyLocation == 'G' and foxyStage == 2:
                    win.blit(pirateCove2, (camImageX, camImageY))
                elif foxyLocation == 'G' and foxyStage == 3:
                    win.blit(pirateCove3, (camImageX, camImageY))
                elif foxyLocation != 'G' and foxyStage == 4 and GRandintValue == [False]:
                    win.blit(pirateCove4, (camImageX, camImageY))
                elif foxyLocation != 'G' and foxyStage == 4 and GRandintValue == [True]:
                    win.blit(pirateCove5, (camImageX, camImageY))
            elif cameraNow == 'J':
                if bonnyLocation != 'J':
                    win.blit(utilityCloset1, (camImageX, camImageY))
                else:
                    win.blit(utilityCloset2, (camImageX, camImageY))
            elif cameraNow == 'K':
                if bonnyLocation != 'K':
                    win.blit(leftHallwayWithoutBonnyAnimation[leftHallwayCounter], (camImageX, camImageY))
                else:
                    win.blit(leftHallwayWithBonnyAnimation[leftHallwayCounter], (camImageX, camImageY))
            elif cameraNow == 'L':
                if LRandint:
                    LRandintValue = random.choices([True, False, 'GoldenFreddy'], weights=[2, 47, 2])
                    LRandint = False

                if bonnyLocation == 'L' and LRandintValue == [True]:
                    win.blit(leftCorner6, (camImageX, camImageY))
                elif bonnyLocation == 'L' and LRandintValue == [False]:
                    win.blit(leftCorner5, (camImageX, camImageY))
                elif bonnyLocation == 'L' and LRandintValue == ['GoldenFreddy']:
                    win.blit(leftCorner4, (camImageX, camImageY))
                elif bonnyLocation != 'L' and LRandintValue == [False]:
                    win.blit(leftCorner1, (camImageX, camImageY))
                elif bonnyLocation != 'L' and LRandintValue == [True]:
                    win.blit(leftCorner2, (camImageX, camImageY))
                elif bonnyLocation != 'L' and LRandintValue == ['GoldenFreddy']:
                    win.blit(leftCorner3, (camImageX, camImageY))  # Golden Freddy later
            elif cameraNow == 'O':
                if ORandint:
                    ORandintValue = random.choices(['1', '2', '3', '4', False], weights=[1, 1, 1, 1, 96])
                    ORandint = False

                if chicaLocation != 'O' and freddyLocation != 'O' and ORandintValue == [False]:
                    win.blit(rightCorner1, (camImageX, camImageY))
                elif chicaLocation != 'O' and freddyLocation != 'O' and ORandintValue == ['1']:
                    win.blit(rightCorner2, (camImageX, camImageY))
                elif chicaLocation != 'O' and freddyLocation != 'O' and ORandintValue == ['2']:
                    win.blit(rightCorner3, (camImageX, camImageY))
                elif chicaLocation != 'O' and freddyLocation != 'O' and ORandintValue == ['3']:
                    win.blit(rightCorner4, (camImageX, camImageY))
                elif chicaLocation != 'O' and freddyLocation != 'O' and ORandintValue == ['4']:
                    win.blit(rightCorner5, (camImageX, camImageY))
                elif chicaLocation == 'O' and freddyLocation != 'O' and ORandintValue == [False]:
                    win.blit(rightCorner6, (camImageX, camImageY))
                elif chicaLocation == 'O' and freddyLocation != 'O' and ORandintValue == ['1']:
                    win.blit(rightCorner7, (camImageX, camImageY))
                elif chicaLocation == 'O' and freddyLocation != 'O' and ORandintValue == ['2']:
                    win.blit(rightCorner8, (camImageX, camImageY))
                elif chicaLocation != 'O' and freddyLocation == 'O':
                    win.blit(rightCorner9, (camImageX, camImageY))
            elif cameraNow == 'P':
                if PRandint:
                    PRandintValue = random.choices(['1', '2', False], weights=(1, 1, 98))
                    PRandint = False

                if chicaLocation != 'P1' and chicaLocation != 'P2' and freddyLocation != 'P' and PRandintValue == [
                    False]:
                    win.blit(rightHallway1, (camImageX, camImageY))
                elif chicaLocation != 'P1' and chicaLocation != 'P2' and freddyLocation != 'P' and PRandintValue == [
                    '1']:
                    win.blit(rightHallway2, (camImageX, camImageY))
                elif chicaLocation != 'P1' and chicaLocation != 'P2' and freddyLocation != 'P' and PRandintValue == [
                    '2']:
                    win.blit(rightHallway3, (camImageX, camImageY))
                elif chicaLocation == 'P1' and chicaLocation != 'P2' and freddyLocation != 'P':
                    win.blit(rightHallway5, (camImageX, camImageY))
                elif chicaLocation != 'P1' and chicaLocation == 'P2' and freddyLocation != 'P':
                    win.blit(rightHallway6, (camImageX, camImageY))
                elif chicaLocation != 'P1' and chicaLocation != 'P2' and freddyLocation == 'P':
                    win.blit(rightHallway4, (camImageX, camImageY))
            elif cameraNow == 'S':
                if bonnyLocation != 'S1' and bonnyLocation != 'S2' and chicaLocation != 'S1' and chicaLocation != 'S2' and freddyLocation == 'S':
                    win.blit(diningRoom6, (camImageX, camImageY))
                elif bonnyLocation != 'S1' and bonnyLocation != 'S2' and chicaLocation != 'S1' and chicaLocation == 'S2' and freddyLocation != 'S1':
                    win.blit(diningRoom5, (camImageX, camImageY))
                elif bonnyLocation != 'S1' and bonnyLocation != 'S2' and chicaLocation == 'S1' and chicaLocation != 'S2' and freddyLocation != 'S1':
                    win.blit(diningRoom4, (camImageX, camImageY))
                elif bonnyLocation != 'S1' and bonnyLocation == 'S2' and chicaLocation != 'S1' and chicaLocation != 'S2' and freddyLocation != 'S1':
                    win.blit(diningRoom3, (camImageX, camImageY))
                elif bonnyLocation == 'S1' and bonnyLocation != 'S2' and chicaLocation != 'S1' and chicaLocation != 'S2' and freddyLocation != 'S1':
                    win.blit(diningRoom2, (camImageX, camImageY))
                else:
                    win.blit(diningRoom1, (camImageX, camImageY))

            if cameraNow != 'H':
                win.blit(firstNoiseAnimation[firstNoiseCounter], (firstNoiseX, firstNoiseY))
            win.blit(thirdNoiseAnimation[thirdNoiseCounter], (thirdNoiseX, thirdNoiseY))

            if cameraNow == 'A':
                win.blit(stageText, (stageTextX, stageTextY))
                win.blit(CamA, (camMapX, camMapY))
            elif cameraNow == 'D':
                win.blit(toiletsText, (toiletsTextX, toiletsTextY))
                win.blit(CamD, (camMapX, camMapY))
            elif cameraNow == 'F':
                win.blit(employeesOnlyText, (camEmployesOnlyTextX, camEmployesOnlyTextY))
                win.blit(CamF, (camMapX, camMapY))
            elif cameraNow == 'G':
                win.blit(pirateCoveText, (pirateCoveTextX, pirateCoveTextY))
                win.blit(CamG, (camMapX, camMapY))
            elif cameraNow == 'H':
                win.blit(kitchen1, (kitchen1X, kitchen1Y))

                win.blit(kitchenText, (kitchenTextX, kitchenTextY))
                win.blit(CamH, (camMapX, camMapY))
            elif cameraNow == 'J':
                win.blit(utilityClosetText, (utilityClosetTextX, utilityClosetTextY))
                win.blit(CamJ, (camMapX, camMapY))
            elif cameraNow == 'K':
                win.blit(leftHallwayText, (leftHallwayTextX, leftHallwayTextY))
                win.blit(CamK, (camMapX, camMapY))
            elif cameraNow == 'L':
                win.blit(leftCornerText, (leftCornerTextX, leftCornerTextY))
                win.blit(CamL, (camMapX, camMapY))
            elif cameraNow == 'O':
                win.blit(rightCornerText, (rightCornerTextX, rightCornerTextY))
                win.blit(CamO, (camMapX, camMapY))
            elif cameraNow == 'P':
                win.blit(rightHallwayText, (rightHallwayTextX, rightHallwayTextY))
                win.blit(CamP, (camMapX, camMapY))
            elif cameraNow == 'S':
                win.blit(diningRoomText, (camDiningRoomTextX, camDiningRoomTextY))
                win.blit(CamS, (camMapX, camMapY))

            win.blit(CamOverlay, (cameraOverlayX, cameraOverlayY))
            if pointCounter1: win.blit(CamPoint, (cameraPointX, cameraPointY))

        win.blit(night1Night1, (nightX, nightY))
        if 5340 >= tick >= 0:
            win.blit(clock12AM, (clockX, clockY))
        elif 10680 >= tick >= 5340:
            win.blit(clock1AM, (clockX, clockY))
        elif 16020 >= tick >= 10680:
            win.blit(clock2AM, (clockX, clockY))
        elif 21360 >= tick >= 16020:
            win.blit(clock3AM, (clockX, clockY))
        elif 26700 >= tick >= 21360:
            win.blit(clock4AM, (clockX, clockY))
        elif 32040 >= tick >= 26700:
            win.blit(clock5AM, (clockX, clockY))
        elif tick >= 32040:
            win.blit(clock6AM, (clockX, clockY))

        if call1SkipDeley <= 400: win.blit(callSkipText, (callSkipTextX, callSkipTextY))

        win.blit(usage, (usageX, usageY))
        win.blit(powerText, (powerTextX, powerTextY))

        if power == 100:
            win.blit(interest, (interestX, interestY))
        elif 99 >= power >= 10:
            win.blit(interest, (interestX2, interestY2))
        elif 9 >= power >= 0:
            win.blit(interest, (interestX3, interestY3))
        win.blit(powerLeft, (powerLeftX, powerLeftY))

        if usageNow == 1: win.blit(powerLeft1, (usagePowerLeftX, usagePowerLeftY))
        if usageNow == 2: win.blit(powerLeft2, (usagePowerLeftX, usagePowerLeftY))
        if usageNow == 3: win.blit(powerLeft3, (usagePowerLeftX, usagePowerLeftY))
        if usageNow == 4: win.blit(powerLeft4, (usagePowerLeftX, usagePowerLeftY))
        if usageNow == 5: win.blit(powerLeft5, (usagePowerLeftX, usagePowerLeftY))

        if cameraOn:
            win.blit(camFlipOpen[camFlipCounter], (cameraFlipX, cameraFlipY))
        else:
            win.blit(camFlipClose[camFlipCounter], (cameraFlipX, cameraFlipY))

        # ~update
        thirdNoiseCounter += 1
        firstNoiseCounter += 1
        fanCounter += 1
        leftDoorCounter += 1
        rightDoorCounter += 1
        tick += 1
        usageDeley -= 1
        camFlipCounter += 1
        pointCounter += 1
        leftHallwayCounter += 1
        foxyDeley += 1
        if call1SkipDeley <= 400: call1SkipDeley += 1
        if Counter < 275: Counter += 1
        if 215 > Counter > 200: secondNoiseCounter += 1
        if pointCounter == 100:
            if not pointCounter1:
                pointCounter1 = True
            else:
                pointCounter1 = False
            pointCounter = 0

        if camFlipCounter == len(camFlipOpen): camFlipCounter = 11
        if camFlipCounter == len(camFlipClose):
            camFlipCounter = 11 - 1
            if cameraOn: cameraBlackFill = True
        if fanCounter == len(fanAnimation): fanCounter = 0
        if leftDoorCounter == len(leftDoorCloseAnimation): leftDoorCounter = 15 - 1
        if rightDoorCounter == len(rightDoorCloseAnimation): rightDoorCounter = 15 - 1
        if leftDoorCounter == len(leftDoorOpenAnimation): leftDoorCounter = 15 - 1
        if rightDoorCounter == len(rightDoorOpenAnimation): rightDoorCounter = 15 - 1
        if leftHallwayCounter == len(leftHallwayWithoutBonnyAnimation): leftHallwayCounter = 0
        if foxyDeley == 2700 and foxyStage != 4:
            foxyStage += 1
            foxyDeley = 0
        if firstNoiseCounter == len(firstNoiseAnimation): firstNoiseCounter = 0
        if thirdNoiseCounter == len(thirdNoiseAnimation): thirdNoiseCounter = 16 - 1

        if camImageXMove:
            camImageX -= 1
        else:
            camImageX += 1
    else:
        if not zeroUsage:
            if buttonLeftDoor:
                doorSound.play()
                buttonLeftDoor = False
            if buttonRightDoor:
                doorSound.play()
                buttonRightDoor = False
            if cameraOn:
                cameraSound.play()
                cameraIdleSound.stop()
                cameraOn = False
            if buttonLeftLight:
                buttonLeftLight = False
                lampSound.stop()
            if buttonRightLight:
                buttonRightLight = False
                lampSound.stop()
            pygame.mixer.music.stop()
            call1Sounds.stop()
            zeroUsage = True
            powerdownSound.play()
            ambienceSound = pygame.mixer.Sound(officeSoundsFolder + 'ambience.mp3')
            ambienceSound.play(-1)

        if left:
            if zeroUsageDeley <= 1800:
                win.blit(officeWithoutEnergy, (officeXLeft, officeYLeft))
            elif 3000 >= zeroUsageDeley >= 1800:
                win.blit(officeWithoutEnergyWithFreddy, (officeXLeft, officeYLeft))
            if zeroUsageDeley == 1000: wallkingSound.play()
        else:
            win.blit(officeWithoutEnergy, (officeXRight, officeYRight))

        if zeroUsageDeley == 1800:
            musicboxSound.play()
        elif 3500 >= zeroUsageDeley >= 3000:
            win.fill(BLACK)
            ambienceSound.stop()
            musicboxSound.stop()

        if zeroUsageDeley == 3500:
            scareSound.play()
        elif 3700 >= zeroUsageDeley >= 3501:
            win.blit(freddyJumpScareAnimation[freddyJumpScareCounter], (freddyJumpScareX, freddyJumpScareY))
        elif zeroUsageDeley == 3701:
            die = True
            run = False

        zeroUsageDeley += 1
        freddyJumpScareCounter += 1

        if freddyJumpScareCounter == len(freddyJumpScareAnimation): freddyJumpScareCounter = 0

    # update
    pygame.display.update()

# quit
pygame.quit()

if die == True:
    os.system('python die.py')
elif die == 'bonny':
    os.system('python bonnyJump.py')
elif die == 'chica':
    os.system('python chicaJump.py')
elif die == 'win':
    os.system('python 6am.py')