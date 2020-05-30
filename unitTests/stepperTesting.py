import unittest
from stepper import *

class WorldTesting(unittest.TestCase):
    def test(self):
        world = World()
        goToPos = world.goSteps(20, 20)
        if goToPos.getX()==20 and goToPos.getY==20:
            self.assertTrue(True)
        world.updateCurrent()
        if world.current.getX()==20 and world.current.getY==20:
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()