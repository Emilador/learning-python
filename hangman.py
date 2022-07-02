import random
import string
with open("words.txt", "r") as f:
    words = f.readlines()

clean_words = []
for w in words:
    clean_words.append(w.strip().upper())

def get_valid_word(clean_words):
    word = random.choice(clean_words)
    return word

def hangman():
    word = get_valid_word(clean_words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        print("You have used these letters: ", "".join(used_letters))
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word is: ", "".join(word_list))
        user_letter=input("Please guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif (user_letter in used_letters):
            print("You have used this letter before. Please do it again ")
        else:
            print("Thats a invalid character. Please do it again: ")




hangman()



