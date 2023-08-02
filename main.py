import pygame
import sys
import random

LEFTCLICK = 0
MIDDLECLICK = 1
RIGHTCLICK = 2

class Pixel:
    def __init__(self, index, color):
        self.color = color
        self.i = index

class Area:
    def __init__(self, up, down, func, args, kwargs):
        self.upLeft = up
        self.downRight = down
        self.function = func
        self.args = args
        self.kwargs = kwargs
    
    def __repr__(self):
        return "AREA %s | %s"%(self.upLeft, self.downRight)

class ClickAreas:
    def __init__(self):
        self.areas = [[], [], []]
    
    def addArea(self, click, up, down, func, *args, **kwargs):
        if self.areas[click]!= []:
            for i in range(len(self.areas[click])):
                if self.areas[click][i].upLeft[0] > up[0]:
                    self.areas[click].insert(i, Area(up, down, func, args, kwargs))
                    return
            self.areas[click].append(Area(up, down, func, args, kwargs))
        else:
            self.areas[click].append(Area(up, down, func, args, kwargs))
        
    def clickAction(self, click, x, y):
        for area in self.areas[click]:
            if area.upLeft[0] <= x and area.upLeft[1] <= y and area.downRight[0] >= x and area.downRight[1] >= y:
                print(area)
                area.function(*area.args, **area.kwargs)

def drawRow(screen, x, y, length, pixels, zoomI=None, zoomLocation=None):

    newZoomOffset = 0
    MAXPIXELSIZE = 50
    MINPIXELSIZE = 5
    pixelSize = int(length / len(pixels))


    if pixelSize > MAXPIXELSIZE:
        pixelSize = MAXPIXELSIZE
    if pixelSize < MINPIXELSIZE:
        pixelSize = MINPIXELSIZE

    if zoomI:
        normalZoom = zoomLocation * pixelSize + pixelSize * 0.5

        pixelSize = pixelSize * zoomI

        newZoom = zoomLocation * pixelSize + pixelSize * 0.5
        newZoomOffset = normalZoom - newZoom

    pixelRanges = []
    for i in range(len(pixels)):
        start = int(x + i * pixelSize + newZoomOffset)
        end = int(start + pixelSize)
        if end > x and start < x:
            p = pygame.Rect(x, y, pixelSize, pixelSize)
            pixelRanges.append(list(range(int(start), int(end) + 1)))
            pygame.draw.rect(screen, pygame.Color(pixels[i].color), p)
        elif start > x and end < length + x:
            p = pygame.Rect(start, y, pixelSize, pixelSize)
            pixelRanges.append(list(range(start, end + 1)))
            pygame.draw.rect(screen, pygame.Color(pixels[i].color), p)
        elif start < length + x and end > length + x :
            p = pygame.Rect(start, y, length + x - start, pixelSize)
            pixelRanges.append(list(range(start, end + 1)))
            pygame.draw.rect(screen, pygame.Color(pixels[i].color), p)



if __name__ == "__main__":
    a = ClickAreas()
    a.addArea(LEFTCLICK, (10, 0), (25, 20), print, "test", 1, 2, 3)
    a.addArea(LEFTCLICK, (30, 0), (50, 50), print, "test", 1, 2, 3)
    a.addArea(LEFTCLICK, (25, 0), (30, 50), print, "test", 1, 2, 3)
    a.addArea(LEFTCLICK, (50, 0), (60, 50), print, "test1", 1, 2, 3)
    a.addArea(LEFTCLICK, (40, 0), (45, 50), print, "test", 1, 2, 3)
    a.addArea(MIDDLECLICK, (40, 0), (45, 50), print, "test", 1, 2, 3)
    a.addArea(MIDDLECLICK, (10, 0), (45, 50), print, "test", 1, 2, 3)
    print(a.areas)
    a.clickAction(LEFTCLICK, 50, 40)
    #NUMPIXELS = 121
    #upper_row = [Pixel(i, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))) for i in range(NUMPIXELS)]
    #pygame.init()
    #screen = pygame.display.set_mode((10, 10), pygame.RESIZABLE)
    #screen.fill("#1B1D1E")
    #while True:
    #    screen.fill("#1B1D1E")
    #    x, y = screen.get_size()
    #    for event in pygame.event.get():
    #        if event.type == pygame.QUIT:
    #            pygame.quit()
    #            sys.exit()
    #    a = random.randint(0, 120)
    #    for i in range(100, 500):
    #        drawRow(screen, 20, 0, 700, upper_row, i/100, a)
    #        pygame.display.update()
