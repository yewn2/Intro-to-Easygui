import easygui
import random


def yahtzee_lite():
    play_again = ""
    while play_again != "No":
        rolls = 0
        values = ["1", "2", "3", "4", "5", "6"]
        roll_again = ""
        dice_list = []
        dices = ""
        while rolls != 3 and roll_again != "Stick":
            dice_list = []
            rolls += 1
            for dice in range(0, 5):
                dice_list.append(random.choice(values))
            dices = " ".join(dice_list)
            if rolls != 3:
                roll_again = easygui.buttonbox(f"You rolled: {dices}\n\n"
                                               f"Choose:", "Roll",
                                               ["Roll again", "Stick"])
            else:
                easygui.msgbox(f"You rolled: {dices}")
                roll_again = "Stick"
        amount = 0
        for number in dice_list:
            if dice_list.count(number) == 5:
                amount = 5
            elif dice_list.count(number) == 4:
                amount = 4
            elif dice_list.count(number) == 3:
                amount = 3
        if amount == 5:
            easygui.msgbox(f"{dices}\n\n"
                           f"Yahtzee!", "Result")
        elif amount == 4:
            easygui.msgbox(f"{dices}\n\n"
                           f"Four of a kind!", "Result")
        elif amount == 3:
            easygui.msgbox(f"{dices}\n\n"
                           f"Three of a kind!", "Result")
        else:
            easygui.msgbox(f"{dices}\n\n"
                           f"Better luck next time", "Result")
        play_again = easygui.buttonbox(
            "You've had three turns. Do you want to "
            "play another round?", "Goodbye",
            ["Yes", "No"])


yahtzee_lite()
