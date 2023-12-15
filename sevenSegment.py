import pygame


class sevenSegment:
    segments = [0, 0, 0, 0, 0, 0, 0]

    def __init__(self, inputNum, inputSize, activateColor, deactivateColor, posX, posY, inputScreen):
        self.number = inputNum
        self.activeColor = activateColor
        self.deactiveColor = deactivateColor
        self.sizeFactor = inputSize
        self.posX = posX
        self.posY = posY
        self.screen = inputScreen
        self.calcNum()
        # position is the top left corner of the segment. all positions realtive to that point.

    # calculating for the input num value

    def calcNum(self):
        """
            |---0---|
            5       1
            |---6---|
            4       2
            |---3---|
        """
        # determining which segments to show
        if self.number == 0:
            self.segments = [1, 1, 1, 1, 1, 1, 0]
        elif self.number == 1:
            self.segments = [0, 1, 1, 0, 0, 0, 0]
        elif self.number == 2:
            self.segments = [1, 1, 0, 1, 1, 0, 1]
        elif self.number == 3:
            self.segments = [1, 1, 1, 1, 0, 0, 1]
        elif self.number == 4:
            self.segments = [0, 1, 1, 0, 0, 1, 1]
        elif self.number == 5:
            self.segments = [1, 0, 1, 1, 0, 1, 1]
        elif self.number == 6:
            self.segments = [1, 0, 1, 1, 1, 1, 1]
        elif self.number == 7:
            self.segments = [1, 1, 1, 0, 0, 0, 0]
        elif self.number == 8:
            self.segments = [1, 1, 1, 1, 1, 1, 1]
        elif self.number == 9:
            self.segments = [1, 1, 1, 1, 0, 1, 1]
        else:
            self.segments = [1, 1, 1, 1, 1, 1, 0]

        # drawing the segments
        # top bar
        if self.segments[0] == 1:
            self.drawHorizontalSegment(self.activeColor, self.posX, self.posY)
        # top right
        if self.segments[1] == 1:
            self.drawVerticalSegment(self.activeColor, self.posX + 3.5 * self.sizeFactor + 5, self.posY + 5)
        # bottom right
        if self.segments[2] == 1:
            self.drawVerticalSegment(self.activeColor, self.posX + 3.5 * self.sizeFactor + 5, self.posY + 3.5*self.sizeFactor + 15)
        # bottom bar
        if self.segments[3] == 1:
            self.drawHorizontalSegment(self.activeColor, self.posX, self.posY + 7 * self.sizeFactor + 20)
        # bottom left
        if self.segments[4] == 1:
            self.drawVerticalSegment(self.activeColor,  self.posX - 5, self.posY + 3.5*self.sizeFactor + 15)
        # top left
        if self.segments[5] == 1:
            self.drawVerticalSegment(self.activeColor, self.posX - 5, self.posY + 5)
        # middle bar
        if self.segments[6] == 1:
            self.drawHorizontalSegment(self.activeColor, self.posX, self.posY + 3.5 * self.sizeFactor + 10)

    def drawHorizontalSegment(self, color, inputX, inputY):
        pygame.draw.polygon(self.screen, color, [
            (inputX, inputY),
            #sqrt3 / 2 = 0.866, sqrt2 /2  = 0.707
            (inputX + 0.5 * self.sizeFactor, inputY + self.sizeFactor * 0.5),
            (inputX + 0.5 * self.sizeFactor + 2.5 * self.sizeFactor, inputY + self.sizeFactor * 0.5),
            (inputX + 2 * 0.5 * self.sizeFactor + 2.5 * self.sizeFactor, inputY),
            (inputX + 0.5 * self.sizeFactor + 2.5 * self.sizeFactor, inputY - self.sizeFactor * 0.5),
            (inputX + 0.5 * self.sizeFactor, inputY - self.sizeFactor * 0.5),
            (inputX, inputY)
        ])

    def drawVerticalSegment(self, color, inputX, inputY):
        pygame.draw.polygon(self.screen, color, [
            (inputX, inputY),
            (inputX + self.sizeFactor * 0.5, inputY + 0.5 * self.sizeFactor),
            (inputX + self.sizeFactor * 0.5, inputY + 0.5 * self.sizeFactor + 2.5 * self.sizeFactor),
            (inputX, inputY + 2 * 0.5 * self.sizeFactor + 2.5 * self.sizeFactor),
            (inputX - self.sizeFactor * 0.5, inputY + 0.5 * self.sizeFactor + 2.5 * self.sizeFactor),
            (inputX - self.sizeFactor * 0.5, inputY + 0.5 * self.sizeFactor),
            (inputX, inputY)
        ])
