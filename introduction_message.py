# messages to appear at the start of application
def welcome_message():
    introduction = ["Welcome to our F&B recommendation app!!!"," ",
                    "In this app, we will help you identify and sort canteens/food based on your preferences."]
    return introduction

# messages to appear for user to select options from our list_of_options
def list_of_options():
    message_options = ["Below are the list of options you can choose from:"," ",
                       "Option a: List of canteens at NTU",
                       "Option b: Display canteens sorted by rank",
                       "Option c: Display canteens sorted by distance from your position",
                       "Option d: Search for canteens selling your preferred food",
                       "Option e: Search for food within a selected price range"," ",
                       "Otherwise, press z to exit the application."]
    return message_options