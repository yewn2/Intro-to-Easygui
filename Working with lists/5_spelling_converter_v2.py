import easygui


def nz_to_us():
    another_word = ""
    while another_word != "No":
        us_remove = ""
        us_insert = ""
        word = easygui.enterbox("Enter your NZ English Word",
                                "NZ English")
        if "our" in word:
            us_remove = "u"
        elif "ise" in word:
            us_remove = "s"
            us_insert = "z"
        elif "yse" in word:
            us_remove = "s"
            us_insert = "z"
        word_list = list(word)
        if us_remove != "":
            if us_remove == "u":
                position = (word.find(us_remove))
                for letter in range(len(us_remove)):
                    word_list.pop(position)
            else:
                position = (word.find(us_remove))
                for letter in range(len(us_remove)):
                    word_list.pop(position)
                    word_list.insert(position, us_insert)
            word_list = ''.join(word_list)
            easygui.msgbox(f"Your word converted to US English spelling is: "
                           f"{word_list}", "US English", "Exit")
        else:
            easygui.msgbox("No change in spelling",
                           "Nothing to change")
        another_word = easygui.buttonbox("Would you like to enter another "
                                         "word?", "Another one?",
                                         ["Yes", "No"])


nz_to_us()
