import random
from HangmanWords import word_list
from HangmanArt import stages, logo

print(logo)
lives = len(stages)
chosen_word = random.choice(word_list)
print(chosen_word)
guessed_letter = []
display = []
for _ in chosen_word:
    display += "_"

#print(list(chosen_word))
#print(display)
while display != list(chosen_word) and lives != 0:
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letter:
        print("You have already guessed this letter.")
        continue
    else:
        guessed_letter += guess

    for position in range(len(chosen_word)):
        if guess == chosen_word[position]:
            display[position] = guess
    
    print(f"{' '.join(display)}\n")

    if guess not in chosen_word:
        print(f"You guessed the letter {guess}. That is not present in the word. You lose a life.")
        print(stages[lives-1])
        lives -= 1
        if lives == 0:
            print("You lose.")

    if display == list(chosen_word):
        print("You win!")

    