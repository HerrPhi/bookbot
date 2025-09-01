from stats import get_num_words

#function get_book_text:
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
'''
#function that counts words, input is a text
def get_num_words(text):
    words = text.split()
    return len(words)
'''

def main():
    #print(get_book_text("books/frankenstein.txt"))
    number_of_words = get_num_words(get_book_text("books/frankenstein.txt"))
    print(f"{number_of_words} words found in the document")

main()