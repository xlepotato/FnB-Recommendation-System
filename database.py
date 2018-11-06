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
                        [Food("NA", "Big Mac", 4.2, "522")],
                        3.9, 'A', (220, 172), "6777 3777", "Mon to Sat: 7am to 12am, Sun & PH: 10am to 10pm", -1,
                        999, True, True
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