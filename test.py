import easygui
import random

number = random.randint(0, 5)
print(number)

words = ["cat", "bat", "mat", "hat"]
my_word = random.choice(words)
print(my_word)

friend = "Stephanie"
letter = random.choice(friend)
print(letter)

print(friend[3])

name = easygui.enterbox("Hi, what's your name?", "Name")
print(name)

age = easygui.integerbox("How old are you?")
print(age)

carry_on = easygui.buttonbox("Do you want to continue?",
                             choices=["Yes", "No", "Don't care"],
                             title="Continue")

welcome = easygui.msgbox("Welcome to Easygui", title="Welcome")

gender = easygui.buttonbox("Choose gender", "Gender",
                           ["man", "woman", "other"])
print(gender)
