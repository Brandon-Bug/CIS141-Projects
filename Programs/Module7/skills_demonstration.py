# Mod 7 Skills Demo Starter Code

def generate_stats(name,cls,level,health):
    return f"{name} - Class: {cls}, Level: {level}, Health: {health}"

# Generate stats for Warrior
formatted_stats = generate_stats("Thorin", "Warrior", 10, 150)
print(formatted_stats)

# Generate stats for Mage
formatted_stats = generate_stats("Merlin", "Mage", 12, 120)
print(formatted_stats)

# Generate stats for Rogue
formatted_stats = generate_stats("Ezio", "Ezio", 8, 100)
print(formatted_stats)
