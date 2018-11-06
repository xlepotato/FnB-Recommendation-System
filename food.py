import database

def search_by_food(food_name, food_list_canteens):
    canList = []
    for canteen in food_list_canteens:
        if canteen.name == food_name:
            canList.append(canteen)
    # list = database.canteensNTU.retrieve_canteen()
   # print(list[1].name)
    return canList



# if __name__ == '__main__':
#     value = search_by_food("apple",database.canteensNTU)
#     print (value)


