from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = ['Rock', 'Paper', 'Scissors']
user_choice = int(input("Enter your choice 0 for Rock, 1 for Paper and 2 for Scissors. "))

if user_choice == 0:
    print(f"You chose: {options[user_choice]}\n" + rock)
elif user_choice == 1:
    print(f"You chose: {options[user_choice]}\n" + paper)
elif user_choice == 2:
    print(f"You chose: {options[user_choice]}\n" + scissors)
else:
    print("Invalid Input")

comp_choice = randint(0, 2)
if comp_choice == 0:
    print(f"Computer chose: {options[comp_choice]}\n" + rock)
if comp_choice == 1:
    print(f"Computer chose: {options[comp_choice]}\n" + paper)
if comp_choice == 2:
    print(f"Computer chose: {options[comp_choice]}\n" + scissors)

if user_choice == comp_choice:
    print("Its a draw.")
elif user_choice == 2 and comp_choice == 0:
    print("You lost.")
elif user_choice > comp_choice or (user_choice == 0 and comp_choice == 2):
    print("You won.")
else:
    print("You lost")