from art import logo, vs
from game_data import data
import random
from os import system

def get_data():
    """Get data from random account."""
    return random.choice(data)

def format_data(account):
    """Formats the data into printable format."""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"

def check_answer(follower_count_A, follower_count_B, answer):
    if follower_count_A > follower_count_B:
        return answer == 'a'
    else:
        return answer == 'b'


def game():
    account_a = get_data()
    account_b = get_data()
    score = 0
    run_again = True
    
    while run_again:
        account_a = account_b
        account_b = get_data()
        
        if account_a == account_b:
            account_b = get_data()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        account_a_followers = account_a['follower_count']
        account_b_followers = account_b['follower_count']
        
        is_correct = check_answer(account_a_followers, account_b_followers, answer)

        system('cls')
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            run_again = False
            print(f"Sorry that's wrong. Final score: {score}")


system('cls')
while input("Do you want to play the Higher or Lower game? Type 'y' or 'n': ").lower() == 'y':
    system('cls')
    print(logo)
    game()
else:
    system('cls')
    print("Sorry to see you go")