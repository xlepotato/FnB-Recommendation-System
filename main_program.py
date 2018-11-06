import get_user_location
import database
import user_interface
from time import sleep
import pygame
import sort_distance
import food
import sort_by_rank
import search_by_price



def main():
    print()
    for interface1 in user_interface.userinterface1():
        print(interface1)
    print()

    #preference_halal = input("Are you a Muslim (Pls enter True or False): ")
    #print()
    #preference_vegetarian = input("Are you a vegetarian (Pls enter True or False): ")
    #print()

    while True:
        for interface2 in user_interface.userinterface2():
            print(interface2)
        print()

        User_options = input("Pls select your preferred option (eg. a,b,c etc.): ")
        print()

        while not User_options == "a" and "b" and "c" and "d" and "e" and "f":
            print("Please select the option correctly.")
            User_options = input("Pls select your preferred option (eg. a,b,c etc.): ")
            print()
        else:


            if User_options == "a":
                database.canteensNTU.info()
            elif User_options == "e":
                canList = food.search_by_food("Hamburger", database.canteensNTU.retrieve_canteen())
                print(canList)

            elif User_options == "b":
                print("Nyan")
                #
                # Continue = input("Please enter z to return to the options menu, otherwise press any key to exit: ")
                # if Continue == "z":
                #     pass
                # else:
                #     break
            elif User_options == "c":
                get_user_location.get_user_location()
            elif User_options == "z":
                break

            toContinue = input("Do you still want to continue? Enter 'Y' to continue or 'N' to exit").capitalize()
            if toContinue == 'Y':
                continue
            elif toContinue == 'N':
                print("Thank you for using our application ")
                break


    # while True:
    #     for interface2 in user_interface.userinterface2():
    #         print(interface2)
    #     print()
    #
    #     User_options = input("Pls select your preferred option (eg. a,b,c etc.): ")
    #     print()
    #
    #     while not User_options == "a" and "b" and "c" and "d" and "e" and "f":
    #         print("Please select the option correctly.")
    #         User_options = input("Pls select your preferred option (eg. a,b,c etc.): ")
    #         print()
    #
    #     if User_options == "a":
    #         database.canteensNTU.info()
    #     elif User_options == "e":
    #         canList = food.search_by_food("Hamburger",database.canteensNTU)
    #         print(canList)
    #
    #     elif User_options == "b":
    #         print("Nyan")
    #
    #     Continue = input("Please enter z to return to the options menu, otherwise press any key to exit: ")
    #     if Continue == "z":
    #         pass
    #     else:
    #         break




if __name__ == '__main__':
    pygame.init()
    main()
