from work import *


class World(object):
    def __init__(self):
        self.origin = CoordinateSystem()
        self.max = CoordinateSystem()
        self.start = CoordinateSystem()
        self.current = CoordinateSystem()
        self.goToPos = CoordinateSystem()

    def getCurrentX(self):
        return self.current.getY()

    def getCurrentY(self):
        return self.current.getX()

    def getStepsForGivenPosition(self, xCoord, yCoord, ifInSteps=False):
        currentX = self.current.getX()
        currentY = self.current.getY()
        mmToGoX = xCoord - currentX
        mmToGoY = yCoord - currentY
        if ifInSteps==False:
            stepsToGoX=mmToGoX*self.generalConfig['mmToSteps']
            stepsToGoY=mmToGoY*self.generalConfig['mmToSteps']
        else:
            stepsToGoX=mmToGoX
            stepsToGoY=mmToGoY
        return stepsToGoX, stepsToGoY

    def goMM(self, x, y):
        self.goSteps(x * self.generalConfig['mmToSteps'], y * self.generalConfig['mmToSteps'])

    def addStepsToCurrent(self,x,y, ifInSteps=False):
        cX=self.current.getX()
        cY=self.current.getY()
        if ifInSteps==False:
            mmX=x/self.generalConfig['mmToSteps']
            mmY=y/self.generalConfig['mmToSteps']
        else:
            mmX=x
            mmY=y
        return cX+mmX,cY+mmY

    def updateCurrent(self,x,y):
        self.current.setX(x)
        self.current.setY(y)

    def setUpCoordinates(self, config):
        self.config=config
        self.getAllConfigVars(config)
        self.setUpWorlds()

    def getAllConfigVars(self, config):
        self.generalConfig = config['general']


    def setUpWorlds(self):
        self.max.setX(self.generalConfig['lengthX'])
        self.max.setY(self.generalConfig['lengthY'])
        startX=self.generalConfig['startPosX']
        startY=self.generalConfig['startPosY']
        self.origin.setX(startX)
        self.origin.setY(startY)

    def takeRef(self):
        return True

    def getFactor(self):
        return self.generalConfig['mmToSteps']

    def getLengthX(self):
        return self.generalConfig['lengthX']

    def getLengthY(self):
        return self.generalConfig['lengthY']

    def printObjectName(self):
        print(self)