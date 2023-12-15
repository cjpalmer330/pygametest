import os
import pygame
from sevenSegment import sevenSegment
import math

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
targets = []


# 0 is false 1 true

class target:
    def __init__(self, inputX, inputY, inputRadius, inputColor):
        self.centerY = inputY
        self.radius = inputRadius
        self.centerX = inputX
        self.targetColor = inputColor
        self.hit = 0


targetIsHit = []
i = 0
while i < 18:
    targetIsHit.append(0)
    i += 1

# creating the targets
targetX, targetY, targetRadius = 100, 100, 40
i = 0
while i < targetIsHit.__len__():
    # getting x and y values
    if (i % 9) != 0:
        targetX += 120
    else:
        targetX = 100
        targetY += 120

    # create target and add to the array
    tempTarget = target(targetX, targetY, targetRadius, (100, 80, 80))
    targets.append(tempTarget)
    i += 1

# drawing
timeBeforeReset = 5 * 60  # 60 is fps
font = pygame.font.SysFont('Helvetica', 48)
pushedStart, targetCount = 0, 0
startGreen = '#73f598'
startText = "Start Timer"
startRectColor = startGreen

# game run
while running:
    screen.fill('#d394f7')

    # start timer
    startRect = pygame.Rect(screen.get_width() - 300, 50, 200, 50)
    pygame.draw.rect(screen, startRectColor, startRect, 0 , 15)

    # timer
    if pushedStart:
        timeBeforeReset -= 1
        if timeBeforeReset == 0:
            for target in targets:
                target.targetColor = (100, 80, 80)
            timeBeforeReset = 5 * 60
            targetCount = 0

    # display tenths of a second
    displayTimer = float(timeBeforeReset / 60)
    timerSurface = font.render(str("%.1f" % displayTimer), True, (0, 0, 0))
    screen.blit(timerSurface, (screen.get_width() / 2, 50))

    # drawing targets
    for target in targets:
        pygame.draw.circle(screen, target.targetColor, (target.centerX, target.centerY), target.radius)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            # start and stop timer, change color to indicate
            if ((startRect.x < mouseX < startRect.x + startRect.w) and
                    (startRect.y < mouseY < startRect.y + startRect.h)):
                print("inside the button")
                if startRectColor == startGreen:
                    startRectColor = '#73b0f5'
                    startText = "Stop Timer"
                    pushedStart = 1
                else:
                    startRectColor = startGreen
                    startText = "Start Timer"
                    pushedStart = 0

            print(mouseX, mouseY, startRect.x, startRect.w, startRect.y, startRect.h, running)
            # change target color on click
            for target in targets:
                if ((target.centerX - mouseX) ** 2 + (target.centerY - mouseY) ** 2) < target.radius ** 2:
                    if(target.hit == 1): break
                    target.hit = 1
                    target.targetColor = '#5c0323'
                    targetCount += 1
                    break

    # on click we check if the position is within one of the target
    # if we are within the target set that target to 1 == hit, and change color
    # print the start / stop text
    startSurface = font.render(startText, True, (0, 0, 0))
    screen.blit(startSurface, (screen.get_width() - 300, 48))

    # testing segment
    testingSegment = sevenSegment(targetCount, 10, '#FFFFFF', '#333333', 150, 50, screen)
    # testingSegment.drawHorizontalSegment('#FFFFFF', 150, 150)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
