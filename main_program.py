import get_user_location
import database
import user_interface
import pygame


def main():
    print()
    for line_in_welcome in user_interface.welcome_message():
        print(line_in_welcome)
    print()
    while True:
        for line_in_options in user_interface.list_of_options():
            print(line_in_options)
        print()

        user_option = input("Pls select your preferred option (eg. a,b,c etc.): ")
        print()

        while not user_option == "a" and user_option == "b" and user_option == "c" and user_option == "d" and user_option == "e" and user_option == "f" and user_option == "z":
            print("Please select the option correctly.")
            user_option = input("Pls select your preferred option (eg. a,b,c etc.): ")
            print()

        if user_option == "a":
            database.canteensNTU.info()
        elif user_option == "b":
            pass
        elif user_option == "c":
            get_user_location.get_user_location()
        elif user_option == "d":
            pass
        elif user_option == "e":
            food_name = input("Enter the name of the food to search ")
            canList = database.canteensNTU.search_by_food(food_name)
            if canList is not None:
                for i in canList:
                    i.info()  # print all the canteen info of the result that matches the given food name

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


