import get_user_location
import database
import user_interface
import pygame


def main():
    print()
    # print every line of message in welcome_message on one line in terminal
    for line_in_welcome in user_interface.welcome_message():
        print(line_in_welcome)

    print()
    while True:
        #print every line of message in list_of_options on one line in terminal
        for line_in_options in user_interface.list_of_options():
            print(line_in_options)
        print()

        # User selects the option listed in list_of_options
        user_option = input("Please select your preferred option (eg. a,b,c etc.): ")
        print()

        # user will be asked to select the options again if they select an option that is not listed in the list_of_options
        while not user_option == "a" and user_option == "b" and user_option == "c" and user_option == "d" and user_option == "e" and user_option == "f" and user_option == "z":
            print("Please select the option correctly.")
            user_option = input("Pls select your preferred option (eg. a,b,c etc.): ")
            print()

        # list of canteens at NTU
        if user_option == "a":
            database.canteensNTU.info()

        # Display canteens sorted by rank
        elif user_option == "b":

        # Display canteens sorted by distance with respect to your current position
        elif user_option == "c":
            # get user's current_position from x,y coordinates in pygame display map and sort_by_distance
            get_user_location.get_user_location()

        # Display food within a selected price range
        elif user_option == "d":

        # Search for canteens selling your preferred food
        elif user_option == "e":
        # canList = food.search_by_food("Hamburger", database.canteensNTU.retrieve_canteen())
        food_name = input("Enter the name of the food to search ")
        print(food_name)
        canList = database.canteensNTU.search_by_food(food_name)
        # print(canList)
        for i in canList:
            i.info()

        elif user_option == "z":
            break

        toContinue = input("Do you still want to continue? Enter 'Y' to continue or 'N' to exit: ").capitalize()
        if toContinue == 'Y':
            continue
        elif toContinue == 'N':
            print("Thank you for using our application ")
            break


if __name__ == '__main__':
    pygame.init()
    main()


