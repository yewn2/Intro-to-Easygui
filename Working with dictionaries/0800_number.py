import easygui


def letter_to_number(string):
    num_letters = {
        "A": "2", "B": "2", "C": "2",
        "D": "3", "E": "3", "F": "3",
        "G": "4", "H": "4", "I": "4",
        "J": "5", "K": "5", "L": "5",
        "M": "6", "N": "6", "O": "6",
        "P": "7", "Q": "7", "R": "7", "S": "7",
        "T": "8", "U": "8", "V": "8",
        "W": "9", "X": "9", "Y": "9", "Z": "9",
    }
    letter_list = list(string.upper())
    num_list = []

    for char in letter_list:
        num_list.append(num_letters[char])

    return "0800 " + "".join(num_list)


def word_to_phone():
    word = easygui.enterbox("Enter a word to convert to a phone number:",
                            "Word for conversion")
    phone_number = letter_to_number(word)
    easygui.msgbox("Your phone number is:\n\n"
                   f"{phone_number}", "Conversion complete")


word_to_phone()
