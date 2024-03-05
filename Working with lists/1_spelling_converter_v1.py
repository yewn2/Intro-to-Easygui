import easygui


def nz_to_us():
    us_remove = "u"
    word = easygui.enterbox("Enter your NZ English Word", "NZ English")
    word_list = list(word)
    position = (word.find(us_remove))
    for letter in range(len(us_remove)):
        word_list.pop(position)
    word_list = ''.join(word_list)
    easygui.msgbox(f"Your word converted to US English spelling is: "
                   f"{word_list}", "US English", "Exit")


nz_to_us()
