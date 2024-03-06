import easygui
import random


def winning_card():
    play_again = ""
    while play_again != "Exit":
        card_names = ["two", "three", "four", "five", "six", "seven", "eight",
                      "nine",
                      "ten", "jack", "queen", "king", "ace"]
        card_suits = ["clubs", "diamonds", "hearts", "spades"]
        player_name = easygui.enterbox("Enter Player Name: ", "Player Name")
        player_card = [random.choice(card_names), random.choice(card_suits)]
        computer_card = [random.choice(card_names), random.choice(card_suits)]
        if card_names.index(player_card[0]) > card_names.index(computer_card[0]):
            easygui.msgbox(f"{player_name}, your card was the {player_card[0]} "
                           f"of {player_card[1]}\n"
                           f"The computer's card was the {computer_card[0]} of "
                           f"{computer_card[1]}\n"
                           f"{player_name}, your card was higher. You won.",
                           f"{player_name} wins")
        else:
            easygui.msgbox(f"{player_name}, your card was the {player_card[0]} "
                           f"of {player_card[1]}\n"
                           f"The computer's card was the {computer_card[0]} of "
                           f"{computer_card[1]}\n"
                           f"{player_name}, your card was lower. You lost.",
                           f"{player_name} loses")
        play_again = easygui.buttonbox("Would you like to play again or exit?",
                                       "Play again?",
                                       ["Play again", "Exit"])


winning_card()
