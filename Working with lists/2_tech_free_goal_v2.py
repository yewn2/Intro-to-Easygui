import easygui


def tech_free_goal():
    goal = easygui.buttonbox("Select the amount of tech-free days you wish "
                             "to set as your goal.", "Goal amount",
                             [1, 2, 3, 4, 5, 6, 7])
    days = easygui.enterbox("Please enter each of the days on which you used "
                            "technology\n"
                            "Separate each day with a space",
                            "Days tech was used")
    days_list = days.split()
    days_amt = 7 - len(days_list)
    if days_amt < goal:
        easygui.msgbox(f"Too bad! You had {7 - days_amt} tech-using days.\n"
                       f"That is {(7 - days_amt) - goal} more than your goal.",
                       "Goal not achieved")
    else:
        easygui.msgbox(f"Congratulations! You had {days_amt} tech-free days.\n"
                       f"You met your goal of at least 3 tech-free days.",
                       "Goal achieved")


tech_free_goal()
