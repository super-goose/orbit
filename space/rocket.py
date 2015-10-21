import pygame
import math

class Rocket:
    def __init__(self):
        self.velocity = 0
        fuel = 200
        angle = 0
        self.position = (100, 100)

    def launch(self):
        self.velocity = 1
        self.direction = 0

    def advancePosition(self, bodies):
        self.checkProximity()

    def checkProximity(self, bodies):
        for planet in bodies:
            print("{0} from {1}".format(bodies[planet].distanceFrom(self.position), bodies[planet].getName()))


