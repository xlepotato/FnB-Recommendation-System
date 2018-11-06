import pygame
import database
from math import sqrt


# define event handler for mouse click.
# this event handler will be fired (activated) when user clicks a mouse button anywhere in the display window
def MouseClick():
    finish = False
    while finish == False:
        # pygame.event.get() retrieves all events made by user
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                finish = True
                pygame.display.quit()

    return (mouseX, mouseY)


# distance between two points
def distance_a_b(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


# this function sorts the canteens by using the current position of the user
def sort_distance(current_position):
    list_canteens = []
    for canteen in database.canteensNTU.list:
        # distance between user location and each canteen
        list_canteens.append((distance_a_b(current_position, canteen.coordinates), canteen))

    list_canteens = sorted(list_canteens, key=lambda x: x[0])
    print("The canteens are sorted by distance from your position:")
    for element in list_canteens:
        print("Distance from your position to this canteen is", round(element[0], 2))
        element[1].info()
        print()


def get_user_location():
    # make necessary initializations for Width, Height
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
    sort_distance((buttonX, buttonY))
