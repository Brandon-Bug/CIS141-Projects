# 1. Prompt the user for a word. Then, prompt the user for how many times they'd like that word repeated. Use the skills you learned in this module to print the word the correct number of times.

input_word = input("What word would you like to repeat?: ")
repeat_count = int(input("How many times would you like to repeat it?: "))
print(input_word*repeat_count)

#2. Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."

user_name = input("What is your name?: ")
user_age = int(input("How old are you "+user_name+"? "))

age_next_year = user_age + 1
final_message = "Hello, " + user_name + "! You are " + str(user_age) + " years old. Next year, you will be " + str(age_next_year) + " years old."
print(final_message)

#3. Prompt the user for a sentence and a word to try to find in that sentence. Have the program print out whether the word was found in the sentence. (i.e. True or False)

user_sentence = input("Write a sentance: ")
word_to_find = input("Give a word to find in that sentance: ")
print(word_to_find in user_sentence)

#4. Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen.

user_word = input("Write a word: ")
first_index = int(input("Enter the first index: "))
last_index = int(input("Enter the last index: "))
sliced_word = user_word[first_index:last_index]
print(sliced_word)

#5. Print 3 words with a | character (called a pipe) in between them. Use the appropriate keyword argument in print() to do so.

word_1 = "This"
word_2 = "is"
word_3 = "Olympic"

print(word_1,word_2,word_3,sep="|")
