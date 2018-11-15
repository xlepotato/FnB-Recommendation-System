import database
import pygame
from nlp import chat


# ------------------------- MouseClick -------------------------
# define event handler for mouse click.
# this event handler will be fired (activated) when user clicks a mouse button anywhere in the display window
def MouseClick():
    mouseX,mouseY = (0,0)
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
    if (mouseX,mouseY) == (0,0):
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
    screen.blit(text1, (550, 20))

    # will update the contents of the entire display window
    pygame.display.flip()

    # get outputs of MouseClick event handler, and pass it to sort_by_distance
    database.canteensNTU.sort_by_distance(MouseClick())
# ------------------------------------------------------------------


# ------------------------- Intro Messages -------------------------
# messages to appear at the start of application
def welcome_message():
    introduction = ["Welcome to the F&B recommendation app!!! \n",
                    "Let me help you identify and sort canteens/food based on your preferences."]
    return introduction


# messages to appear for user to select options from our list_of_options
def list_of_options():
    message_options = ["Below are the list of options you can choose from:", " ",
                       "Option a: Display all the information of canteens at NTU",
                       "Option b: Display information of a canteen that you select",
                       "Option c: Display food menu of a canteen that you select",
                       "Option d: Display canteens sorted by Google Rank",
                       "Option e: Display canteens sorted by distance from your position",
                       "Option f: Search for canteens selling your preferred food",
                       "Option g: Search for food within a selected price range",
                       "Option h: Update rank of a selected canteen",
                       "Option i: Update food menu of a selected canteen",
                       "Option j: Add new food to the food menu of a selected canteen", " ",
                       "Otherwise, enter z to exit the application."]
    return message_options


# list of canteens to appear for user to select one
def list_of_canteens():
    canteen_list = ["0: Each A Cup",
                    "1: Food Court 1",
                    "2: Food Court 2",
                    "3: Food Court 16",
                    "4: Foodgle Food Court",
                    "5: KFC",
                    "6: Koufu @ the South Spine",
                    "7: McDonald's",
                    "8: NIE Canteen",
                    "9: North Spine Food Court",
                    "10: Subway",
                    "11: Quad Cafe", " "]
    return canteen_list


'''
Function Name: canteen_display()
Function Parameter: None
Function Return: canteen_id
Purpose: Display the list of canteen available and prompts user for canteen_id with validation check
'''


def canteen_display(user_option):
    # print every line of message in list_of_canteens on a new line
    for line_in_canteen_list in list_of_canteens():
        print(line_in_canteen_list)
    # Ensure that user will always input valid value
    while True:
        if user_option == 'h' or user_option == 'i':
            canteen_id_str = input("Input the canteen_id that you want to update: ")
        else:
            canteen_id_str = input("Input the canteen_id that you want to display: ")
        print()
        if canteen_id_str.isdigit():
            if 0 <= int(canteen_id_str) <= 11:
                canteen_id = int(canteen_id_str)
                break
            else:
                print("Please input an integer between 0 and 11 inclusive!")
                print()
        else:
            print("Please input a positive integer!")
            print()
    return canteen_id


'''
Function Name: food_display()
Function Parameter: None
Function Return: food_id
Purpose: Display the list of food available in a selected canteen and prompts user for food_id with validation check
'''


def food_display(canteen_id):
    food_number = 0
    # print every line of message in list_of_canteens on a new line with corresponding index
    for food in database.canteensNTU.list[canteen_id].foodMenu:
        print("{0}: {1}".format(food_number, food.name))
        food_number += 1
    print()
    # Ensure that user will always input valid value
    while True:
        food_id_str = input("Input the food id that you want to update: ")
        if food_id_str.isdigit():
            if 0 <= int(food_id_str) <= len(database.canteensNTU.list[canteen_id].foodMenu):
                food_id = int(food_id_str)
                break
            else:
                print("Please input an integer between 0 and", len(database.canteensNTU.list[canteen_id].foodMenu),
                      "inclusive!")
                print()
        else:
            print("Please input a positive integer!")
            print()
    return food_id
# ------------------------------------------------------------------


