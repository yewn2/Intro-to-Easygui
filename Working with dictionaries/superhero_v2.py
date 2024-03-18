hero_0 = {
    "name": "Materdon",
    "power": "flight",
    "strength": "5"
}

print(hero_0["strength"])

if "name" in hero_0:
    print(f"The superhero's name is {hero_0['name']}")
else:
    print("There is no superhero name.")

if "speed" in hero_0:
    print(f"The superhero's speed is {hero_0['speed']}")
else:
    print("There is no superhero speed.")

if "Materdon" in hero_0["name"]:
    print("That is the superhero's name.")
else:
    print("That isn't the superhero's name.")

if "Smerlyx" in hero_0["name"]:
    print("That is the superhero's name.")
else:
    print("That isn't the superhero's name.")
