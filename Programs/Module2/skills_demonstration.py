# Write a small Python program that asks the user for their name, the total bill amount at a restaurant, and the number of people splitting the bill. 
# The program will then calculate how much each person should pay and display the result with a friendly message.

user_name = input("What is your name? ")
total_bill = float(input("How much was the bill? $"))
num_of_people = int(input("How many people are splitting the bill? "))

split_value = total_bill/num_of_people

print(f"Hello {user_name}! You will need to have everyone pay ${split_value:.2f} to cover the bill completely.")