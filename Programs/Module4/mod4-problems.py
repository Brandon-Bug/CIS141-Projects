#1. Construct a truth table for the expression: (A AND B) OR (NOT B) where A and B each can be True or False. Your truth table should be commented out (as it's not valid Python code!)

#  4 Rows (2x2)
#  
#  A   B   (A AND B)   (NOT B)     (A AND B) OR (NOT B)
#  ----------------------------------------------------
#  T   T       T         F            T
#  T   F       F         T            T
#  F   T       F         F            F
#  F   F       F         T            T


#2. The headlights of a car should only automatically turn on when the daylight outside is below a certain threshold. If a sensor threshold is below the number 8, print "Headlights On"; otherwise, print "Headlights Off".
daylight = 4

if daylight < 8:
    print("Headlights On")
else:
    print("Headlights Off")

#3. Prompt the user for their bank balance. Evaluate whether the balance is less than $100. Print True if the user’s balance is below $100; print False, otherwise.

user_balance = float(input("What is your current bank balance? $"))

if user_balance < 100:
    print(True)
else:
    print(False)


#4. A theater wants to enforce age restrictions for movie tickets. Ask the user for their age, and tell them whether they can see G (appropriate for under 13), PG-13 (appropriate for 13 to 17), or R (appropriate for over 18) rated movies.

user_age = int(input("How old are you?: "))

if user_age >= 18:
    print("You may see an R rated film.")
elif user_age >= 13:
    print("You are limited to seeing PG-13 rated movies.")
else:
    print("You are only allowed to see G rated movies.")

#5. A store charges $5 for shipping on any order under $50. If the order amount is $50 or more, shipping is free. Ask the user for the order total and print the total cost, including shipping.

order_total = float(input("How much was your order?: $"))

if order_total < 50:
    order_total += 5

print(f"Your total order cost (including shipping) will be ${order_total:.2f}!")
