def main():
    positive_words = ['goood', 'gooood', 'gorgeous', 'gorgeously', 'grace', 'graceful', 'gracefully', 'gracious', 'graciously', 'graciousness', 'grand', 'grandeur', 'grateful', 'gratefully', 'gratification', 'gratified', 'gratifies', 'gratify', 'gratifying', 'gratifyingly', 'gratitude', 'great', 'greatest', 'greatness', 'grin', 'groundbreaking', 'guarantee', 'guidance', 'guiltless', 'gumption', 'gush', 'gusto', 'gutsy', 'hail', 'halcyon', 'hale', 'hallmark', 'hallmarks', 'hallowed', 'handier', 'handily', 'hands-down', 'handsome', 'handsomely', 'handy', 'happier', 'happily', 'happiness', 'happy', 'hard-working', 'hardier', 'hardy', 'harmless', 'harmonious', 'harmoniously', 'harmonize', 'harmony', 'headway', 'heal', 'healthful', 'healthy', 'hearten', 'heartening', 'heartfelt', 'heartily', 'heartwarming', 'heaven', 'heavenly', 'helped', 'helpful', 'helping', 'hero', 'heroic', 'heroically', 'heroine', 'heroize', 'heros', 'high-quality', 'high-spirited', 'hilarious', 'honoring', 'hooray', 'hopeful', 'hospitable', 'hot', 'hotcake', 'hotcakes', 'hottest', 'hug', 'humane', 'humble', 'humility', 'humor', 'humorous', 'humorously', 'certain', 'new', 'enjoy', 'enjoyable', 'enjoying', 'fast', 'fastly', 'fulfillment','interesting', 'interests', 'intimacy', 'intimate', 'intricate', 'intrigue', 'intriguing', 'intriguingly', 'intuitive', 'invaluable', 'invaluablely', 'inventive', 'invigorate', 'invigorating', 'invincibility', 'invincible', 'inviolable', 'inviolate', 'invulnerable', 'irreplaceable', 'irreproachable', 'irresistible', 'irresistibly', 'issue-free', 'joy','pleasure']
    negative_words =['2-faced', 'behind', 'difficult', 'difficulty', 'ugly', 'blah', 'smugly', 'blame', 'blameworthy', 'bland', 'blandish', 'blaspheme', 'blasphemous', 'blasphemy', 'blasted', 'blatant', 'blatantly', 'blather', 'bleak', 'bleakly', 'bleakness', 'bleed', 'bleeding', 'bleeds', 'blemish', 'blind', 'blinding', 'blindingly', 'blindside', 'blister', 'blistering', 'bloated', 'blockage', 'blockhead', 'bloodshed', 'bloodthirsty', 'bloody', 'blotchy', 'blow', 'blunder', 'blundering', 'blunders', 'blunt', 'blur', 'bluring', 'blurred', 'blurring', 'blurry', 'blurs', 'blurt', 'boastful', 'boggle', 'bogus', 'boil', 'boiling', 'boisterous', 'bomb', 'bombard', 'bombardment', 'bombastic', 'bondage', 'bonkers', 'bore', 'bored', 'boredom', 'bores', 'boring', 'botch', 'bother', 'bothered', 'bothering', 'bothers', 'bothersome', 'bowdlerize', 'boycott', 'braggart', 'bragger', 'brainless', 'brainwash', 'brash', 'brashly', 'brashness', 'brat', 'bravado', 'brazen', 'brazenly', 'brazenness', 'irrationalities', 'irrationality', 'irrationally', 'irrationals', 'irreconcilable', 'irrecoverable', 'irrecoverableness', 'irrecoverablenesses', 'irrecoverably', 'irredeemable', 'irredeemably', 'irreformable', 'irregular', 'irregularity', 'irrelevance', 'irrelevant', 'irreparable', 'irreplacible', 'irrepressible', 'irresolute', 'irresolvable', 'irresponsible', 'irresponsibly', 'irretating', 'irretrievable', 'irreversible', 'irritable', 'irritably', 'irritant', 'irritate', 'irritated', 'irritating', 'sorrow','pain']
    txt = ['The', 'concept', 'behind', 'gamification', 'is', 'not', 'new', 'but', 'certainly', 'the', 'advent', 'of', 'the', 'word', 'has', 'been', 'difficult', 'The', 'term', 'gamification', 'was', 'coined', 'in', '2002', 'by', 'British', 'consultant', 'Nick', 'Pelling', 'as', 'a', 'deliberately', 'ugly', 'word', 'to', 'describe', 'apply', 'gamelike', 'accelerated', 'user', 'interface', 'design', 'to', 'make', 'electronic', 'transactions', 'both', 'enjoyable', 'and', 'fast', 'This', 'element', 'of', 'gamification', 'can', 'be', 'considered', 'from', 'two', 'different', 'points', 'of', 'view', 'On', 'the', 'one', 'hand', 'we', 'have', 'the', 'non-game', 'context', 'which', 'refers', 'to', 'the', 'many', 'fields', 'where', 'gamification', 'can', 'be', 'applied', 'On', 'the', 'other', 'hand', 'the', 'context', 'refers', 'also', 'to', 'the', 'gaming', 'environment', 'where', 'the', 'player', 'is', 'immersed', 'and', 'can', 'fulfil', 'game', 'requirements', 'As', 'we', 'are', 'going', 'to', 'see', 'in', 'the', 'next', 'chapters', 'game', 'elements', 'design', 'and', 'context', 'represent', 'the', 'three', 'main', 'elements', 'characterizing', 'all', 'the', 'gamified', 'experiences']

    (a,b,c) = get_pos(txt, positive_words)
    (d,e,f) = get_neg(txt, negative_words)
    print("the count of positive words in the sentence:",a)
    print("the length of the sentence:",b)
    print("the positive_attitude_index:",c)
    print("the count of negative words in the sentence:",d)
    print("the negative_attitude_index:",f)
    print("the valence of this text is:",c-f)




def get_pos(txt, positive_words):
    length=len(txt) # to find the length of the cleaned sentence
    pos_count=0
    for i in positive_words:
        #if that word is in the snt_list
        if txt.count(i)>0: # or simply use if i in snt_list:
            print(i)# just to see if I'm getting the right word
            pos_count = pos_count + txt.count(i) # I want to get the count of word i and add it to pos_count
            
    pos_attitude = pos_count/length
    return pos_count,length,pos_attitude





def get_neg(txt, negative_words):

    length=len(txt) # to find the length of the cleaned sentence
    neg_count=0
    for i in negative_words:
        #if that word is in the snt_list
        if txt.count(i)>0: # or simply use if i in snt_list:
            print(i)# just to see if I'm getting the right word
            neg_count = neg_count + txt.count(i) # I want to get the count of word i and add it to neg_count
            
    neg_attitude = neg_count/length
    return neg_count,length,neg_attitude


main()

