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
left = True
tick = 0 # The End: 21600
power = 100
usageNow = 1
usageDeley = 500

buttonLeftDoor = False
buttonLeftLight = False
buttonRightDoor = False
buttonRightLight = False

secondNoiseCounter = 0
fanCounter = 0
leftDoorCounter = 15-1
rightDoorCounter = 15-1

buttonLeftDoorDeley, buttonLeftDoorDeleyTime = False, 20
buttonLeftLightDeley, buttonLeftLightDeleyTime = False, 20
buttonRightDoorDeley, buttonRightDoorDeleyTime = False, 20
buttonRightLightDeley, buttonRightLightDeleyTime = False, 20

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
night1Count.set_colorkey(colorKey)
buttonLeftFalseFalse.set_colorkey(BLACK), buttonLeftTrueFalse.set_colorkey(BLACK)
buttonLeftFalseTrue.set_colorkey(BLACK), buttonLeftTrueTrue.set_colorkey(BLACK)
buttonRightFalseFalse.set_colorkey(BLACK), buttonRightTrueFalse.set_colorkey(BLACK)
buttonRightFalseTrue.set_colorkey(BLACK), buttonRightTrueTrue.set_colorkey(BLACK)
usage.set_colorkey(colorKey), powerLeft.set_colorkey(colorKey), interest.set_colorkey(colorKey)
powerLeft1.set_colorkey(BLACK), powerLeft2.set_colorkey(BLACK), powerLeft3.set_colorkey(BLACK)
powerLeft4.set_colorkey(BLACK), powerLeft5.set_colorkey(BLACK)

ambienceSoundVolume = pygame.mixer.music.load(officeSoundsFolder + 'ambience.mp3')
fanSoundVolume = pygame.mixer.music.load(officeSoundsFolder + 'fan.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

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
        usageDeley = 500
        power -= 1
    elif usageDeley == 0 and usageNow == 2:
        usageDeley = 450
        power -= 2
    elif usageDeley == 0 and usageNow == 3:
        usageDeley = 375
        power -= 3
    elif usageDeley == 0 and usageNow == 4:
        usageDeley = 350
        power -= 3
    elif usageDeley == 0 and usageNow == 5:
        usageDeley = 200
        power -= 4

    if left:
        if buttonRightLight: buttonRightLight = False
    else:
        if buttonLeftLight: buttonLeftLight = False

    # text
    fontText = pygame.font.SysFont("FiveFontsatFreddy's-Regular.ttf", 32)
    powerText = fontText.render(str(power), True, WHITE)

    # blit
    if left:
        if buttonLeftLight: win.blit(officeLightLeft, (officeWithEnergyXLeft, officeWithEnergyYLeft))
        else: win.blit(officeWithEnergy, (officeWithEnergyXLeft, officeWithEnergyYLeft))

        win.blit(fanAnimation[fanCounter], (fanXRight, fanYRight))

        if buttonLeftLight:
            if buttonLeftDoor: win.blit(buttonLeftTrueTrue, (buttonLeftX, buttonLeftY))
            else: win.blit(buttonLeftFalseTrue, (buttonLeftX, buttonLeftY))
        else:
            if buttonLeftDoor: win.blit(buttonLeftTrueFalse, (buttonLeftX, buttonLeftY))
            else: win.blit(buttonLeftFalseFalse, (buttonLeftX, buttonLeftY))

        if buttonLeftDoor: win.blit(leftDoorCloseAnimation[leftDoorCounter], (leftDoorAnimationX, leftDoorAnimationY))
        if not buttonLeftDoor: win.blit(leftDoorOpenAnimation[leftDoorCounter], (leftDoorAnimationX, leftDoorAnimationY))
    else:
        if buttonRightLight: win.blit(officeLightRight, (officeWithEnergyXRight, officeWithEnergyYRight))
        else: win.blit(officeWithEnergy, (officeWithEnergyXRight, officeWithEnergyYRight))

        win.blit(fanAnimation[fanCounter], (fanXLeft, fanYLeft))

        if buttonRightLight:
            if buttonRightDoor: win.blit(buttonRightTrueTrue, (buttonRightX, buttonRightY))
            else: win.blit(buttonRightFalseTrue, (buttonRightX, buttonRightY))
        else:
            if buttonRightDoor: win.blit(buttonRightTrueFalse, (buttonRightX, buttonRightY))
            else: win.blit(buttonRightFalseFalse, (buttonRightX, buttonRightY))

        if buttonRightDoor: win.blit(rightDoorCloseAnimation[rightDoorCounter], (rightDoorAnimationX, rightDoorAnimationY))
        if not buttonRightDoor: win.blit(rightDoorOpenAnimation[rightDoorCounter], (rightDoorAnimationX, rightDoorAnimationY))

    win.blit(night1Night1, (nightX, nightY))
    if 3085 >= tick >= 0: win.blit(clock12AM, (clockX, clockY))
    elif 6170 >= tick >= 3085: win.blit(clock1AM, (clockX, clockY))
    elif 9255 >= tick >= 6170: win.blit(clock2AM, (clockX, clockY))
    elif 12340 >= tick >= 9255: win.blit(clock3AM, (clockX, clockY))
    elif 15425 >= tick >= 12340: win.blit(clock4AM, (clockX, clockY))
    elif 18510 >= tick >= 15425: win.blit(clock5AM, (clockX, clockY))
    elif 21595 >= tick >= 18510: win.blit(clock6AM, (clockX, clockY))
    elif tick == 21600: pass

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

    # update
    pygame.display.update()

    fanCounter += 1
    leftDoorCounter += 1
    rightDoorCounter += 1
    tick += 1
    usageDeley -= 1

    if fanCounter == len(fanAnimation): fanCounter = 0

    if Counter < 275: Counter += 1
    if 215 > Counter > 200: secondNoiseCounter += 1

    if leftDoorCounter == len(leftDoorCloseAnimation):
        leftDoorCounter = 15-1
    if rightDoorCounter == len(rightDoorCloseAnimation):
        rightDoorCounter = 15-1
    if leftDoorCounter == len(leftDoorOpenAnimation):
        leftDoorCounter = 15-1
    if rightDoorCounter == len(rightDoorOpenAnimation):
        rightDoorCounter = 15-1

# quit
pygame.quit()