#function that counts words, input is a text
def get_num_words(text):
    words = text.split()
    return len(words)