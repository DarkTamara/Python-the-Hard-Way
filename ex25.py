def break_words (stuff):
    """this function wll break up the words for us"""
    words = stuff.split(' ') #splits the "stuff" argument i will give to him
    return words

def sort_words(words):
    return sorted(words) #sorts the things in the list

def print_first_word(words):
    """prints the first word after popping it off."""
    word = words.pop(0) # this one takes the element on the 0 possition and deletes it
    print word

def print_last_word(words):
    """prints the last word after popping it off."""
    word = words.pop(len(words)-1)
    print word

def sort_sentence(sentence):
    """takes in a full sentance and returns the sorted words."""
    return sort_words(words) #sorts stuff 

def print_first_and_last (sentence):
    """prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
