#1. Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. Print the final sum.

user_limit = int(input("Calculate the sum up until which number?: "))
count = 1
sum = 0

while count <= user_limit:
    sum+=count
    count+=1
print(sum)

#2. Define a string variable (e.g., my_string = "Olympic College"). Use a for loop to print each character on its own line. Convert each character to uppercase before printing.

my_string = "This is a string for CIS141!"
for char in range(len(my_string)):
    print(my_string.upper()[char])

#3. Use a for loop and the range() function to print all even numbers from 2 to 20.

for i in range(2,21,2):
    print(i)

#4. Use nested for loops to create a simple multiplication table for numbers 1 through 5. Format your output so that each row corresponds to multiplying by a specific number. Example output:

# 1   2   3   4   5
# 2   4   6   8   10
# 3   6   9   12  15
# 4   8   12  16  20
# 5   10  15  20  25


for i in range(1,6):
    for j in range(1,6):
        print(f"{i * j:3}", end=" ") #Used some formatting from previous lessons to correct the exact alignment, otherwise it is visually messy
        #print(i*j, end=" ") #Unformatted

    print("")


#5. Write a program that continuously asks the user to input a number. If the user enters 0, immediately stop asking for more numbers. Otherwise, print the number they entered. Sample interaction:

"""
Enter a number (0 to stop): 4
You entered 4
Enter a number (0 to stop): 7
You entered 7
Enter a number (0 to stop): 0
Exiting...
"""

while True:
    user_number = int(input("Please enter a number (Enter 0 to exit program): "))
    
    if user_number == 0:
        print("User entered 0, exiting program.")
        break

    print("You entered",user_number)
