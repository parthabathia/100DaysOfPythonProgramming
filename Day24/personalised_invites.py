with open("../Day24/Input/Letters/starting_letter.txt", mode="r") as file:
    letter = file.read()

with open("../Day24/Input/Names/invited_names.txt", mode="r") as file:
    for name in file:
        name = name.strip()
        with open(f"../Day24/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as names:
            letter_new = letter.replace("[name]", name)
            names.write(letter_new)
