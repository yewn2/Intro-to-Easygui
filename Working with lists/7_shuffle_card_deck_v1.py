import easygui
import random


def shuffle_card_deck():
    card_names = ["two", "three", "four", "five", "six", "seven", "eight",
                  "nine",
                  "ten", "jack", "queen", "king", "ace"]
    card_suits = ["clubs", "diamonds", "hearts", "spades"]
    shuffle_again = ""
    while shuffle_again != "No":
        deck = []
        for suit in card_suits:
            for card in card_names:
                deck.append([card.capitalize(), " of ", suit.capitalize()])
        random.shuffle(deck)
        draw = []
        for card in deck[0:7]:
            name = "".join(card)
            draw.append(name)
        show_cards = "\n*   ".join(draw)
        shuffle_again = easygui.buttonbox(
            f"Seven cards have been drawn.\n"
            f"You have drawn:\n*    {show_cards}\n"
            f"Do you want to play again?", "Random draw",
            ["Yes", "No"])


shuffle_card_deck()
