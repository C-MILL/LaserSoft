import time
from pathlib import Path

from PyQt5.QtCore import QThread, pyqtSignal
import matplotlib

from work.Cal import cal
from work.StepperDriver import stepper

matplotlib.use('Agg')
import matplotlib.pyplot as plt



class Work(QThread):
    updatePage = pyqtSignal()

    def __init__(self):
        QThread.__init__(self)
        self.daemon = True


    def startOperation(self):
        self.start()

    def run(self):
        if self.inSteps==True:
            cal(self, self.world, self.config, False)
        self.coordToDraw = {'x': [], 'y': []}
        self.stepperDict={'x':[],'y':[],'laser':[],'speed':[]}
        xList = self.coordDict['x']
        yList = self.coordDict['y']
        laserList = self.coordDict['laser']
        lines = 0
        drawnLines=0
        dictC = {}
        self.percentStep = 0
        self.percentStepOfDrawing =0
        for element in range(len(xList)):
            x = xList[element]
            y = yList[element]
            laser = laserList[element]
            x, y = self.world.getStepsForGivenPosition(x, y,self.inSteps)
            currentXY={'x':x,'y':y}
            if x == 0 or y == 0:
                stepAfter = 0
                if x == 0:
                    bigger = 'y'
                    smaller = 'x'
                else:
                    bigger = 'x'
                    smaller = 'y'
            elif abs(x) > abs(y):
                smaller = 'y'
                bigger = 'x'
                stepAfter = y / x
            elif abs(x) == abs(y):
                smaller = 'x'
                bigger = 'y'
                stepAfter = y / x
            else:
                smaller = 'x'
                bigger = 'y'
                stepAfter = x / y


            biggerNr=currentXY[bigger]
            for i in currentXY:
                if currentXY[i] > 0:
                    currentXY[i] = 1
                elif currentXY[i] == 0:
                    currentXY[i] = 0
                else:
                    currentXY[i]= -1

            for mm in range(int(abs(biggerNr))):
                before = round((mm) * stepAfter)
                if before != round((mm + currentXY[smaller]) * stepAfter):
                    dictC[smaller] = currentXY[smaller]
                else:
                    dictC[smaller] = 0
                dictC[bigger] = currentXY[bigger]

                #if not at the beginning and laser before and now is the same
                if mm!=0 and self.stepperDict['laser'][element-1]==self.stepperDict['laser'][element]:
                    #if step can be added to step before
                    if self.stepperDict['x'][element-1]==1 and dictC['y']==1 and self.stepperDict['y'][element-1]==0 and self.stepperDict['x'][element]!=1:
                        self.stepperDict['y'][element-1]=dictC['y']
                    elif self.stepperDict['y'][element-1]==1 and dictC['x']==1 and self.stepperDict['x'][element-1]==0 and self.stepperDict['y'][element]!=1:
                        self.stepperDict['x'][element - 1] = dictC['x']

                    #if laser before and now is not the same step can not be added
                    else:
                        self.stepperDict['x'].append(dictC['x'])
                        self.stepperDict['y'].append(dictC['y'])
                        if laser == True:
                            self.stepperDict['laser'].append(True)
                            self.stepperDict['speed'].append(self.workingSpeed)
                        else:
                            self.stepperDict['laser'].append(False)
                            self.stepperDict['speed'].append(self.movingSpeed)
                else:
                    self.stepperDict['x'].append(dictC['x'])
                    self.stepperDict['y'].append(dictC['y'])
                    if laser == True:
                        self.stepperDict['laser'].append(True)
                        self.stepperDict['speed'].append(self.workingSpeed)
                    else:
                        self.stepperDict['laser'].append(False)
                        self.stepperDict['speed'].append(self.movingSpeed)

                x, y = self.world.addStepsToCurrent(dictC['x'], dictC['y'],self.inSteps)
                if laser == True:
                    if self.inSteps==False:
                        if ('x' + str(lines)) not in self.coordToDraw:
                            self.coordToDraw['x' + str(lines)] = [self.world.getCurrentY()]
                            self.coordToDraw['y' + str(lines)] = [self.world.getCurrentX()]
                        self.coordToDraw['x' + str(lines)].append(round(x))
                        self.coordToDraw['y' + str(lines)].append(round(y))
                    else:
                        if ('x' + str(lines)) not in self.coordToDraw:
                            self.coordToDraw['x' + str(lines)] = [self.world.getCurrentY()/self.mmToSteps]
                            self.coordToDraw['y' + str(lines)] = [self.world.getCurrentX()/self.mmToSteps]
                        self.coordToDraw['x' + str(lines)].append(round(x/self.mmToSteps))
                        self.coordToDraw['y' + str(lines)].append(round(y/self.mmToSteps))
                self.world.updateCurrent(x, y)

            if laser == True:
                lines += 1




        for element in range(len(self.stepperDict['speed'])):
            self.percent = 100 * ((element + 1) / len(self.stepperDict['speed']))
            if self.percent >= self.percentStep:
                if self.percent>=self.percentStepOfDrawing:
                    self.draw(round(((len(self.coordToDraw)/2)/100)*self.percent), drawnLines)
                    drawnLines = round(((len(self.coordToDraw)/2)/100)*self.percent)
                    if self.inSteps==False:
                        self.percentStepOfDrawing+=100
                    else:
                        self.percentStepOfDrawing += 5
                if self.inSteps==False:
                    self.percentStep += 100
                else:
                    self.percentStep +=5
                self.updatePage.emit()

            if self.stepperDict['laser'][element]==True:
                self.laser.turnOnLaser(self.laserPower)
                stepper([self.stepperDict['x'][element], self.stepperDict['y'][element]], self.stepperDict['speed'][element],self.firingDiameter)
                self.laser.turnOffLaser()
            else:
                stepper([self.stepperDict['x'][element], self.stepperDict['y'][element]], self.stepperDict['speed'][element], self.firingDiameter)
            if self.stop==True:
                break
        if self.inSteps==True:
            cal(self, self.world, self.config, False)


    def getPercent(self):
        return self.percent



    def draw(self, lines,drawnLines):
        for line in range(lines-drawnLines):
            try:
                x = self.coordToDraw['x' + str(line+drawnLines)]
                y = self.coordToDraw['y' + str(line+drawnLines)]
                plt.plot(x, y, linestyle='-', color='black', linewidth=0.8)
            except:
                pass

        figure = plt.gcf()
        if not plt.gca().yaxis_inverted():
            plt.gca().invert_yaxis()

        figure.set_size_inches(7.5, 5)
        plt.plot(self.config['general']['lengthX'], self.config['general']['lengthY'], color='black')
        plt.plot(-self.config['general']['startPosX'], -self.config['general']['startPosY'], color='black')
        plt.savefig(str(Path(__file__).parents[1]) + "/images/plot.jpg", background='#36393b', dpi=100)

    def setUp(self, laser, laserPower, workingSpeed, coordDict, config, world,mmToSteps,movingSpeed,inSteps, firingDiameter):
        self.inSteps=inSteps
        self.mmToSteps=mmToSteps
        self.laser = laser
        self.laserPower = laserPower
        self.workingSpeed = workingSpeed
        self.coordDict = coordDict
        self.config = config
        self.world = world
        self.movingSpeed=movingSpeed
        self.firingDiameter=firingDiameter


    def setStop(self,state):
        self.stop=state