def print_upper_words(words):
    """For a list of words, print out each word on a separate line, but in all uppercase.
    
    For Example: 
        print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])

        Should print:
            HELLO
            HEY
            GOODBYE
            YO
            YES
    """
    for word in words:
        print(word.upper())

def print_upper_words_e(words):
    """For a list of words, print out each word on a separate line, but only words that start with the letter 'e', and in all uppercase
    
    For Example:
        print_upper_words_e(["Edward", "Scissorhands", "elephant", "mouse", "eager", "beaver"])
        
        Should print:
            EDWARD
            ELEPHANT
            EAGER
    """
    for word in words:
        if word.lower().startswith("e"):
            print(word.upper())

def must_start_with(input):
    """Request for user to input desired starting letters of words to capitalize"""

    start_letter = input("Please choose your starting letters, separated by spaces.\n")
    return start_letter.split()

def print_upper_words_set_of_letters(words, letters):
    """For a list of words, print out each word on a separate line, but only words that start with input letters, and in all uppercase.
    
    For Example:
        print_upper_words_set_of_letters([["hello", "hey", "goodbye", "yo", "yes"], must_start_with=["h", "y"])"""
    
    for word in words:
        for letter in letters:
            if word.lower().startswith(letter):
                print(word.upper())



print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])

print_upper_words_e(["Edward", "Scissorhands", "elephant", "mouse", "eager", "beaver"])

print_upper_words_set_of_letters(["hello", "hey", "goodbye", "yo", "yes"], must_start_with(input))