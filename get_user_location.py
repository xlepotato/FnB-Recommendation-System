import pygame
import database
from math import sqrt

## define event handler for mouse click.
## this event handler will be fired (activated) when user clicks a mouse button anywhere in the display window
def MouseClick():
    finish = False
    while finish == False:
        ## pygame.event.get() retrieves all events made by user
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                finish = True
                pygame.display.quit()

    return (mouseX, mouseY)

def calc_distance(x2,y2):
    ## getting distance based on the point indicated in the map
    for i in range(0,5):
        x1 = database.canteensNTU.list[i].coordinates[0]
        y1 = database.canteensNTU.list[i].coordinates[1]
        distance = sqrt(((x2-x1)**2) + ((y2-y1)**2))
        print(round(distance,0))

def get_user_location():
    ## make necessary initializations for Width, Height
    W = 640
    H = 480
    font = pygame.font.SysFont("monospace", 20)
    text1 = font.render("NTU map", True, (0, 0, 0))

    # initialize display window, call it screen
    screen = pygame.display.set_mode((W, H))

    # read image file and rescale it to the window size
    screenIm = pygame.image.load("img/NTU_campus.png")
    screenIm = pygame.transform.scale(screenIm, (W, H))

    # add the image over the screen object
    screen.blit(screenIm, (0, 0))

    # add the text over the screen object
    screen.blit(text1, (200, 300))

    # will update the contents of the entire display window
    pygame.display.flip()

    # get outputs of Mouseclick event handler
    buttonX, buttonY = MouseClick()
    print("Your current coordinates is:",(buttonX, buttonY))
    calc_distance(buttonX,buttonY)

# pygame.init()
# get_user_location()

