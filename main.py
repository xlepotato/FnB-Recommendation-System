import database
import pygame


# ------------------------- MouseClick -------------------------


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


# ------------------------------------------------------------------


# ------------------------- Get User Location ----------------------

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

    # get outputs of MouseClick event handler, and pass it to sort_by_distance
    database.canteensNTU.sort_by_distance(MouseClick())

# ------------------------------------------------------------------


# ------------------------- Intro Messages -------------------------


# messages to appear at the start of application
def welcome_message():
    introduction = ["Welcome to our F&B recommendation app!!!"," ",
                    "In this app, we will help you identify and sort canteens/food based on your preferences."]
    return introduction

# messages to appear for user to select options from our list_of_options
def list_of_options():
    message_options = ["Below are the list of options you can choose from:"," ",
                       "Option a: Display all information of canteens at NTU",
                       "Option b: Display information on a canteen by name"
                       "Option c: Display canteens sorted by rank",
                       "Option d: Display canteens sorted by distance from your position",
                       "Option e: Search for canteens selling your preferred food",
                       "Option f: Search for food within a selected price range"," ",
                       "Option g: Update rank of selected canteen"
                       "Otherwise, press z to exit the application."]
    return message_options

def list_of_canteens():
    canteen_list = [""]

# ------------------------------------------------------------------


def main():
    print()
    # print every line of message in welcome_message on one line in terminal
    for line_in_welcome in welcome_message():
        print(line_in_welcome)

    print()
    while True:
        # print every line of message in list_of_options on one line in terminal
        for line_in_options in list_of_options():
            print(line_in_options)
        print()

        # user selects the option listed in list_of_options
        user_option = input("Please select your preferred option (eg. a,b,c etc.): ")
        print()

        # user will be asked to select the options again if they select an option that is not listed in the list_of_options
        while not user_option == "a" and user_option == "b" and user_option == "c" and user_option == "d" and user_option == "e" and user_option == "f" and user_option == "z":
            print("Please select the option correctly.")
            user_option = input("Please select your preferred option (eg. a, b, c, etc.): ")
            print()

        # list of canteens at NTU
        if user_option == "a":
            database.canteensNTU.info()

        elif user_option == "b":
            database.canteensNTU.update_rank(canteen_id, rank)

        # Display canteens sorted by rank
        elif user_option == "c":
            database.canteensNTU.sort_by_rank()

        # Display canteens sorted by distance with respect to your current position
        elif user_option == "d":
            # get user's current_position from x,y coordinates in pygame display map and sort_by_distance
            get_user_location()

        # Search for canteens selling your preferred food
        elif user_option == "e":
            food_name = input("Enter the name of the food to search: ")
            database.canteensNTU.search_by_food(food_name)

        # Display food within a selected price range
        elif user_option == "f":
            print("Input two numbers denoting your preferred price range: ")
            input1 = input("Minimum value: ")
            input2 = input("Maximum value: ")
            try:
                float(input1)
                float(input2)
                if float(input1) > float(input2):
                    raise Exception("First input should be less than or equal to the second input!")
            except ValueError:
                print("Wrong input format!")
            except Exception as error:
                print(error)
            else:
                database.canteensNTU.search_by_price((float(input1), float(input2)))

        elif user_option == "g":


        # user to press z to exit the application
        elif user_option == "z":
            break

        # user to press y to continue or any other key to exit
        toContinue = input("Do you still want to continue? Enter 'Y' to continue, otherwise, enter any key to exit: ").capitalize()
        if toContinue == 'Y':
            continue
        else:
            print("Thank you for using our application ")
            break


if __name__ == '__main__':
    pygame.init()
    main()


