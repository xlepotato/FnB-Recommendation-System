class Food:
    def __init__(self, stall, name, price, calorie):
        self.stall = stall
        self.name = name
        self.price = price
        self.calorie = calorie

    def description(self):
        return "Food {} from stall {} costs ${} and has {}".format(self.name, self.stall, self.price, self.calorie)

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
        print("Capacity:", self.capacity if self.capacity > 0 else "NA")
        print("Is open on weekends:", "Yes" if self.isOpenWkd == True else "No")
        print("Is open on public holidays:", "Yes" if self.isOpenPH == True else "No")


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



canteensNTU = ListOfCanteens()
canteensNTU.add(Canteen("McDonald's", "North Spine Plaza 76 Nanyang Drive N2.1-01-08 Singapore 637331", True, True,
                        [Food("NA", "Big Mac", 4.2, "522 kcal")],
                        3.9, 'A', (220, 172), "6777 3777", "Mon to Sat: 7am to 12am, Sun & PH: 10am to 10pm", -1,
                        999, True, True
                        ))

canteensNTU.info()
