import database

def search_by_food(food_name, food_list_canteens):
    canList = []
    # for canteen in food_list_canteens:
    #     if canteen.name == food_name:
    #         canList.append(canteen)
    # list = database.canteensNTU.retrieve_canteen()
    print(food_list_canteens[1].name)
   # print(list[1].name)
    for canteen in food_list_canteens:
        for food in canteen:
            if food.name == food_name:
                print("found")
            else:
                print("Not found")
    return



# if __name__ == '__main__':
#     value = search_by_food("apple",database.canteensNTU)
#     print (value)


