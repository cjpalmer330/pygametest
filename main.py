import os
import pygame
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
pushedStart = 0
while running:
    screen.fill('#d394f7')
    # timer
    if pushedStart:
        timeBeforeReset -= 1
        if timeBeforeReset == 0:
            for target in targets:
                target.targetColor = (100, 80, 80)
            timeBeforeReset = 5 * 60

    #display tenths of a second
    displayTimer = float(timeBeforeReset / 60)
    text_surface = font.render(str("%.1f" % displayTimer), False, (0, 0, 0))
    screen.blit(text_surface, (screen.get_width()/2, 50))

    #drawing targets
    for target in targets:
        pygame.draw.circle(screen, target.targetColor, (target.centerX, target.centerY), target.radius)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # on click we check if the position is within one of the target
    # if we are within the target set that target to 1 == hit, and change color
    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        for target in targets:
            if ((target.centerX - mouseX) ** 2 + (target.centerY - mouseY) ** 2) < target.radius ** 2:
                target.hit = 1
                target.targetColor = '#5c0323'
                break

    # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
