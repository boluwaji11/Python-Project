word = input('Enter mute: ')

special_characters = ['“' ,'”' , ',' , '.' , '-', '@', '!', '#', '$', '%', '^', '&', '*', '(', ')', '/', '?', '"']          # List of characters to be removed
for every_character in special_characters:
    word = word.replace(every_character, '')

word = word.lower()           # Converts block of strings to lowercase characters
word = word.split()           # Converts string to list

print(word)
