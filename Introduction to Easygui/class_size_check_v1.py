import easygui

again = "Yes"

while again == "Yes":
    school = easygui.enterbox("Enter the name of the school", "School name")
    size = easygui.integerbox("What is the maximum number of children allowed "
                              "per class?\n"
                              "Must be a number between 10 and 30",
                              "Maximum class size",
                              10, 10, 30)
    students = easygui.integerbox(f"What is the total number of children at "
                                  f"{school}?\n"
                                  f"Must be a number between 10 and 1400",
                                  "Total roll of school",
                                  10, 10, 1400)
    teachers = easygui.integerbox(f"How many teachers are there at {school}?\n"
                                  f"Must be a number between 1 and 120",
                                  "Total teachers",
                                  1, 1, 120)

    req_teachers = students // size
    if students % req_teachers > 0:
        req_teachers += 1

    if req_teachers > teachers:
        amt = req_teachers - teachers
        easygui.msgbox("You don't have enough teachers.\n\n"
                       f"You need {amt} more teachers.", "Under-staffed")
    elif req_teachers < teachers:
        amt = teachers - req_teachers
        easygui.msgbox("You have too many teachers.\n\n"
                       f"You could do without {amt} current teacher/s.",
                       "Under-staffed")
    else:
        easygui.msgbox("You have the right amount of teachers.",
                       "Perfectly staffed")

    again = easygui.buttonbox("Do you want to perform another calculation?",
                              "More ratios?", ["Yes", "No"])

easygui.msgbox("Goodbye", "Thanks for using this calculator")
