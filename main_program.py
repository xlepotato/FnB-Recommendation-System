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
    while True:
        for interface2 in user_interface.userinterface2():
            print(interface2)
        print()

        user_option = input("Pls select your preferred option (eg. a,b,c etc.): ")
        print()

        while not user_option == "a" and user_option == "b" and user_option == "c" and user_option == "d" and user_option == "e" and user_option == "f" and user_option == "z":
            print("Please select the option correctly.")
            user_option = input("Pls select your preferred option (eg. a,b,c etc.): ")
            print()
        else:
            if user_option == "a":
                database.canteensNTU.info()
            elif user_option == "e":
                #canList = food.search_by_food("Hamburger", database.canteensNTU.retrieve_canteen())
                canList = database.canteensNTU.search_by_food("Hamburger")
                # print(canList)
                for i in canList:
                    i.info()

            elif user_option == "b":
                print("Nyan")
            elif user_option == "c":
                get_user_location.get_user_location()
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