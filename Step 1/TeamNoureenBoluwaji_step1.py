# This program compares a set of words against other specific words

# Start
# Define the mainline logic (main) function
# Create local constant variables within the main function
# Call the counting function within the main function
# Define the counting function
    # Pass the local constant variables into the counting function
    # Check the list of words against the sentiment list
    # Calculate the total count
# Call the main function
# End

#===============================================================================

# Define the header of the program
print('Welcome! This program compares different words')
print('----------------------------------------------')
print()

# Define the main function
def main():
    # Declare the local constant variables
    word1 = 'This'
    word2 = 'is'
    word3 = 'a'
    word4 = 'beautiful'
    word5 = 'and'
    word6 = 'sunny'
    word7 = 'day'
    # Declare the sentiments list
    sentiment1 = 'Beautiful'
    sentiment2 = 'beautiful'
    sentiment3 = 'sunny'
    # Call the counting function
    counting(word1, word2, word3, word4, word5, word6, word7, sentiment1, sentiment2, sentiment3)           

# Define the counting function
def counting(word1, word2, word3, word4, word5, word6, word7, sentiment1, sentiment2, sentiment3):
    total_count = 0
    for words_list in [word1, word2, word3, word4, word5, word6, word7]: # For loop analyzing words
        for sentiments_list in [sentiment1, sentiment2, sentiment3]: # For loop analyzing sentiments           
            if words_list == sentiments_list:
                total_count +=1         # The running total
          
    # Display the result
    print('Comparing the words against the sentiments list......')
    print()
    print('The number of words that also appeared on the sentiment lists were:')
    print(total_count, 'word(s)')
    print()
    print('Thank You!')

# Call the main function to execute               
main()
