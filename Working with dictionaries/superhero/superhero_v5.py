hero_0 = {
    "name": "Materdon",
    "power": "flight",
    "strength": "5"
}

print(hero_0)

hero_0["speed"] = 12
print(hero_0)

hero_0["strength"] = 6
print(hero_0)

popped_item = hero_0.pop("power")
print(hero_0)
print(popped_item)

print("Superhero 1 stats\n")
for i in hero_0:
    print(f"{i}: {hero_0[i]}")
