'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to it.
    Write a Python script that reads a file gardening_tips.txt and prints
    out each tip one by one.
'''

with open("gardening_tips.txt",'r') as gardening_tips:
    for line in gardening_tips:
        print(line, end="")

'''
#2. Write a Python program that allows users to log their hiking trips. The program should:
    - Use a while loop to repeatedly ask for a hike name and distance in miles
    - Save each entry to hiking_log.txt (each hike on a new line)
    - When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''

file = open("hiking_log.txt",'a')
while True:

    hike_name = input("Name of your hike?: ")
    if hike_name == "0":
        break

    distance = input("Distance of hike in miles?: ")
    if distance == "0":
        break

    file.write(f"{hike_name} \t {distance}\n")

file.close()

'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into it. Write a Python program that:
    - Reads the file
    - Requests 5 inputs from the user: 5 words the user would like to count the frequency of
    - Counts how many times each word appears
    - Creates a dictionary of the words and their counts
    - Print the dictionary to the console
'''

lyrics = []

# Read and lowercase lyrics for word searching
with open("song_lyrics.txt",'r') as song_lyrics:
    lyrics = song_lyrics.read().lower().split()

# getting words from the user while current_word is above 0
user_word_count = {}
current_word = 5

while current_word > 0: # Building the dictionary of words

    word_input = input(f"Please enter {current_word} word(s) that you would like to count, press enter after each word!: ")

    user_word_count[word_input.lower()] = 0

    current_word -= 1


for word in lyrics: # Searching for valid words

    clean_word = word.replace("?","").replace(",","") #Cleaning up some of the lyrics to ensure accurate word counts

    if clean_word in user_word_count:
        user_word_count[clean_word] += 1

print(user_word_count)


'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated by commas.
    Write a program that reads the poll.txt file
    Count how many votes "yea" or "nay" received and print the results.
'''

yea_votes = 0
nay_votes = 0

with open("poll.txt",'r') as poll_votes:
    votes = poll_votes.read().split(",")

    for vote in votes:
        if vote == "yea":
            yea_votes += 1
        elif vote == "nay":
            nay_votes += 1

print(f"There are {yea_votes} \"Yea\" votes and {nay_votes} \"Nay\" votes.")
