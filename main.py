def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)
    
    print(word_count)
    print(letter_count)

def get_word_count(text):
    
    words = text.split()
    #my implementation is to use FOR loop to count number of words
    #however it is not recommended as we can use len() built-in function to count the lenght of the list of words
    
    #my implementation
    #i = 0
    #for word in words:
    #    i += 1
    #return (i)

    #boot.dev implementation
    return len(words)

def get_letter_count(text):
    this_text = text
    lowered_string = this_text.lower()

    #problem:
    #count the letters that shows up in the lowered string
    #first is to create a list of alphabets
    #then count each word that appear in the lowered strings for each alphabets

    counter = 0
    alph = "abcdefghijklmnopqrstuvwxyz"
    this_character = list(alph)
    this_character_dict = {}

    for i in range (0, 26):
        this_character_dict[this_character[i]] = 0
        i += 1
    
    #using dictionary to count the number of words that appear in frankenstein text
    

    return this_character

#I am still not familiar with STDIN, this is boot dev implementation
def get_book_text(path):
    with open(path) as f:
        return f.read()

main()