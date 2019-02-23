import pygame, sys

pygame.init()



red = (255, 0, 0)
blue = (0, 255, 0)
green = (0, 0, 255)

pygame.display.set_caption('Team Managment')

clock = pygame.time.Clock()

pygame.font.init()
myfont = pygame.font.SysFont('Arial', 10)

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
    def __init__(self, tribe, currentMeasure, teamX, teamY, teamGap, anchor, width, height, criticalValue):
        self.tribe = tribe
        self.currentMeasure = currentMeasure
        self.teamGap = teamGap
        self.teamX = teamX
        self.teamY = teamY
        self.anchor = anchor
        self.width = width
        self.height = height
        self.criticalValue = criticalValue

    def changeMeasure(self, measure):
        self.currentMeasure = measure
        print(self.currentMeasure)

    def changeCritValue(self, critValue):
        self.criticalValue = critValue


    def draw(self, win):
        count = 0
        currentMeasurement = myfont.render(self.currentMeasure, False, (255, 255, 255))
        win.blit(currentMeasurement, (130, 5))
        for team in self.tribe.getTeams():
            pygame.draw.rect(win, team.colour, (self.teamX, (self.teamY + (40*count) + (self.teamGap*count)), team.getMeasure(self.currentMeasure), 40))
            count += 1
        critValue = self.criticalValue
        x = critValue.getX
        pygame.draw.rect(win, red, (self.criticalValue.x, 20, 1, 390))
            
class criticalValue(object):
    def __init__(self, x):
        self.x = x

    def changeValue(self, newX):
        self.x = newX

    def getX(self):
        return self.x


m1 = measure('Release Rate', 80)
m2 = measure('Operational Incidents', 50)
m3 = measure('Release Rate', 190)
m4 = measure('Operational Incidents', 120)
c1 = criticalValue(150)
c2 = criticalValue(40)
teamOne = team((165,207,255), [m1,m2])
teamTwo = team(blue,[m3,m4])
teamThree = team(green,[m3,m2])
teamFour = team((171,0,255),[m1,m4])
teamFive = team((255,255,0),[m1,m2])
teamSix = team((255,162,0),[m3,m4])
teamSeven = team((255,0,255),[m3,m2])
teamEight = team((0,255,235),[m1,m4])
tribeOne = tribe([teamOne,teamTwo,teamThree,teamFour,teamFive,teamSix,teamSeven,teamEight])
viewOne = itemsScoresView(tribeOne, 'Operational Incidents', 10, 20, 10, (0,0), 368, 448, c2)
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
        viewOne.changeMeasure('Operational Incidents')
        viewOne.changeCritValue(c2)
    if keys[pygame.K_DOWN]:
        viewOne.changeMeasure('Release Rate')
        viewOne.changeCritValue(c1)

    win.fill((0,0,0))
    viewOne.draw(win)
    pygame.display.update()
    
pygame.quit()
