# This program performs sentiment analysis on a block of text.

def main():
    print('Welcome! This program computes Sentiment Analysis.')
    print('-----------------------------------------')
    positive_words = ['goood', 'gooood', 'gorgeous', 'gorgeously', 'grace', 'graceful', 'gracefully', 'gracious', 'graciously', 'graciousness', 'grand', 'grandeur', 'grateful', 'gratefully', 'gratification', 'gratified', 'gratifies', 'gratify', 'gratifying', 'gratifyingly', 'gratitude', 'great', 'greatest', 'greatness', 'grin', 'groundbreaking', 'guarantee', 'guidance', 'guiltless', 'gumption', 'gush', 'gusto', 'gutsy', 'hail', 'halcyon', 'hale', 'hallmark', 'hallmarks', 'hallowed', 'handier', 'handily', 'hands-down', 'handsome', 'handsomely', 'handy', 'happier', 'happily', 'happiness', 'happy', 'hard-working', 'hardier', 'hardy', 'harmless', 'harmonious', 'harmoniously', 'harmonize', 'harmony', 'headway', 'heal', 'healthful', 'healthy', 'hearten', 'heartening', 'heartfelt', 'heartily', 'heartwarming', 'heaven', 'heavenly', 'helped', 'helpful', 'helping', 'hero', 'heroic', 'heroically', 'heroine', 'heroize', 'heros', 'high-quality', 'high-spirited', 'hilarious', 'honoring', 'hooray', 'hopeful', 'hospitable', 'hot', 'hotcake', 'hotcakes', 'hottest', 'hug', 'humane', 'humble', 'humility', 'humor', 'humorous', 'humorously', 'certain', 'new', 'enjoy', 'enjoyable', 'enjoying', 'fast', 'fastly', 'fulfillment','interesting', 'interests', 'intimacy', 'intimate', 'intricate', 'intrigue', 'intriguing', 'intriguingly', 'intuitive', 'invaluable', 'invaluablely', 'inventive', 'invigorate', 'invigorating', 'invincibility', 'invincible', 'inviolable', 'inviolate', 'invulnerable', 'irreplaceable', 'irreproachable', 'irresistible', 'irresistibly', 'issue-free', 'joy','pleasure']

    negative_words = ['2-faced', 'behind', 'difficult', 'difficulty', 'ugly', 'blah', 'smugly', 'blame', 'blameworthy', 'bland', 'blandish', 'blaspheme', 'blasphemous', 'blasphemy', 'blasted', 'blatant', 'blatantly', 'blather', 'bleak', 'bleakly', 'bleakness', 'bleed', 'bleeding', 'bleeds', 'blemish', 'blind', 'blinding', 'blindingly', 'blindside', 'blister', 'blistering', 'bloated', 'blockage', 'blockhead', 'bloodshed', 'bloodthirsty', 'bloody', 'blotchy', 'blow', 'blunder', 'blundering', 'blunders', 'blunt', 'blur', 'bluring', 'blurred', 'blurring', 'blurry', 'blurs', 'blurt', 'boastful', 'boggle', 'bogus', 'boil', 'boiling', 'boisterous', 'bomb', 'bombard', 'bombardment', 'bombastic', 'bondage', 'bonkers', 'bore', 'bored', 'boredom', 'bores', 'boring', 'botch', 'bother', 'bothered', 'bothering', 'bothers', 'bothersome', 'bowdlerize', 'boycott', 'braggart', 'bragger', 'brainless', 'brainwash', 'brash', 'brashly', 'brashness', 'brat', 'bravado', 'brazen', 'brazenly', 'brazenness', 'irrationalities', 'irrationality', 'irrationally', 'irrationals', 'irreconcilable', 'irrecoverable', 'irrecoverableness', 'irrecoverablenesses', 'irrecoverably', 'irredeemable', 'irredeemably', 'irreformable', 'irregular', 'irregularity', 'irrelevance', 'irrelevant', 'irreparable', 'irreplacible', 'irrepressible', 'irresolute', 'irresolvable', 'irresponsible', 'irresponsibly', 'irretating', 'irretrievable', 'irreversible', 'irritable', 'irritably', 'irritant', 'irritate', 'irritated', 'irritating', 'sorrow','pain']

    text = input('Please enter the text you want to analyze: ')         # Get the text from the users

    special_characters = ['“' ,'”' , ',' , '.' , '-', '@', '!', '#', '$', '%', '^', '&', '*', '(', ')', '/', '?', '"']          # List of characters to be removed
    
    for every_character in special_characters:
        text = text.replace(every_character, '')
    
    text = text.lower()           # Converts block of strings to lowercase characters
    text = text.split()           # Converts string to list

    positive_output = get_pos(text, positive_words)     # Call the get_pos function to run the positive attitude analysis
    negative_output = get_neg(text, negative_words)     # Call the get_pos function to run the negative attitude analysis
    
    valence = positive_output[2] - negative_output[2]       #  positive attitude index subtracted from the negative attitude index
    
    # Display the results
    print('\nThe following are the output of the Sentiment Analysis:')
    print()
    print('The length of words in your main text is:')
    print(positive_output[1], 'words.')           # total text length converted from tuple
    print()
    print('The Positive and Negative Attitude Index is calculated as:')
    print('Positive or Negative words in a text / the length of words in the text.')
    print()
    print('\tThe Positive Attitude Index:', format(positive_output[2], '.3f'))      # Displays the positive attitude index
    print('\tThe positive word(s):', positive_output[3])                # Displays the positive words
    print()
    print('\tThe Negative Attitude Index:', format(negative_output[2], '.3f'))      # Displays the negative attitude index
    print('\tThe negative word(s):', negative_output[3])            # Displays the negative words
    print()
    print('The total count for:')
    print('\tPositive words:', positive_output[0])
    print('\tNegative words:', negative_output[0])
    print()
    print('Valence is the polarity of a piece of text, whether it is "Positive", "Negative", or "Neutral".')
    print('It is calculated as: (Positive-Attitude-Index) minus (Negative-Attitude-Index)')
    print('\tValence:', format(valence, '.3f'))         # Displays the Valence
    print('Thanks for using the program.')


 # ----------- Define the get_pos function

def get_pos(text, positive_words):

    pos_words = []
    pos_count = 0
    

    for each_word in text:
        for each_pos_word in positive_words:
            if each_word == each_pos_word:
                pos_count += 1
                pos_words.append(each_pos_word)
                
    length = len(text)
    
    pos_attitude = pos_count / length
        
    return pos_count, length, pos_attitude, pos_words          # Outputs as a tuple

 # ----------- Define the get_neg function

def get_neg(text, negative_words):
    
    neg_words = []
    neg_count = 0
   
    for each_word in text:
        for each_neg_word in negative_words:
            if each_word == each_neg_word:
                neg_count += 1
                neg_words.append(each_neg_word)
                    
    length = len(text)
    
    neg_attitude = neg_count / length
    
    return neg_count, length, neg_attitude, neg_words      # Outputs as a tuple

# Call the main function
main()