def main():
    print()
    # print every line of message in welcome_message on one line in terminal
    for line_in_welcome in welcome_message():
        print("bot : ",line_in_welcome)

    print()
    while True:
        # print every line of message in list_of_options on one line in terminal
        for line_in_options in list_of_options():
            print(line_in_options)
        print()

        # user selects the option listed in list_of_options
        user_option = input("Please select your preferred option (eg. a, b, c,  etc.): ")

        # user will be asked to select the options again if they select an option that is not listed
        while len(user_option) != 1 or ((not "a" <= user_option <= "j") and user_option != "z"):
            print("Please select the option correctly!")
            user_option = input("Please select your preferred option (eg. a, b, c, etc.): ")

        print()

        # Display all the information of canteens at NTU
        if user_option == "a":
            database.canteensNTU.info()

        # Display information on a selected canteen
        elif user_option == "b":
            # prompt user for the canteen id and display the list of canteen
            canteen_id = canteen_display(user_option)
            database.canteensNTU.list[canteen_id].info()

        # Display food menu of a selected canteen
        elif user_option == "c":
            # prompt user for the canteen id and display the list of canteen
            canteen_id = canteen_display(user_option)
            database.canteensNTU.list[canteen_id].menu()

        # Display canteens sorted by rank
        elif user_option == "d":
            database.canteensNTU.sort_by_rank()

        # Display canteens sorted by distance with respect to your current position
        elif user_option == "e":
            # get user's current_position from x,y coordinates in pygame display map and sort_by_distance
            print("bot : Select your current location on the map.")
            get_user_location()

        # Search for canteens selling your preferred food
        elif user_option == "f":
            food_name = input("Enter the name of the food to search: ")
            database.canteensNTU.search_by_food(food_name)

        # Display food within a selected price range
        elif user_option == "g":
            print("Input two numbers denoting your preferred price range: ")
            while True:
                input1 = input("Minimum value: ")
                input2 = input("Maximum value: ")
                try:
                    float(input1)
                    float(input2)
                    if float(input1) < 0.0 or float(input2) < 0.0:
                        raise Exception("Numbers should be positive!")
                    if float(input1) > float(input2):
                        raise Exception("First input should be less than or equal to the second input!")
                except ValueError:
                    print("Wrong input format, please input again!")
                except Exception as error:
                    print(error, "Input again!")
                else:
                    database.canteensNTU.search_by_price((float(input1), float(input2)))
                    break

        # Update rank of selected canteen
        elif user_option == "h":
            # prompt user for the canteen id and display the list of canteen
            canteen_id = canteen_display(user_option)
            while True:
                rank = input("Input the new rank for the canteen from 0.0 to 5.0: ")
                try:
                    float(rank)
                    if float(rank) < 0 or float(rank) > 5.0:
                        raise Exception("Please enter a value between 0 and 5 inclusive!")
                except ValueError:
                    print("Wrong input format, please input again!")
                except Exception as error:
                    print(error, "Input again!")
                else:
                    database.canteensNTU.update_rank(canteen_id, float(rank))
                    break

        # Update food in the food menu of selected canteen
        elif user_option == "i":
            # prompt user for the canteen id and display the list of canteen
            canteen_id = canteen_display(user_option)
            food_id = food_display(canteen_id)

            while True:
                new_price_str = input("Input a new price value for the food: ")
                try:
                    float(new_price_str)
                    if float(new_price_str) < 0:
                        raise Exception("Please enter a non-negative value!")
                except ValueError:
                    print("Wrong input format, please input again!")
                except Exception as error:
                    print(error, "Input again!")
                else:
                    new_price = float(new_price_str)
                    break

            while True:
                new_calorie_str = input("Input a non-negative integer for a new calorie of the food: ")
                try:
                    int(new_calorie_str)
                    if int(new_calorie_str) < 0:
                        raise Exception("Please enter a non-negative value!")
                except ValueError:
                    print("Wrong input format, please input again!")
                except Exception as error:
                    print(error, "Input again!")
                else:
                    break

            stall_name = database.canteensNTU.list[canteen_id].foodMenu[food_id].stall
            food_name = database.canteensNTU.list[canteen_id].foodMenu[food_id].name
            new_food = database.Food(stall_name, food_name, new_price, new_calorie_str)
            database.canteensNTU.update_food(canteen_id, food_id, new_food)

        # Add new food to the specified canteen
        elif user_option == "j":
            # prompt user for the canteen id and display the list of canteen
            canteen_id = canteen_display(user_option)
            stall_name = input("Please input the food stall name to add (input NA if it not applicable): ")
            food_name = input("Please input the name of the food to add: ")

            while True:
                new_price_str = input("Input a price value for the food: ")
                try:
                    float(new_price_str)
                    if float(new_price_str) < 0:
                        raise Exception("Please enter a non-negative value!")
                except ValueError:
                    print("Wrong input format, please input again!")
                except Exception as error:
                    print(error, "Input again!")
                else:
                    food_price = float(new_price_str)
                    break

            while True:
                new_calorie_str = input("Input a non-negative integer for a calorie of the food: ")
                try:
                    int(new_calorie_str)
                    if int(new_calorie_str) < 0:
                        raise Exception("Please enter a non-negative value!")
                except ValueError:
                    print("Wrong input format, please input again!")
                except Exception as error:
                    print(error, "Input again!")
                else:
                    break

            new_food = database.Food(stall_name, food_name, food_price, new_calorie_str)
            database.canteensNTU.add_food(canteen_id, new_food)

        # user to press z to exit the application
        elif user_option == "z":
            break

        # user to press y to continue or any other key to exit
        print()
        toContinue = input("Do you still want to continue? Enter 'Y' to continue, otherwise, enter any key to exit: ").capitalize()
        if toContinue == 'Y':
            continue
        else:
            print("Thank you for using our application ")
            break


if __name__ == '__main__':
    pygame.init()
    keep_looping = True
    while keep_looping:
        result = chat()
        # print(result)
        if result:
            main()
        else:
            break




