import easygui


def login_number():
    logins = {
        "w1nd0w": "cross5",
        "gUeSt": "12345",
        "superhero": "hero1",
        "new_login": "password"
    }

    username = easygui.enterbox("Enter your username: ", "User")

    while username not in logins:
        easygui.msgbox("Incorrect username, please try again.")
        username = easygui.enterbox("Enter your username: ", "User")

    password = easygui.passwordbox(f"Enter the password for user {username}:",
                                   "Password")

    if password == logins[username]:
        easygui.msgbox(f"Welcome {username}", "Correct password")
    else:
        easygui.msgbox("Sorry, wrong password", "Incorrect password")


login_number()
