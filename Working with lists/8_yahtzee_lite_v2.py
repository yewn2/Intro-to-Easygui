import easygui
import random


def roll(player):
    score = 0
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
            roll_again = easygui.buttonbox(f"{player} roll {rolls}: "
                                           f"\n{dices}\n\n"
                                           f"Choose:", "Roll",
                                           ["Roll again", "Stick"])
        else:
            roll_again = "Stick"
            easygui.msgbox(f"{player} roll {rolls}: \n{dices}\n\n",
                           "Roll", "Stick")
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
                       f"Yahtzee!\nScore: 50", "Result")
        score = 50
    elif amount == 4:
        easygui.msgbox(f"{dices}\n\n"
                       f"Four of a kind!\nScore: 30", "Result")
        score = 30
    elif amount == 3:
        easygui.msgbox(f"{dices}\n\n"
                       f"Three of a kind!\nScore: 10", "Result")
        score = 10
    else:
        easygui.msgbox(f"{dices}\n\n"
                       f"Better luck next time\nScore: 0", "Result")
        score = 0
    return score


def yahtzee_lite_2():
    play_again = ""
    while play_again != "No":
        player_1 = easygui.enterbox("Enter the name of player 1:",
                                    "Player 1")
        player_2 = easygui.enterbox("Enter the name of player 2:",
                                    "Player 2")
        score1 = roll(player_1)
        score2 = roll(player_2)
        if score1 > score2:
            play_again = easygui.buttonbox(
                f"The winner is {player_1} with a score of "
                f"{score1}\n"
                f"{player_2} scored {score2}\n"
                f"Do you want to play another round?", "Result",
                ["Yes", "No"])
        elif score2 > score1:
            play_again = easygui.buttonbox(
                f"The winner is {player_2} with a score of "
                f"{score2}\n"
                f"{player_1} scored {score1}\n"
                f"Do you want to play another round?", "Result",
                ["Yes", "No"])
        else:
            play_again = easygui.buttonbox(
                f"This is a draw!\n"
                f"{player_1} scored {score1} and "
                f"{player_2} also scored {score2}\n\n"
                f"Do you want to play another round?", "Result",
                ["Yes", "No"])
    easygui.msgbox("Thanks for playing Yahtzee! Lite for 2 players",
                   "Goodbye", "Exit")


yahtzee_lite_2()
