import sys, pygame, time
from space.planet import Planet
from space.rocket import Rocket

def offset(p, x, y):
    return ((p[0] + x), (p[1] + y))

def processKeydown(key):
    if key == 273: #up arrow
        x = key
    elif key == 274: #down arrow
        x = key
    elif key == 276: #left arrow
        x = key
    elif key == 275: #right arrow
        x = key
    elif key == 112: #p key
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == 114 or event.key == 112: # r key or p key
                        paused = False
                    elif event.key == 113: # q key
                        sys.exit()
    elif key == 113: #q key
        sys.exit()
    elif key == 111: #o key
        r.checkProximity(b)
    else: 
        print(key)


pygame.init()
size = width, height = 1200, 750
center = int(width/2), int(height/2)
speed = [2, 2]
black = 0, 0, 0


screen = pygame.display.set_mode(size)
pygame.display.set_caption('Orbit by Jay Davis')

panel = pygame.Surface((200, height), 0, screen)
panel.fill((100, 100, 100))

b = {
    'sun'    : Planet(screen, (200, 200, 80), center, 10, center),
    'mercury': Planet(screen, (180, 180, 180), offset(center, 72, 0), 2, center),
    'venus'  : Planet(screen, (200, 200, 150), offset(center, 136, 0), 3, center),
    'earth'  : Planet(screen, (80, 80, 200), offset(center, 188, 0), 3, center),
    'mars'   : Planet(screen, (200, 80, 80), offset(center, 284, 0), 2, center),
}

# set orbital radii
b['sun'].setName('Sun').setGravity(274)#1278) 

# -7.9 is accurate for mercury's velocity so it goes around once for every 88 iterations(earth days)
b['mercury'].setOrbitRadius(72).setOrbitPeriod(88).setName('Mercury').setGravity(3.4).setVelocity(-7.9)

# -5.8 is accurate for venus's velocity so it goes around once for every 224 iterations(earth days)
b['venus'].setOrbitRadius(136).setOrbitPeriod(224).setName('Venus').setGravity(8.4).setVelocity(-5.8)

# -4.95 is accurate for earth's velocity so it goes around once for every 365 iterations(days)
b['earth'].setOrbitRadius(188).setOrbitPeriod(365).setName('Earth').setGravity(9.2).setVelocity(-4.95)

# -4.0 is accurate for mars's velocity so it goes around once for every 687 iterations(earth days)
b['mars'].setOrbitRadius(284).setOrbitPeriod(687).setName('Mars').setGravity(3.4).setVelocity(-4.0)

#r = Rocket()
positions = []
i = 0
while 1:
    i += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            processKeydown(event.key)

    screen.fill(black)

    b['sun'].drawPlanet()

    b['mercury'].advancePosition(b['sun']).drawPlanet()
    b['venus'].advancePosition(b['sun']).drawPlanet()
    b['earth'].advancePosition(b['sun']).drawPlanet()
    b['mars'].advancePosition(b['sun']).drawPlanet()

    pygame.display.flip()



# EOF this has been the visible solar system