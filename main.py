from random import random
import pygame
from sevenSegment import sevenSegment
from target import target


# declaring globals
startGreen, stopBlue, backgroundColor = '#73f598', '#73b0f5', '#445552'
startText = "Start Timer"
startRectColor = startGreen

# target creation method
def createTarget(targets, targetRadius):
    # getting x and y values
    targetX = random() * (1920 - 150) + (75 + targetRadius)
    targetY = random() * (1080 - 100 - 150) + (150 + targetRadius)
    # create target and add to the array
    # list of target objects

    targets.append(target(targetX, targetY, targetRadius, '#f7d9d7', '#eb4034'))


class main:
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()
    running = True
    targets = []

    # 0 is false 1 true
    # initial target loading
    targetRadius = 40
    i = 0
    while i < 10:
        createTarget(targets, targetRadius)
        i += 1

    # drawing
    timeLength = 5
    timeBeforeReset = timeLength * 60  # 60 is fps
    font = pygame.font.SysFont('Helvetica', 48)
    pushedStart, targetCount, highScore = 0, 0, 0


    # stop Timer
    def stopTimer():
        global startRectColor
        startRectColor = '#73f598'
        global startText
        startText = "Start Timer"

    def startTimer():
        print("inside start")
        global startRectColor
        global startText
        startRectColor = '#73b0f5'
        startText = "Stop Timer"

    while running:
        screen.fill(backgroundColor)

        # start timer
        startRect = pygame.Rect(screen.get_width() - 300, 50, 200, 50)
        pygame.draw.rect(screen, startRectColor, startRect, 0, 15)

        # timer
        if pushedStart:
            timeBeforeReset -= 1
            # timer finished
            if timeBeforeReset == 0:
                timeBeforeReset = timeLength * 60  # 60 fps
                highScore = targetCount
                targetCount = 0
                pushedStart = 0
                stopTimer()


        # display highscore
        sevenSegment(highScore, 6, '#FFFFFF', (screen.get_width() / 2 + 100), 50, screen)

        # display timer
        displayTimer = float(timeBeforeReset / 60)
        timerSurface = font.render(str("%.1f" % displayTimer), True, (0, 0, 0))
        screen.blit(timerSurface, (screen.get_width() / 2, 50))

        # drawing all targets
        for target in targets:
            pygame.draw.circle(screen, target.targetColor, (target.centerX, target.centerY), target.radius)
            pygame.draw.circle(screen, target.secondColor, (target.centerX, target.centerY), target.radius * 0.8)
            pygame.draw.circle(screen, target.targetColor, (target.centerX, target.centerY), target.radius * 0.6)
            pygame.draw.circle(screen, target.secondColor, (target.centerX, target.centerY), target.radius * 0.4)

        # checking for click on the start/stop button and on each target
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                # start and stop timer, change color to indicate
                if ((startRect.x < mouseX < startRect.x + startRect.w) and
                        (startRect.y < mouseY < startRect.y + startRect.h)):
                    print("inside the button")
                    if pushedStart == 0:
                        pushedStart = 1
                        print("calling start")
                        startTimer()
                    else:
                        pushedStart = 0
                        print("calling stop")
                        stopTimer()

                # change target color on click
                for targetToCheck in targets:
                    if ((targetToCheck.centerX - mouseX) ** 2 + (
                            targetToCheck.centerY - mouseY) ** 2) < targetToCheck.radius ** 2 and pushedStart:
                        createTarget(targets, targetRadius)

                        # removing hit target
                        targets.remove(targetToCheck)

                        # increment highscore
                        targetCount += 1
                        break

        # print the start / stop text
        startSurface = font.render(startText, True, (0, 0, 0))
        screen.blit(startSurface, (screen.get_width() - 300, 48))

        # Score counter
        sevenSegment(targetCount, 10, '#FFFFFF', 150, 50, screen)
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
