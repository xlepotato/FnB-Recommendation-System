from math import sqrt

# distance between two points
def distance_a_b(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


# Separate class for the Food
class Food:
    # initialization when the Food class is created
    def __init__(self, stall, name, price, calorie):
        self.stall = stall
        self.name = name
        self.price = price
        self.calorie = calorie

    # returns the string description of the Food
    def description(self):
        result = "Food {}".format(self.name)
        if self.stall != "NA":
            result = result + " from stall {}".format(self.stall)
        result = result + " costs ${}".format(self.price)
        if self.calorie != "NA":
            result = result + " and has {} kcal".format(self.calorie)
        return result

    # updates the food information
    def update(self, new_stall, new_name, new_price, new_calorie):
        self.stall = new_stall
        self.name = new_name
        self.price = new_price
        self.calorie = new_calorie


# Separate class for the Canteen
class Canteen:
    # initialization when the Canteen class is created
    def __init__(self, name, address, isHalal, isVegetarian, foodMenu, rank, hygieneID, coordinates,
                 handPhone, workingTime, numberOfStalls, capacity, isOpenWkd, isOpenPH):
        self.name = name
        self.address = address
        self.isHalal = isHalal
        self.isVegetarian = isVegetarian
        self.foodMenu = foodMenu
        self.rank = rank
        self.hygieneID = hygieneID
        self.coordinates = coordinates
        self.handPhone = handPhone
        self.workingTime = workingTime
        self.numberOfStalls = numberOfStalls
        self.capacity = capacity
        self.isOpenWkd = isOpenWkd
        self.isOpenPH = isOpenPH

    # prints the menu description of the Canteen
    def menu(self):
        print("Canteen", self.name, "has foods like:")
        for food in self.foodMenu:
            print(food.description())

    def add_food_to_menu(self, new_food):
        self.foodMenu.append(new_food)

    # prints the information of the Canteen
    def info(self):
        print("Name:", self.name)
        print("Address:", self.address)
        print("Is Halal:", "Yes" if self.isHalal is True else "No")
        print("Is Vegetarian:", "Yes" if self.isVegetarian is True else "No")
        print("Rank on Google Maps:", self.rank)
        print("Hygiene rank:", self.hygieneID)
        print("Hand Phone:", self.handPhone)
        print("Working time:", self.workingTime)
        print("Number of stalls:", self.numberOfStalls if self.numberOfStalls > 0 else "NA")
        print("Seat Capacity:", self.capacity if self.capacity > 0 else "NA")
        print("Open on weekends:", "Yes" if self.isOpenWkd is True else "No")
        print("Open on public holidays:", "Yes" if self.isOpenPH is True else "No")

    # updates the rank of the canteen
    def update_rank(self, new_rank):
        self.rank = new_rank


# distance between two points
def distance_a_b(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


# Separate class for the List of Canteens
class ListOfCanteens:
    # initialization when the List of Canteens class is created
    def __init__(self):
        self.list = []

    # adding a new canteen to the list
    def add(self, newCanteen):
        self.list.append(newCanteen)

    # prints all the information of canteens in the list
    def info(self):
        for canteen in self.list:
            canteen.info()
            print()
            canteen.menu()
            print()

    # search for the canteens which has the foodName in the menu
    # returns the list of canteens
    def search_by_food(self, foodName):
        found = False
        result = []
        for canteen in self.list:
            for food in canteen.foodMenu:
                if food.name == foodName:
                    result.append(canteen)
                    found = True
        if found:
            print("Below are the canteens that have {}:".format(foodName))
            for canteen in result:
                print(canteen.name)
        else:
            print("No search result was found :(")

    # search for the canteens which has the food with prince within the given range
    # returns the list of tuples in format (canteen, foodList)
    def search_by_price(self, priceRange):
        result = []
        found = False
        for canteen in self.list:
            list_foods = []
            for food in canteen.foodMenu:
                if priceRange[0] <= food.price <= priceRange[1]:
                    list_foods.append(food)
                    found = True
            result.append((canteen, list_foods))
        if found:
            print("Below are the canteens that have food with price between {} and {}:".format(priceRange[0], priceRange[1]))
            for element in result:
                if len(element[1]) > 0:
                    print("Canteen {} has foods like: ".format(element[0].name))
                    for food in element[1]:
                        print(food.description())
                    print()
        else:
            print("No search result was found :(")
        return result

    # this function sorts the canteens by using the current position of the user
    def sort_by_distance(self, current_position):
        list_canteens = []
        if current_position == (0,0):
            pass
        else:
            for canteen in self.list:
                # distance between user location and each canteen
                list_canteens.append((distance_a_b(current_position, canteen.coordinates), canteen))

            list_canteens = sorted(list_canteens, key=lambda x: x[0])
            print("The canteens are sorted by distance from your position:")
            for element in list_canteens:
                print("Distance from your position to this canteen is", round(element[0], 2))
                element[1].info()
                print()

    # this function sorts the canteens by google rank
    def sort_by_rank(self):
        list_canteens = []
        for canteen in self.list:
            # distance between user location and each canteen
            list_canteens.append((canteen.rank, canteen))

        list_canteens = sorted(list_canteens, key=lambda x: x[0], reverse=True)
        print("The canteens are sorted by Google Rank:")
        for element in list_canteens:
            print("The rank of this canteen is: ", element[0])
            element[1].info()
            print()

    # update the rank of some canteen from the list
    def update_rank(self, canteen_id, new_rank):
        self.list[canteen_id].rank = new_rank

    # add the new food for some canteen from the list
    def add_food(self, canteen_id, new_food):
        self.list[canteen_id].add_food_to_menu(new_food)

    # update the food info for some canteen from the list
    def update_food(self, canteen_id, food_id, new_food):
        self.list[canteen_id].foodMenu[food_id] = new_food


# canteensNTU has all the data
canteensNTU = ListOfCanteens()

# separately adding information of each canteen to the database

canteensNTU.add(Canteen("Each A Cup", "North Spine Plaza, 50 Nanyang Avenue, NS3-01-21, Singapore 639798", True, True,
                        [Food("NA", "Ice Cream Black Tea", 3.2, "NA"),
                         Food("NA", "Green Tea Macchiato", 2.7, "NA"),
                         Food("NA", "Grape Red Tea", 2.8, "NA"),
                         Food("NA","Honey Green Tea", 2.8, "NA"),
                         Food("NA", "Plum Red Tea", 2.8, "NA"),
                         Food("NA","Milo Ice", 3.0, "NA"),
                         Food("NA", "Earl Grey Milk Tea", 3.0, "NA"),
                         Food("NA","Fresh Lemon Lime Juice", 3.0, "NA"),
                         Food("NA", "Jasmine Green Tea", 2.1, "NA"),
                         Food("NA", "Yakult Green Tea", 3.5, "NA"),
                         Food("NA", "Caramel Milk Tea", 3.5, "NA"),
                         Food("NA","Oreo Crush", 2.9, "NA")],
                        3.2, 'NA', (240, 184), "9182 9307", "Mon to Fri: 9am to 9pm, Sat & Sun: 9am to 6pm", -1,
                        -1, True, False
                        ))
canteensNTU.add(Canteen("Food Court 1", "21 Nanyang Circle, Hall 1, Singapore 639778", False, False,
                        [Food("Economical Rice", "Steam Pork Rice", 3.5, "500"),
                         Food("Economical Rice", "Old Cucumber & Pork Ribs Soup", 2.3, "446"),
                         Food("Economical Rice", "Winter Melon Pork Ribs Soup", 2.3, "102"),
                         Food("Chinese Cuisine", "Spicy Chicken", 3.5, "549"),
                         Food("Chinese Cuisine", "Spicy Pork", 3.5, "442"),
                         Food("Chinese Cuisine", "Chilli Prawn", 3.0, "573"),
                         Food("Handmade Noodle", "Seafood Soup", 4.0, "238"),
                         Food("Handmade Noodle", "Ban Mian", 3.5, "485"),
                         Food("Mala Talk", "Chicken Soup w/ Rice", 4.0, "500"),
                         Food("Mala Talk", "Mala Hotpot", 5.0, "NA"),
                         Food("Western Cuisine", "Beef Bolognese", 5.5, "505"),
                         Food("Western Cuisine", "Chicken Cutlet", 5.5, "576")],
                        3.1, 'NA', (379, 358), "6334 3033", "Mon to Fri: 7am to 9pm, Sat & Sun: 7am to 9pm", 5,
                        310, True, True
                        ))
canteensNTU.add(Canteen("Food Court 2", "35 Students Walk, Hall 2, Singapore 639548", True, True,
                        [Food("Japanese Western", "Plain Yakisoba", 4.0, "450"),
                         Food("Japanese Western", "Curry Omelette", 5.0, "520"),
                         Food("Ayam Penyet", "Ayam Penyet Set", 4.8, "738"),
                         Food("Ayam Penyet", "Ikan Dory Penyet Set", 4.5, "690"),
                         Food("Chicken Rice", "Steamed Chicken Rice", 2.8, "475"),
                         Food("Chicken Rice", "Roasted Chicken Rice", 3.8, "550"),
                         Food("Korean Cuisine", "BBQ Beef", 4.9, "564"),
                         Food("Korean Cuisine", "Korean Rice Cake", 3.8, "532"),
                         Food("Sichuan Cuisine", "Double Cooked Sliced Pork", 5.5, "528"),
                         Food("Sichuan Cuisine", "Spicy Fish", 7.5, "489"),
                         Food("Xiao Long Bao", "Fresh Prawn Chicken Siew Mai", 4.3, "229"),
                         Food("Shandong Big Bun", "Liang Ban Seaweed", 1.0, "181")],
                        4.2, 'B', (420, 286), "6334 3033", "Mon to Fri: 7am to 9pm, Sat & Sun: 7am to 9pm", 7,
                        446, True, True
                        ))

canteensNTU.add(Canteen("Food Court 16", "50 Nanyang Walk Singapore 639929", True, True,
                        [Food("Japanese Cuisine", "Kaki Fuyong Oyster", 4.8, "450"),
                         Food("Japanese Cuisine", "Curry Don", 3.9, "520"),
                         Food("Muslim Food", "Nasi Lemak", 2.9, "465"),
                         Food("Muslim Food", "Mee Siam", 2.5, "432"),
                         Food("Dim Sum", "Red Bean Bun", 0.6, "147"),
                         Food("Dim Sum", "Soon Kueh", 0.5, "119"),
                         Food("Ban Mian & Fish Soup", "Seafood Ban Mian", 4.5, "528"),
                         Food("Ban Mian & Fish Soup", "Fried Fish Soup", 5.0, "489"),
                         Food("Chicken Rice", "Hainanese Chicken Rice", 3.5, "492"),
                         Food("Chicken Rice", "Chicken Porridge", 2.2, "489"),
                         Food("Noodle", "Mushroom Minced Meat", 3.0, "500"),
                         Food("Noodle", "Prawn Mee", 3.5, "455")],
                        3.9, 'B', (321, 97), "9450 5893", "Mon to Fri: 7am to 9pm, Sat: 7am to 9pm", 5,
                        304, True, False
                        ))

canteensNTU.add(Canteen("Foodgle Food Court", "38 Nanyang Crescent Blk 23, #051 - 058 Singapore 636866", True, True,
                        [Food("Indian Cuisine", "Prata", 4.00, "450"),
                         Food("Indian Cuisine", "Curry Chicken", 5.00, "520"),
                         Food("Ayam Penyet", "Ayam Penyet Set", 4.8, "738"),
                         Food("Ayam Penyet", "Ikan Dory Penyet Set", 4.5, "690"),
                         Food("Ayam Penyet", "Udang Penyet Set", 5.00, "500"),
                         Food("Ayam Penyet", "Fried Ayam Penyet Set", 5.30, "800"),
                         Food("Chicken Rice", "Steamed Chicken Rice", 2.8, "475"),
                         Food("Chicken Rice", "Roasted Chicken Rice", 3.8, "550"),
                         Food("Korean Cuisine", "Ramyun", 4.9, "564"),
                         Food("Korean Cuisine", "Korean Rice Cake", 3.8, "532"),
                         ],
                        3.0, 'B', (599, 69), "8296 3633", "Mon to Sun: 7am to 9pm", 9,
                        440, True, True
                        ))

canteensNTU.add(Canteen("KFC", "North Spine Plaza 76 Nanyang Drive N2.1-01-04 Singapore 637331", True, True,
                        [Food("NA", "Chicken Share Meal", 16.95, "NA"),
                         Food("NA", "Tenders Share Meal", 16.95, "NA"),
                         Food("NA", "Nuggets Share Meal", 16.95, "NA"),
                         Food("NA", "Signature Grilled Chicken Meal", 10.95, "NA"),
                         Food("NA", "Variety Feast", 39.95, "NA"),
                         Food("NA", "Zinger Stacker Box", 11.55, "NA"),
                         Food("NA", "BBQ Pockett Box", 9.95, "NA"),
                         Food("NA", "Tenders Box", 8.95, "NA"),
                         Food("NA", "Cheesy Zinger Stacker", 7.20, "NA"),
                         Food("NA", "Original Recipe Rice Bucket", 5.50, "NA")
                         ],
                        3.1, 'A', (216, 151), "6762 6124", "Mon to Fri: 7.30am to 10pm - Sat & Sun: 11am to 8pm", -1,
                        999, True, False
                        ))

canteensNTU.add(Canteen("Koufu @ the South Spine", "50 Nanyang Avenue SS3-B4 Singapore 639798", True, True,
                        [Food("Japanese Cuisine", "Kaki Fuyong Oyster", 2.70, "450"),
                         Food("Japanese Cuisine", "Curry Don", 3.50, "520"),
                         Food("Japanese Cuisine", "Tempura Bento Set", 5.5, "738"),
                         Food("Muslim Food", "Nasi Lemak", 3.2, "465"),
                         Food("Muslim Food", "Mee Rebus", 3.0, "432"),
                         Food("Dim Sum", "Wholemeal Red Bean Bun", 0.7, "550"),
                         Food("Dim Sum", "Soon Kueh", 0.6, "119"),
                         Food("Pasta Express", "Carbonara", 3.8, "5322"),
                         Food("Pasta Express", "Tomato Pasta", 3.8, "522"),
                         Food("Ban Mian & Fish Soup", "Seafood Ban Mian", 3.5, "528"),
                         Food("Ban Mian & Fish Soup", "Fried Fish Soup", 3.5, "489"),
                         Food("Chicken Rice", "Hainanese Chicken Rice", 3.0, "489"),
                         Food("Chicken Rice", "Chicken Porridge", 3.0, "489"),
                         Food("Noodle", "Mushroom Minced Meat", 3.5, "500"),
                         Food("Noodle", "Prawn Mee", 3.8, "455")],
                        3.6, 'B', (133, 375), "6790 0355", "Mon to Fri: 7am to 9pm, Sat: 7am to 3pm", 15,
                        1050, True, False
                        ))

canteensNTU.add(Canteen("McDonald's", "North Spine Plaza 76 Nanyang Drive N2.1-01-08 Singapore 637331", True, True,
                        [Food("NA", "Big Mac", 4.2, "522"),
                         Food("NA", "McSpicy", 3.0, "522"),
                         Food("NA", "McChicken", 3.0, "385"),
                         Food("NA", "Cheeseburger", 2.0, "300"),
                         Food("NA", "Hamburger", 1.5, "252"),
                         Food("NA", "McWings", 4.0, "498"),
                         Food("NA", "BBQ Beef Burger with Egg", 4.0, "450"),
                         Food("NA", "Mango Peach Chiller", 3.0, "200"),
                         Food("NA", "ChocoCone", 3.0, "295"),
                         Food("NA", "Mudpie McFlurry", 5.0, "532")],
                        3.9, 'A', (220, 172), "6777 3777", "Mon to Sat: 7am to 12am, Sun & PH: 10am to 10pm", -1,
                        999, True, True
                        ))

canteensNTU.add(Canteen("NIE Canteen", "1 Nanyang Walk, Singapore 637616", True, True,
                        [Food("Muslim Food", "Nasi Lemak", 2.70, "450"),
                         Food("Muslim Food", "Mee Rebus", 2.00, "520"),
                         Food("Muslim Food", "Mee Siam", 4.8, "738"),
                         Food("Chicken Rice", "Hainanese Chicken Rice", 2.5, "475"),
                         Food("Chicken Rice", "Chicken Porridge", 2.5, "475"),
                         Food("Ban Mian & Fish Soup", "Double Fish Soup with Rice", 4.2, "550"),
                         Food("Snack and Soft Drinks", "Big Chicken Pau", 0.8, "119"),
                         Food("Snack and Soft Drinks", "Char Siew Pau", 0.6, "102"),
                         Food("Western Food", "Chicken Cutlet", 3.5, "532"),
                         Food("Western Food", "Mexican Chicken Chop", 4.5, "528"),
                         Food("Western Food", "Tempura Fish", 3.5, "489"),
                         Food("Noodle", "Mushroom Minced Meat", 2.5, "500"),
                         Food("Noodle", "Prawn Mee", 2.5, "455")],
                        4.3, 'B', (189, 42), "6790 3888", "Mon to Fri: 7am to 9pm, Sat & Sun: 7am to 9pm", 14,
                        1576, False, False
                        ))

canteensNTU.add(Canteen("North Spine Food Court", "North Spine Plaza, 76 Nanyang Drive, NS2.1-02-03/01A, Singapore 637331", True, True,
                        [Food("Mini Wok", "Seafood Hokkien Mee", 4.0, "NA"),
                         Food("Mini Wok", "Sambal Long Bean w/ Pork", 4.5, "NA"),
                         Food("Yong Tau Foo", "Fishball Noodle", 3.0, "NA"),
                         Food("Yong Tau Foo", "Fishball Soup", 3.0, "NA"),
                         Food("Chicken Rice", "Roasted Chicken Rice", 3.0, "NA"),
                         Food("Handmade Noodle", "Dumpling Ban Mian", 4.0, "NA"),
                         Food("Cantonese Roasted Duck", "Roasted Duck Rice", 3.0, "NA"),
                         Food("Western Food", "Chicken Chop", 5.0, "NA"),
                         Food("Western Food", "Beef Steak Rice", 6.0, "NA"),
                         Food("Vegetarian", "Vegetarian Rice Set", 3.0, "NA"),
                         Food("Vegetarian", "Vegetarian Bee Hoon Set", 3.0, "NA"),
                         Food("Malay BBQ", "Fried Chicken White Rice", 4.0, "NA"),
                         Food("Indian Cuisine", "Mutton Biryani", 4.5, "NA"),
                         Food("Indian Cuisine", "Curry Chicken Biryani", 4.5, "NA")],
                        3.6, 'B', (212, 170), "6465 8588", "Mon to Fri: 7am to 9pm, Sat: 7am to 3pm", 9,
                        1838, True, False
                        ))

canteensNTU.add(Canteen("Subway", "North Spine Plaza 76 Nanyang Drive N2.1-01-04 Singapore 637331", True, True,
                        [Food("NA", "Chicken Bacon Ranch Sandwich", 6.95, "NA"),
                         Food("NA", "Chicken Teriyaki Sandwich", 6.95, "NA"),
                         Food("NA", "Cold Cut Trio Sandwich", 6.95, "NA"),
                         Food("NA", "Egg Mayo Sandwich", 4.95, "NA"),
                         Food("NA", "Italian B.M.T. Sandwich", 7.95, "NA"),
                         Food("NA", "Veggie Delite Sandwich", 4.55, "NA"),
                         Food("NA", "Veggie Patty Sandwich", 4.95, "NA"),
                         Food("NA", "Egg & Cheese Flatbread", 3.95, "NA"),
                         Food("NA", "Roasted Chicken Breast Sandwich", 5.20, "NA"),
                         Food("NA", "Tuna Sandwich", 5.50, "NA")
                         ],
                        3.7, 'A', (212, 166), "6462 5238", "Mon to Fri: 8am to 9pm, Sat & Sun: 11am to 6pm", -1,
                        999, True, False
                        ))

canteensNTU.add(Canteen("Quad Cafe", "60 Nanyang Drive SBS-B1N-10 Singapore 637551", True, True,
                        [Food("Japanese Cuisine", "Kaki Fuyong Oyster", 3.8, "450"),
                         Food("Japanese Cuisine", "Curry Don", 3.3, "520"),
                         Food("Muslim Food", "Nasi Lemak", 3.8, "465"),
                         Food("Muslim Food", "Mee Rebus", 3.5, "432"),
                         Food("Dim Sum", "Red Bean Bun", 0.6, "550"),
                         Food("Dim Sum", "Soon Kueh", 0.5, "119"),
                         Food("Ban Mian & Fish Soup", "Seafood Ban Mian", 4.0, "528"),
                         Food("Ban Mian & Fish Soup", "Fried Fish Soup", 4.5, "489"),
                         Food("Chicken Rice", "Hainanese Chicken Rice", 3.5, "492"),
                         Food("Chicken Rice", "Chicken Porridge", 3.2, "489"),
                         Food("Noodle", "Mushroom Minced Meat", 3.6, "500"),
                         Food("Noodle", "Prawn Mee", 4.0, "455")],
                        3.9, 'B', (125, 269), "9638 0392", "Mon to Fri: 7am to 9pm, Sat: 7am to 3pm", 8,
                        500, True, False
                        ))