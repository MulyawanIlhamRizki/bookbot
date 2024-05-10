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
    chars = {}

    # loop through the text
    for c in text:
        lowered = c.lower()
        # Check if there is text in dictionary chars
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

#I am still not familiar with STDIN, this is boot dev implementation
def get_book_text(path):
    with open(path) as f:
        return f.read()

main()