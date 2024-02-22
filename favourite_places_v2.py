import easygui

name = easygui.enterbox("What is your name?", "Name")
pronoun = easygui.buttonbox("What is your preferred pronoun?",
                            "Pronoun", ["his", "her", "their"])
places = [easygui.enterbox("What is your most favourite place to visit?"),
          easygui.enterbox("What is your second favourite?"),
          easygui.enterbox("What is your third favourite?")]

print(f"The place {name} would most like to visit is {places[0]}")
print(f"{pronoun} second choice would be {places[1]}")
print(f"{pronoun} third choice would be {places[2]}")
