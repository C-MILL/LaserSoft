class CoordinateSystem(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def __eq__(self, other):
        if self.getX() == other.getX() and self.getY() == other.getY():
            return True

    def __ne__(self, other):
        if self.getX() != other.getX() or self.getY() != other.getY():
            return True

    def __add__(self, other):
        self.setX(self.getX()+other.getX())
        self.setY(self.getY()+other.getY())
    
    def __sub__(self, other):
        self.setX(self.getX()-other.getX())
        self.setY(self.getY()-other.getY())
        
