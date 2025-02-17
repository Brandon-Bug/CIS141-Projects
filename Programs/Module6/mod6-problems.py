#1. Given a list of numbers, write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.

nums_list = [3,5,7,9,2,1,5,8,34,12,6,1,7,9,3]
new_sum = 0

for number in nums_list:
    new_sum += number

print(f"The sum of the list is {new_sum}!")


#2. With a list of strings provided, write code that counts how many times the word "Olympic" appears in the list, and then print the count.

strings_list = ["This","is","an","assignment","for","Olympic","College","On","The","Olympic","Website"]
olympic_count = 0

for word in strings_list:
    
    if word.lower() == "olympic":
        olympic_count += 1

print(f"There are {olympic_count} instances of the word \"Olympic\"")

#3. Given a list of strings, write code to create a new list that includes only the strings longer than three characters. Print the resulting filtered list.

second_strings_list = ["This", "is", "another", "list", "of", "words", "that", "may", "contain", "some", "longer", "words"]
longer_word_list = []

for word in second_strings_list:

    if len(word) > 3:
        longer_word_list.append(word)

print(longer_word_list)

#4. For a list of integers, write code that counts how many numbers are positive and how many are negative, then print both counts.

int_list = [4,6,-3,1,2,-64,2,53,-3,5,-7,-4]
positive_nums = 0
negative_nums = 0

for number in int_list:
    if number > 0:
        positive_nums +=1
    else:
        negative_nums +=1

print(f"There are {positive_nums} positive numbers and {negative_nums} negative numbers!")


#5. For a list of integers, use a loop to build a new list where each element is the square of the corresponding element in the original list. Print the new list.

normal_int_list = [4,3,2,6,8,5]
squared_int_list = []

for number in normal_int_list:
    squared_int_list.append(number*number)

print(squared_int_list)
