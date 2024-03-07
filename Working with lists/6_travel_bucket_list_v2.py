import easygui


def travel_bucket_list():
    bucket_list = ""
    places = easygui.enterbox("Enter the names of 5 places you would most "
                              "like to visit\n"
                              "Separate each place name with a comma and space",
                              "Enter favourite places")
    places_list = places.split(", ")
    while len(places_list) != 5:
        if len(places_list) > 5:
            easygui.msgbox(
                "Sorry but you can only enter the names of 5 places.\n"
                f"You entered {len(places_list)} places.",
                "Too many places")
            places = easygui.enterbox(
                "Enter the names of 5 places you would most "
                "like to visit\n"
                "Separate each place name with a comma and space",
                "Enter favourite places")
            places_list = places.split(", ")
        elif len(places_list) < 5:
            easygui.msgbox(
                "Sorry but you can only enter the names of 5 places.\n"
                f"You entered {len(places_list)} places.",
                "Not enough places")
            places = easygui.enterbox(
                "Enter the names of 5 places you would most "
                "like to visit\n"
                "Separate each place name with a comma and space",
                "Enter favourite places")
            places_list = places.split(", ")
    for place in places_list:
        bucket_list = "\n*    ".join(places_list)
    change = easygui.buttonbox(f"My bucket list: \n\n*    {bucket_list}",
                               "Travel bucket list",
                               ["Ok", "Edit"])
    while change != "Ok":
        place_to_change, new_place = easygui.enterbox(
            "Enter the name of the place you want "
            "to change followed by the name of the "
            "new place.\n\n"
            "Separate the two place names with a "
            "comma and space.", "Changes").split(", ")
        position = places_list.index(place_to_change)
        for place in range(len(place_to_change)):
            places_list.pop(position)
            places_list.insert(position, new_place)
        for place in places_list:
            while places_list.count(place) > 1 or place_to_change == new_place:
                places_list.pop(position)
                places_list.insert(position, place_to_change)
                easygui.msgbox(
                    "That place name was a duplicate. Please try again.",
                    "Duplicate")
                place_to_change, new_place = easygui.enterbox(
                    "Enter the name of the place you want "
                    "to change followed by the name of the "
                    "new place.\n\n"
                    "Separate the two place names with a "
                    "comma and space.", "Changes").split(", ")
                position = places_list.index(place_to_change)
                for place2 in range(len(place_to_change)):
                    places_list.pop(position)
                    places_list.insert(position, new_place)
        for place in places_list:
            bucket_list = "\n*    ".join(places_list)
        change = easygui.buttonbox(f"My bucket list: \n\n*    {bucket_list}",
                                   "Travel bucket list",
                                   ["Ok", "Edit"])


travel_bucket_list()
