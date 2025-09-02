from stats import get_num_words
from stats import count_characters

#function get_book_text:
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    #print(get_book_text("books/frankenstein.txt"))
    number_of_words = get_num_words(get_book_text("books/frankenstein.txt"))
    print(f"{number_of_words} words found in the document")

    dictionary_of_characters = count_characters(get_book_text("books/frankenstein.txt"))
    print(dictionary_of_characters)

main()