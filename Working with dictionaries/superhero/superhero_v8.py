heroes = {}

for i in range(2):
    hero_ID = input("\n\nEnter ID: ")
    heroes[hero_ID] = {}

    name = input("Enter name: ")
    heroes[hero_ID]['name'] = name

    power = input("Enter power: ")
    heroes[hero_ID]['power'] = power

    strength = input("Enter strength: ")
    heroes[hero_ID]['strength'] = strength

    speed = input("Enter speed: ")
    heroes[hero_ID]['speed'] = speed

print(f"\n\n{heroes}")
