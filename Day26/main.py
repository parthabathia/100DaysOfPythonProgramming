import pandas as pd


def generate_phonetic():
    user_word = input("Enter a word: ").upper()
    try:
        nato_phonetic_for_user_word = [alphabet_dict[letter] for letter in user_word]
    except KeyError:
        print("Kindly use only letters.")
    else:
        print(nato_phonetic_for_user_word)


data = pd.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for index, row in data.iterrows()}
generate_phonetic()
