import sort_by_distance
import database
import introduction_message
import pygame


def main():
    print()
    # print every line of message in welcome_message on one line in terminal
    for line_in_welcome in introduction_message.welcome_message():
        print(line_in_welcome)

    print()
    while True:
        # print every line of message in list_of_options on one line in terminal
        for line_in_options in introduction_message.list_of_options():
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

        # Display canteens sorted by rank
        elif user_option == "b":
            database.canteensNTU.sort_by_rank()

        # Display canteens sorted by distance with respect to your current position
        elif user_option == "c":
            # get user's current_position from x,y coordinates in pygame display map and sort_by_distance
            sort_by_distance.get_user_location()

        # Search for canteens selling your preferred food
        elif user_option == "d":
            food_name = input("Enter the name of the food to search: ")
            database.canteensNTU.search_by_food(food_name)

        # Display food within a selected price range
        elif user_option == "e":
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


