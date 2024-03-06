import easygui


no_more = "Actually resurrect a spider please"
killed = 0
while no_more != "No":
    if no_more == "Actually resurrect a spider please":
        killed -= 1
    else:
        killed += 1
    no_more = easygui.buttonbox("Do you want to kill the spider?", "Kill",
                                ["KILL IT", "No",
                                 "Actually resurrect a spider please"])
if killed >= 0:
    easygui.msgbox(f"You killed {killed} spiders.", "death")
    if killed >= 15:
        easygui.msgbox("Wow you are good at killing spiders", "Good job")
    elif 0 < killed < 15:
        easygui.msgbox("Hmm are you killing the spiders on purpose or "
                       "by accident?",
                       "Suspicious")
    elif killed == 0:
        easygui.msgbox("Wow you are so peaceful", "Peace lover")
else:
    resurrected = killed * (-1)
    easygui.msgbox(f"You resurrected {resurrected} spiders.",
                   "resurrection")
    easygui.msgbox("YOU RESURRECTED THE SPIDERS?????", "impossible ")
    easygui.msgbox("STOP RESURRECTING THE SPIDERS", "WHY")
    easygui.msgbox("PLEASE STOP", "AHH")
    easygui.msgbox("HOW COULD YOU DO THIS", "bruh")
