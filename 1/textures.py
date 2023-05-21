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
bonny = pygame.image.load(texturesFolder + 'bonny.png')

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

CamA = pygame.image.load(mapSelectedFolder + 'A.png')
CamD = pygame.image.load(mapSelectedFolder + 'D.png')
CamF = pygame.image.load(mapSelectedFolder + 'F.png')
CamG = pygame.image.load(mapSelectedFolder + 'G.png')
CamH = pygame.image.load(mapSelectedFolder + 'H.png')
CamJ = pygame.image.load(mapSelectedFolder + 'J.png')
CamK = pygame.image.load(mapSelectedFolder + 'K.png')
CamL = pygame.image.load(mapSelectedFolder + 'L.png')
CamO = pygame.image.load(mapSelectedFolder + 'O.png')
CamP = pygame.image.load(mapSelectedFolder + 'P.png')
CamS = pygame.image.load(mapSelectedFolder + 'S.png')
CamOverlay = pygame.image.load(cameraFolder + 'overlay.png')
CamPoint = pygame.image.load(cameraFolder + 'point.png')

diningRoom1 = pygame.image.load(DiningRoomFolder + '1.png')
diningRoom2 = pygame.image.load(DiningRoomFolder + '2.png')
diningRoom3 = pygame.image.load(DiningRoomFolder + '3.png')
diningRoom4 = pygame.image.load(DiningRoomFolder + '4.png')
diningRoom5 = pygame.image.load(DiningRoomFolder + '5.png')
diningRoom6 = pygame.image.load(DiningRoomFolder + '6.png')
diningRoomText = pygame.image.load(DiningRoomFolder + '7.png')

employeesOnly1 = pygame.image.load(EmployeesOnlyFolder + '1.png')
employeesOnly2 = pygame.image.load(EmployeesOnlyFolder + '2.png')
employeesOnly3 = pygame.image.load(EmployeesOnlyFolder + '3.png')
employeesOnly4 = pygame.image.load(EmployeesOnlyFolder + '4.png')
employeesOnly5 = pygame.image.load(EmployeesOnlyFolder + '5.png')
employeesOnlyText = pygame.image.load(EmployeesOnlyFolder + '6.png')

kitchen1 = pygame.image.load(KitchenFolder + '1.png')
kitchenText = pygame.image.load(KitchenFolder + '2.png')

leftCorner1 = pygame.image.load(LeftCornerFolder + '1.png')
leftCorner2 = pygame.image.load(LeftCornerFolder + '2.png')
leftCorner3 = pygame.image.load(LeftCornerFolder + '3.png')
leftCorner4 = pygame.image.load(LeftCornerFolder + '4.png')
leftCorner5 = pygame.image.load(LeftCornerFolder + '5.png')
leftCorner6 = pygame.image.load(LeftCornerFolder + '6.png')
leftCornerText = pygame.image.load(LeftCornerFolder + '7.png')

leftHallwayText = pygame.image.load(LeftHallwayFolder + '4.png')

pirateCove1 = pygame.image.load(PirateCoveFolder + '1.png')
pirateCove2 = pygame.image.load(PirateCoveFolder + '2.png')
pirateCove3 = pygame.image.load(PirateCoveFolder + '3.png')
pirateCove4 = pygame.image.load(PirateCoveFolder + '4.png')
pirateCove5 = pygame.image.load(PirateCoveFolder + '5.png')
pirateCoveText = pygame.image.load(PirateCoveFolder + '6.png')

rightCorner1 = pygame.image.load(RightCornerFolder + '1.png')
rightCorner2 = pygame.image.load(RightCornerFolder + '2.png')
rightCorner3 = pygame.image.load(RightCornerFolder + '3.png')
rightCorner4 = pygame.image.load(RightCornerFolder + '4.png')
rightCorner5 = pygame.image.load(RightCornerFolder + '5.png')
rightCorner6 = pygame.image.load(RightCornerFolder + '6.png')
rightCorner7 = pygame.image.load(RightCornerFolder + '7.png')
rightCorner8 = pygame.image.load(RightCornerFolder + '8.png')
rightCorner9 = pygame.image.load(RightCornerFolder + '9.png')
rightCornerText = pygame.image.load(RightCornerFolder + '10.png')

rightHallway1 = pygame.image.load(RightHallwayFolder + '1.png')
rightHallway2 = pygame.image.load(RightHallwayFolder + '2.png')
rightHallway3 = pygame.image.load(RightHallwayFolder + '3.png')
rightHallway4 = pygame.image.load(RightHallwayFolder + '4.png')
rightHallway5 = pygame.image.load(RightHallwayFolder + '5.png')
rightHallway6 = pygame.image.load(RightHallwayFolder + '6.png')
rightHallwayText = pygame.image.load(RightHallwayFolder + '7.png')

stage1 = pygame.image.load(StageFolder + '1.png')
stage2 = pygame.image.load(StageFolder + '2.png')
stage3 = pygame.image.load(StageFolder + '3.png')
stage4 = pygame.image.load(StageFolder + '4.png')
stage5 = pygame.image.load(StageFolder + '5.png')
stage6 = pygame.image.load(StageFolder + '6.png')
stage7 = pygame.image.load(StageFolder + '7.png')
stageText = pygame.image.load(StageFolder + '8.png')

toilets1 = pygame.image.load(ToiletsFolder + '1.png')
toilets2 = pygame.image.load(ToiletsFolder + '2.png')
toilets3 = pygame.image.load(ToiletsFolder + '3.png')
toilets4 = pygame.image.load(ToiletsFolder + '4.png')
toiletsText = pygame.image.load(ToiletsFolder + '5.png')

utilityCloset1 = pygame.image.load(UtilityClosetFolder + '1.png')
utilityCloset2 = pygame.image.load(UtilityClosetFolder + '2.png')
utilityClosetText = pygame.image.load(UtilityClosetFolder + '3.png')