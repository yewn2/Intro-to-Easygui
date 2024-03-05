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
    easygui.msgbox(f"My bucket list: \n\n*    {bucket_list}")


travel_bucket_list()
