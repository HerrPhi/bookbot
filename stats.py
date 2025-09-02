#function that counts words, input is a text
def get_num_words(text):
    words = text.split()
    return len(words)

#function that counts how often each character appears
def count_characters(text):
    text_in_lowercase = text.lower()
    words = text_in_lowercase.split()
    #empty dictionary for all characters:
    characters = dict()
    for word in words:
        letters = list(word)    #turns single word into a list of its letters
        for letter in letters:      #iterate over all letters in a word
            if letter in characters:
                new_value = characters[letter] + 1
                characters[letter] = new_value  #accesses the dictionary with letter as the key and updates the corresponding value
            else:
                characters[letter] = 1  #adds the character to the dictionary
    return characters   #returns the dictionary with the characters and their counts

#returns sorted list of dictionarys
def sort_dictionary_into_list(dictionary):
    sorted_list_of_dictionarys = list()

    for char in dictionary:
        new_dict = dict()
        num = dictionary[char]
        new_dict = {"char" : char, "num" : dictionary[char]}
        sorted_list_of_dictionarys.append(new_dict)

    
    sorted_list_of_dictionarys.sort(reverse=True,key=sort_on)
    #print(sorted_list_of_dictionarys)

    return sorted_list_of_dictionarys

def sort_on(dict):
    return dict["num"]