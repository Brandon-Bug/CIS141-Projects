'''
#1. Write a function called count_vowels(input) that takes a string
    and returns the number of vowels (a, e, i, o, u) in it.
'''

def count_vowels(input_string):
    vowel_count = 0

    for letter in input_string:
        if letter in ["a","e","i","o","u"]:
            vowel_count += 1
    
    return vowel_count

print(count_vowels("This function will count vowels"))
print(count_vowels("While this string will have many more vowels"))

'''
#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
    (reads the same forward and backward, ignoring case). The function should returns
    either True or False.
'''

def is_palindrome(s):
    lower_s = s.lower()
    flipped_s = lower_s[::-1]
    
    return lower_s == flipped_s

print(is_palindrome("tacocat"))
print(is_palindrome("RaceCar"))
print(is_palindrome("Olympic College"))

'''
#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
    For example, water is very effective to fight fire.
    Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
    strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
    simple type effectiveness rules. Your solution only needs to work for these three sets of input:
    print(type_advantage("Water", "Fire"))  # "Super Effective"
    print(type_advantage("Fire", "Water"))  # "Not Very Effective"
    print(type_advantage("Electric", "Grass"))  # "Neutral"
'''

def type_advantage(attacker, defender):

    super_effective = "Super Effective"
    not_effective = "Not Very Effective"
    neutral = "Neutral"

    if attacker.lower() == "water" and defender.lower() == "fire":
        return super_effective
    
    elif attacker.lower() == "fire" and defender.lower() == "water":
        return not_effective
    
    else:
        return neutral

print(type_advantage("Water","Fire"))
print(type_advantage("Fire","Water"))
print(type_advantage("Electric","Grass"))



'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington State Ferry fare
    based on age and whether the person has a vehicle. Assume the following rates:
    * Adults (19-64): $10 without a vehicle, $20 with a vehicle.
    * Seniors (65+): $5 without a vehicle, $15 with a vehicle.
    * Children (0-18): Free.
'''

def ferry_fare(age, vehicle):

    if age >= 65: #Passenger is a senior

        return "Senior with vehicle: $15" if vehicle else "Senior without vehicle: $5"
    
    elif age >= 19: #Passenger is an adult

        return "Adult with vehicle: $20" if vehicle else "Adult without vehicle: $10"

    else: #Passenger is a child, rides free
        return "Child, passenger rides free"

print(ferry_fare(12,False))
print(ferry_fare(43,True))
print(ferry_fare(72,False))

'''
#5. Write a function called level_up(experience) that takes a player's experience points
    and returns their new level based on these rules:
    * 0-99 XP → Level 1
    * 100-199 XP → Level 2
    * 200+ XP → Level 3
'''

def level_up(experience):

    if experience >= 200:
        return "Level 3"
    elif experience >= 100:
        return "Level 2"
    else:
        return "Level 1"

print(level_up(20))
print(level_up(146))
print(level_up(300))
