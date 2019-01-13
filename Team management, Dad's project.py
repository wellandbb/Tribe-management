import pygame, sys

pygame.init()

size = (368,448)
win = pygame.display.set_mode((size))

red = (255, 0, 0)
blue = (0, 255, 0)
green = (0, 0, 255)

pygame.display.set_caption('Team Managment')

clock = pygame.time.Clock()

class team(object):
    def __init__(self, points, y, x, colour, measures):
        self.points = points
        self.y = y
        self.x = x
        self.colour = colour
        self.measures = measures
        
    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.points, 40))

    def getMeasure(self, measure):
        for items in self.measures:
            if items.getName == measure:
                print(items.getValue)
                

class measure(object):
    def __init__(self, name, value):
        self.value = value
        self.name = name

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

class tribe(object):
    def __init__(self, teams, currentMeasure):
        self.teams = teams
        self.currentMeasure = currentMeasure

    def changeMeasure(self, measure):
        self.currentMeasure = measure

    def showMeasure(self):
        for items in self.teams:
            items.getMeasure(self.currentMeasure)
        
        

#mainloop
run = True

m1 = measure('releaseRate', 3)
m2 = measure('operationalIncidents', 1)
teamOne = team(20, 30, 10, red, [m1,m2])
tribeOne = tribe([teamOne], 'releaseRate')
#teamTwo = team(20, 80, 10, blue)
#teamThree = team(20, 130, 10, green)
#teamFour = team(20, 180, 10, red)
#teamFive = team(20, 230, 10, blue)
#teamSix = team(20, 280, 10, green)
#teamSeven = team(20, 330, 10, red)
#teamEight = team(20, 380, 10, blue)
while run:

    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        tribeOne.showMeasure()



    teamOne.draw(win)
    #teamTwo.draw(win)
    #teamThree.draw(win)
    #teamFour.draw(win)
    #teamFive.draw(win)
    #teamSix.draw(win)
    #teamSeven.draw(win)
    #teamEight.draw(win)


    
    pygame.display.update()
    
pygame.quit()
