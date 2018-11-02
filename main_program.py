import pygame


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

    return (mouseX, mouseY)


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
    print("Your current coordinates is:", (buttonX, buttonY))


def userinterface1():
    user_options1 = ["Welcome to our F&B recommendation app!!!",
                     "In this app, we will help you identify, sort food courts based on your preferences.",
                     "Please select your current location in the map displayed after this message"]
    return user_options1


def userinterface2():
    user_options2 = ["To list all the canteens in NTU, please press 1",
                     "To search for a canteen near you, please press 2",
                     "To search for a canteen with your preferred food, please press 3",
                     "To display canteens by rank, please press 4",
                     "To search for food within a selected price range, please press 5",
                     "To display canteens by distance nearest to you, please press 6"]
    return user_options2


def main():
    for something in userinterface1():
        print(something)
    pygame.init()
    get_user_location()
    for something2 in userinterface2():
        print(something2)
    User_options = input("Option: ")


if __name__ == '__main__':
    main()

print("hey")


print("wan ying")


print ("yoloooo")

print("weee")