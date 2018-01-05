# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.

# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "The Night Scene"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
BROWN = (107, 69, 9)
YELLOW = (255, 208, 0)
GREY = (181, 170, 157)
LIGHTGREEN = (142, 222, 39)
DARKGREEN = (93, 120, 1)

def make_stars():
    for s in stars:
        pygame.draw.ellipse(screen, WHITE, s)
stars = []
for i in range(200):
    x = random.randrange(0, 800)
    y = random.randrange(0, 400)
    r = random.randrange(1, 5)
    stars.append([x, y, r, r])

def sky():
    screen.fill(BLACK)

def moon(a, b):
    pygame.draw.ellipse(screen, WHITE, [a, b, 100, 100])

def grass():
    pygame.draw.rect(screen, LIGHTGREEN, [0, 400, 800, 200])

def fence():
    y = 380
    for x in range(5, 800, 30):
        post = ([x+5, y], [x+10, y+5], [x+10, y+40], [x, y+40], [x, y+5])
        pygame.draw.polygon(screen, WHITE, post)

    pygame.draw.rect(screen, WHITE, [0, y+10, 800, 5])
    pygame.draw.rect(screen, WHITE, [0, y+30, 800, 5])

def house():
    pygame.draw.rect(screen, RED, [340, 265, 160, 140])
    pygame.draw.polygon(screen, BROWN, [[420, 185], [330,265], [510, 265]])
    pygame.draw.rect(screen, BLUE, [360, 305, 40, 40])
    pygame.draw.rect(screen, BROWN, [420, 325, 40, 80])

def trees(w, x, y, z):
    pygame.draw.rect(screen, BROWN, [w, x, 40, 160])
    pygame.draw.ellipse(screen, DARKGREEN, [y, z, 120, 140])

def cloud(x, y):
    pygame.draw.ellipse(screen, GREY, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GREY, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, GREY, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, GREY, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, GREY, [x + 20, y + 20, 60, 40])

def snowman(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y, 20, 20])
    pygame.draw.ellipse(screen, WHITE, [x - 5, y + 15, 30, 30])
    pygame.draw.ellipse(screen, WHITE, [x - 10, y + 30, 40, 40])
    
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Drawing code
    '''sky'''
    sky()
    ''' stars '''
    make_stars()
        
    ''' moon '''
    moon(660, 20)

    ''' clouds '''
    cloud(200,100)
    cloud(400, 50)
    cloud(50, 25)
    cloud(710, 80)
    
    ''' grass '''
    grass()

    '''house'''
    house()
    
    ''' fence '''
    fence()

    '''trees'''
    trees(50, 300, 10, 200)

    ''' snowmen '''
    snowman(700, 500)

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
