import easygui
import random

player = 0

for roll in range(2):
    player += 1
    playername = easygui.enterbox(f"Player {player} Enter Name")
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    easygui.msgbox(f"Player {player}: {playername}\n"
                   f"You rolled:\n\n{die1} and {die2}\n\n"
                   f"Total: {die1 + die2}", f"Player {player}")
