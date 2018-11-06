import sort_by_distance
import database
import introduction_message
import pygame


def main():
    print()
    for line_in_welcome in introduction_message.welcome_message():
        print(line_in_welcome)
    print()
    while True:
        for line_in_options in introduction_message.list_of_options():
            print(line_in_options)
        print()

        user_option = input("Please select your preferred option (eg. a, b, c, etc.): ")
        print()

        while not user_option == "a" and user_option == "b" and user_option == "c" and user_option == "d" and user_option == "e" and user_option == "f" and user_option == "z":
            print("Please select the option correctly.")
            user_option = input("Please select your preferred option (eg. a, b, c, etc.): ")
            print()

        if user_option == "a":
            database.canteensNTU.info()
        elif user_option == "b":
            database.canteensNTU.sort_by_rank()
        elif user_option == "c":
            sort_by_distance.get_user_location()
        elif user_option == "d":
            food_name = input("Enter the name of the food to search: ")
            database.canteensNTU.search_by_food(food_name)
        elif user_option == "e":
            print("Input two numbers denoting your preferred price range: ")
            x = (int)(input("Minimum value: "))
            y = (int)(input("Maximum value: "))
            database.canteensNTU.search_by_price((x, y))
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


