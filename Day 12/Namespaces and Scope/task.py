enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# Local scope
# def drink_potion():
#     potion_strength = 2
#     print(f"potion strength: {potion_strength}")

# drink_potion()
# print(potion_strenth) # Name error

# Global scope
player_health = 10

def drink_potion():
    potion_strength = 2
    print(f"potion strength: {potion_strength}")
    print(f"health: {player_health}")

drink_potion()