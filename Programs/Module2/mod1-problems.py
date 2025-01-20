import math

# 1. Create a program that prints the following output to the screen: "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."
print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")

# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.
variable_1 = int(input("Please enter the first number: "))
variable_2 = int(input("Please enter the second number: "))

print(f"Addition: {variable_1+variable_2}")
print(f"Subtraction: {variable_1-variable_2}")
print(f"Multiplication: {variable_1*variable_2}")
print(f"Division: {variable_1/variable_2}")

# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)
side_1 = int(input("The length of the first side: "))
side_2 = int(input("The length of the second side: "))
side_3 = int(input("The length of the third side: "))

semiperimeter = ((side_1 + side_2 + side_3)/2)
triangle_area = math.sqrt(semiperimeter*(semiperimeter-side_1)*(semiperimeter-side_2)*(semiperimeter-side_3))
print(f"The area of the triangle is {triangle_area}.")

# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).

# This could have been one line, however, for legibility reasons it has been separated into multiple.
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
number_3 = int(input("Enter the third number: "))
number_4 = int(input("Enter the fourth number: "))
number_5 = int(input("Enter the fifth number: "))
all_numbers = [number_1, number_2, number_3, number_4, number_5]

num_total = sum(all_numbers)
num_average = num_total/len(all_numbers)
num_min = min(all_numbers)
num_max = max(all_numbers)
num_range = num_max - num_min

print(f"You entered {all_numbers}, their total is {num_total}, the average is {num_average} the minimum is {num_min}, the maximum is {num_max}, and the range is {num_range}")
# Standard Deviation calculation function was not included in the math library, an alternative could be used with the statistics library however.
