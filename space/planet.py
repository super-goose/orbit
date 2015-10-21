import pygame
import math

class Planet:
    def __init__(self, surface, color, position, radius, center):
        self.radius = radius
        self.surface = surface
        self.color = color
        self.setPosition(position)
        self.center = center
        self.setOrbitOffset(0)
        self.setOrbitPeriod(1)
        self.setOrbitRadius(0)
        self.year = 0
        self.mass = 0
        self.velocity = 0
        self.angle = 0
        self.name = ''

    def drawPlanet(self):
        x = int(self.position[0])
        y = int(self.position[1])
        pygame.draw.circle(self.surface, self.color, (x, y), self.radius)

    def getRadius(self): return self.radius       

    def setPosition(self, newPos):
        self.position = newPos
        return self

    def getPosition(self): return self.position        

    def setVelocity(self, vel):
        self.velocity = vel
        return self

    def getVelocity(self): return self.velocity        

    def setAngle(self, angle):
        self.angle = angle
        return self

    def getAngle(self): return self.angle        

    def setName(self, name):
        self.name = name
        return self

    def getName(self): return self.name

    def setGravity(self, gravity):
        self.gravity = gravity
        return self

    def getGravity(self): return self.gravity

    def setOrbitRadius(self, radius):
        self.orbitRadius = radius
        return self

    def getOrbitRadius(self): return self.orbitRadius

    def setOrbitOffset(self, offset):
        self.orbitOffset = offset
        return self

    def getOrbitOffset(self): return self.orbitOffset

    def setOrbitPeriod(self, period):
        self.orbitPeriod = period
        return self

    def getOrbitPeriod(self): return self.orbitPeriod

    def advancePosition(self, sun):
        x, y = self.position

        # get new point with no gravity
        v = self.velocity
        angle = self.angle
        vx = v * math.sin(angle)
        vy = v * math.cos(angle)

        # get the pull fromt he sun
        gravitaionalConstant = 14 # this is the number that made it work well
                                  # i don't know why this number and not another
        sunX, sunY = sun.getPosition()
        sunX -= x
        sunY -= y
        d = math.sqrt(sunX**2 + sunY**2)
        g = sun.getGravity() * gravitaionalConstant / (d ** 2)

        ax = (g * sunX) / d
        ay = (g * sunY) / d

        # add these vectors together
        dx = vx + ax
        dy = vy + ay
        newV = math.sqrt(dx**2 + dy**2)

        # using law of cosines to get the angle
        # by getting the cosine first, then using arccos to find the angle
        ac = (g**2 - v**2 - newV**2)/(-2 * v * newV)
        A = math.acos(ac)

        #update attributes
        self.angle += A
        self.velocity = newV

        x += newV * math.sin(self.angle)
        y += newV * math.cos(self.angle)
        self.setPosition((x, y))

        return self

    def distanceFrom(self, pos):
        x1 = self.position[0]
        y1 = self.position[1]
        x2 = pos[0]
        y2 = pos[1]

        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


# EOF for planets