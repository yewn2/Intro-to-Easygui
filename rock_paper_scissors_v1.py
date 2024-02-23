import easygui
import random

welcome = easygui.buttonbox("Welcome to Rock Paper Scissors\n"
                            "Rock beats Scissors\n"
                            "Paper beats Rock\n"
                            "Scissors beats Paper\n\n"
                            "Do you want to play?", "Welcome and Rules",
                            ["Yes", "No"])
while welcome == "Yes":
    weapons = ["Rock", "Paper", "Scissors"]
    playername = easygui.enterbox("Enter your name", "Name")
    my_choice = easygui.buttonbox("Choose your weapon", "Weapon choice",
                               [weapons[0], weapons[1], weapons[2]])
    pc_choice = random.choice(weapons)
    choice = easygui.msgbox(f"{playername} chose {my_choice} and the computer "
                            f"chose {pc_choice}")
    if pc_choice == my_choice:
        easygui.msgbox("This was a draw")
    elif pc_choice == weapons[0] and my_choice == weapons[1]:
        easygui.msgbox("You win")
    elif pc_choice == weapons[1] and my_choice == weapons[2]:
        easygui.msgbox("You win")
    elif pc_choice == weapons[2] and my_choice == weapons[0]:
        easygui.msgbox("You win")
    elif pc_choice == weapons[0] and my_choice == weapons[2]:
        easygui.msgbox("Computer wins")
    elif pc_choice == weapons[1] and my_choice == weapons[0]:
        easygui.msgbox("Computer wins")
    elif pc_choice == weapons[2] and my_choice == weapons[1]:
        easygui.msgbox("Computer wins")

    welcome = easygui.buttonbox("Welcome to Rock Paper Scissors\n"
                                "Rock beats Scissors\n"
                                "Paper beats Rock\n"
                                "Scissors beats Paper\n\n"
                                "Do you want to play?", "Welcome and Rules",
                                ["Yes", "No"])
