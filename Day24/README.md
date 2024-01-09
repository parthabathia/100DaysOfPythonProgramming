# Day 24 of Python programming bootcamp

The provided code is a Python script designed to customize and generate personalized invitation letters based on a template. Here's a description of the code:

1. The script begins by opening a file named "starting_letter.txt" located at "../Day24/Input/Letters/" in read-only mode. It reads the contents of this file and stores them in the variable `letter`.

```python
with open("../Day24/Input/Letters/starting_letter.txt", mode="r") as file:
    letter = file.read()
```

2. Next, the script opens another file named "invited_names.txt" located at "../Day24/Input/Names/" in read-only mode. It then iterates over each line in this file, removing any leading or trailing whitespaces using the `strip()` method, and assigns the cleaned name to the variable `name`.

```python
with open("../Day24/Input/Names/invited_names.txt", mode="r") as file:
    for name in file:
        name = name.strip()
```

3. Inside the loop, the script opens a new file for writing, named dynamically as "letter_for_{name}.txt" in the directory "../Day24/Output/ReadyToSend/". This file will contain a personalized invitation letter for each individual.

```python
        with open(f"../Day24/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as names:
```

4. Within this inner loop, the script replaces the placeholder "[name]" in the original letter template with the current name, creating a personalized letter for each invitee. The modified letter is then written to the newly created file.

```python
            letter_new = letter.replace("[name]", name)
            names.write(letter_new)
```

In summary, this script takes a template letter from "starting_letter.txt" and customizes it for each invited name from "invited_names.txt". It creates individualized invitation letters, saving them to separate files in the "../Day24/Output/ReadyToSend/" directory. The placeholder "[name]" in the original letter is replaced with the corresponding name for each invitee.