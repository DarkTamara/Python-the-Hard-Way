def break_words (stuff):
    """this function wll break up the words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    return sorted(words)

def print_first_word(words):
    """prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """prints the last word after popping it off."""
    print word

def sort_sentence(sentence):
    """takes in a full sentance and returns the sorted words."""
    return sort_words(words)

def print_first_and_last (sentence):
    """prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(word)

def print_first_and_last_sorted(sentence):
    """sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
