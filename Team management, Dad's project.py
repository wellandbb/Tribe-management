import pygame, sys

pygame.init()



red = (255, 0, 0)
blue = (0, 255, 0)
green = (0, 0, 255)

pygame.display.set_caption('Team Managment')

clock = pygame.time.Clock()

class team(object):
    def __init__(self, colour, measures):
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


class itemsScoresView(object):
    def __init__(self, tribe, currentMeasure, size, teamX, teamY, teamGap):
        self.tribe = tribe
        self.currentMeasure = currentMeasure
        self.size = size
        self.teamGap = teamGap
        self.teamX = teamX
        self.teamY = teamY

    def changeMeasure(self, measure):
        self.currentMeasure = measure
        print(self.currentMeasure)


    def draw(self, win):
        count = 0
        for team in self.tribe.getTeams():
            pygame.draw.rect(win, team.colour, (self.teamX, (self.teamY + (40*count) + (self.teamGap*count)), team.getMeasure(self.currentMeasure), 40))
            count += 1

    def getSize(self):
        return self.size
            
    




m1 = measure('releaseRate', 80)
m2 = measure('operationalIncidents', 50)
m3 = measure('releaseRate', 190)
m4 = measure('operationalIncidents', 120)
teamOne = team(red, [m1,m2])
teamTwo = team(blue,[m3,m4])
teamThree = team(green,[m3,m2])
teamFour = team((171,0,255),[m1,m4])
teamFive = team((255,255,0),[m1,m2])
teamSix = team((255,162,0),[m3,m4])
teamSeven = team((255,0,255),[m3,m2])
teamEight = team((0,255,235),[m1,m4])
tribeOne = tribe([teamOne,teamTwo,teamThree,teamFour,teamFive,teamSix,teamSeven,teamEight])
viewOne = itemsScoresView(tribeOne, 'operationalIncidents', (368,448), 10, 20, 10)
screen = (368,448) 
win = pygame.display.set_mode(screen)
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
