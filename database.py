class Food:
    def __init__(self, stall, name, price, calorie):
        self.stall = stall
        self.name = name
        self.price = price
        self.calorie = calorie

    def description(self):
        return "Food {} from {} stall costs ${} and has {} kcal".format(self.name, self.stall, self.price, self.calorie)

    def get_stall(self):
        return self.stall

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_calorie(self):
        return self.calorie

    def set_stall(self, stall):
        self.stall = stall
    def set_name(self, name):
        self.name = name
    def set_price(self,price):
        self.price = price
    def set_calorie(self, calorie):
        self.calorie = calorie


class Canteen:
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

    '''
        Function: Getter Methods
        Purpose: To retrieve a particular attributes from the Canteen class
    '''
    def get_name(self):
        return self.name
    def get_address(self):
        return self.address
    def get_isHalal(self):
        return self.isHalal
    def get_isVegetarian(self):
        return self.isVegetarian
    def get_foodMenu(self):
        return self.foodMenu
    def get_rank(self):
        return self.rank
    def get_hygieneID(self):
        return self.hygieneID
    def get_coordinates(self):
        return self.coordinates
    def get_handPhone(self):
        return self.handPhone
    def get_workingTime(self):
        return self.workingTime
    def get_numberOfStalls(self):
        return self.numberOfStalls
    def get_capacity(self):
        return self.capacity
    def get_isOpenWkd(self):
        return self.isOpenWkd
    def get_isOpenPH(self):
        return self.isOpenPH

    '''
        Function: Setter Methods
        Purpose: To set a new value for a particular attributes in the Canteen class
    '''
    def set_address(self, address):
        self.stall = address
    def set_name(self, name):
        self.name = name
    def set_isHalal(self, isHalal):
        self.isHalal = isHalal
    def set_isVegetarian(self, isVegetarian):
        self.isVegetarian = isVegetarian
    def set_foodMenu(self, foodMenu):
        self.foodMenu = foodMenu
    def set_rank(self, rank):
        self.rank = rank
    def set_hygieneID(self, hygieneID):
        self.hygieneID = hygieneID
    def set_coordinates(self, coordinates):
        self.coordinates = coordinates
    def set_handPhone(self, handPhone):
        self.handPhone = handPhone
    def set_workingTime(self, workingTime):
        self.workingTime = workingTime
    def set_numberOfStalls(self, price):
        self.price = price
    def set_capacity(self, capacity):
        self.capacity = capacity
    def set_isOpenWkd(self, isOpenWkd):
        self.isOpenWkd = isOpenWkd
    def set_isOpenPH(self, isOpenPH):
        self.isOpenPH = isOpenPH


    def menu(self):
        print("Canteen", self.name, "has foods like:")
        for food in self.foodMenu:
            print(food.description())


    def info(self):
        print("Name:", self.name)
        print("Address:", self.address)
        print("Is Halal:", "Yes" if self.isHalal == True else "No")
        print("Is Vegetarian:", "Yes" if self.isVegetarian == True else "No")
        print("Rank on Google Maps:", self.rank)
        print("Hygiene rank:", self.hygieneID)
        print("Hand Phone:", self.handPhone)
        print("Working time:", self.workingTime)
        print("Number of stalls:", self.numberOfStalls if self.numberOfStalls > 0 else "NA")
        print("Seat Capacity:", self.capacity if self.capacity > 0 else "NA")
        print("Open on weekends:", "Yes" if self.isOpenWkd == True else "No")
        print("Open on public holidays:", "Yes" if self.isOpenPH == True else "No")


class ListOfCanteens:
    def __init__(self):
        self.list = []

    def add(self, newCanteen):
        self.list.append(newCanteen)

    def info(self):
        for canteen in self.list:
            canteen.info()
            print()
            canteen.menu()
            print()

   # def retrieve_canteen_by_food_name(self):
       # for canteen in self-list:





canteensNTU = ListOfCanteens()
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