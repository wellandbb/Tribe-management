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
    def __init__(self, y, x, colour, measures):
        self.y = y
        self.x = x
        self.colour = colour
        self.measures = measures

    def getMeasure(self, selectedMeasure):
        for measure in self.measures:
            if measure.getName() == selectedMeasure:
                return measure.getValue()
                

class measure(object):
    def __init__(self, name, value):
        self.value = value
        self.name = name

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

class tribe(object):
    def __init__(self, teams):
        self.teams = teams


    def getTeams(self):
        return self.teams


class tribeMeasureView(object):
    def __init__(self, tribe, currentMeasure):
        self.tribe = tribe
        self.currentMeasure = currentMeasure

    def changeMeasure(self, measure):
        self.currentMeasure = measure
        print(self.currentMeasure)


    def draw(self, win):
        for team in self.tribe.getTeams():
            pygame.draw.rect(win, team.colour, (team.x, team.y, team.getMeasure(self.currentMeasure), 40))
            
    




m1 = measure('releaseRate', 80)
m2 = measure('operationalIncidents', 50)
m3 = measure('releaseRate', 190)
m4 = measure('operationalIncidents', 120)
teamOne = team( 30, 10, red, [m1,m2])
teamTwo = team(80, 10, blue,[m3,m4])
teamThree = team(130, 10, green,[m3,m2])
teamFour = team(180, 10, red,[m1,m4])
teamFive = team(230, 10, blue,[m1,m2])
teamSix = team(280, 10, green,[m3,m4])
teamSeven = team(330, 10, red,[m3,m2])
teamEight = team(380, 10, blue,[m1,m4])
tribeOne = tribe([teamOne,teamTwo,teamThree,teamFour,teamFive,teamSix,teamSeven,teamEight])
viewOne = tribeMeasureView(tribeOne, 'operationalIncidents')
#mainloop
run = True
while run:

    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        viewOne.changeMeasure('operationalIncidents')
    if keys[pygame.K_DOWN]:
        viewOne.changeMeasure('releaseRate')

    win.fill((0,0,0))
    viewOne.draw(win)
    pygame.display.update()
    
pygame.quit()
