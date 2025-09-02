from stats import get_num_words
from stats import count_characters
from stats import sort_dictionary_into_list

#function get_book_text:
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    #print(get_book_text("books/frankenstein.txt"))

    number_of_words = get_num_words(get_book_text("books/frankenstein.txt"))
    #print(f"{number_of_words} words found in the document")

    dictionary_of_characters = count_characters(get_book_text("books/frankenstein.txt"))
    #print(dictionary_of_characters)

    sorted_list_of_dictionarys = sort_dictionary_into_list(dictionary_of_characters)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for dictionary in sorted_list_of_dictionarys:
        if dictionary["char"].isalpha():
            print(f"{dictionary["char"]}: {dictionary["num"]}")
    print("============= END ===============")


main()