import pygame


class sevenSegment:
    segments = [0, 0, 0, 0, 0, 0, 0]

    def __init__(self, inputNum, inputSize, activateColor, posX, posY, inputScreen):
        self.number = str(inputNum)
        self.activeColor = activateColor
        self.sizeFactor = inputSize
        self.posX = posX
        self.posY = posY
        self.screen = inputScreen
        # call the draw function for each digit in the number
        numDigits = len(self.number)
        while numDigits > 0:
            numDigits -= 1
            self.calcNum(int(self.number[numDigits]), numDigits)
        # position is the top left corner of the segment. all positions realtive to that point.

    # calculating for the input num value

    def calcNum(self, num, digitNum):
        digitSpace = self.sizeFactor * digitNum * 7
        barFactor = 3.5 * self.sizeFactor
        gapSize = self.sizeFactor / 2
        """
            |---0---|
            5       1
            |---6---|
            4       2
            |---3---|
        """
        # determining which segments to show
        if num == 0:
            self.segments = [1, 1, 1, 1, 1, 1, 0]
        elif num == 1:
            self.segments = [0, 1, 1, 0, 0, 0, 0]
        elif num == 2:
            self.segments = [1, 1, 0, 1, 1, 0, 1]
        elif num == 3:
            self.segments = [1, 1, 1, 1, 0, 0, 1]
        elif num == 4:
            self.segments = [0, 1, 1, 0, 0, 1, 1]
        elif num == 5:
            self.segments = [1, 0, 1, 1, 0, 1, 1]
        elif num == 6:
            self.segments = [1, 0, 1, 1, 1, 1, 1]
        elif num == 7:
            self.segments = [1, 1, 1, 0, 0, 0, 0]
        elif num == 8:
            self.segments = [1, 1, 1, 1, 1, 1, 1]
        elif num == 9:
            self.segments = [1, 1, 1, 1, 0, 1, 1]
        else:
            self.segments = [1, 1, 1, 1, 1, 1, 0]

        # drawing the segments
        # top bar
        if self.segments[0] == 1:
            self.drawHorizontalSegment(self.activeColor, self.posX + digitSpace, self.posY)
        # top right
        if self.segments[1] == 1:
            self.drawVerticalSegment(self.activeColor, self.posX + barFactor + gapSize + digitSpace, self.posY + gapSize)
        # bottom right
        if self.segments[2] == 1:
            self.drawVerticalSegment(self.activeColor, self.posX + barFactor + gapSize + digitSpace,
                                     self.posY + barFactor + 3 * gapSize)
        # bottom bar
        if self.segments[3] == 1:
            self.drawHorizontalSegment(self.activeColor, self.posX + digitSpace, self.posY + 2 * barFactor + 4 * gapSize)
        # bottom left
        if self.segments[4] == 1:
            self.drawVerticalSegment(self.activeColor, self.posX - gapSize + digitSpace, self.posY + barFactor + 3 * gapSize)
        # top left
        if self.segments[5] == 1:
            self.drawVerticalSegment(self.activeColor, self.posX - gapSize + digitSpace, self.posY + gapSize)
        # middle bar
        if self.segments[6] == 1:
            self.drawHorizontalSegment(self.activeColor, self.posX + digitSpace, self.posY + barFactor + 2 * gapSize)

    def drawHorizontalSegment(self, color, inputX, inputY):
        pygame.draw.polygon(self.screen, color, [
            (inputX, inputY),
            # sqrt3 / 2 = 0.866, sqrt2 /2  = 0.707
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
