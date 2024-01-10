import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for index, row in data.iterrows()}

user_word = input("Enter a word: ")

user_word_as_list = [letter.upper() for letter in user_word]

nato_word_for_user_word = [alphabet_dict[letter] for letter in user_word_as_list]

print(nato_word_for_user_word)
