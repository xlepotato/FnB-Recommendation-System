import get_user_location
import database
import user_interface
import pygame


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
                food_name = input("Enter the name of the food to search ")
                canList = database.canteensNTU.search_by_food(food_name)
                if canList is not None:
                    for i in canList:
                        i.info()  #print all the canteen info of the result that matches the given food name

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


