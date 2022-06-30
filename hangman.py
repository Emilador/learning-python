import random
import string
with open("words.txt", "r") as f:
    words = f.readlines()

clean_words = []
for w in words:
    clean_words.append(w.strip().upper())

def get_valid_word(clean_words):
    word=random.choice(clean_words)
    while ("-"in word or " "in word):
        word=random.choice(clean_words)

        return word.upper()

def hangman():
    word=get_valid_word(clean_words)
    word_letters=set(word)
    alphabet=set(string.ascii_uppercase)
    usedletters=set()







