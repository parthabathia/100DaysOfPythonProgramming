print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("\nWelcome to Treasure Island.")
start = input("Do you wish to find the treasure? (Y/N) ").upper()
play = 1
if start == 'Y':
    while play:
        print("Let's Start")
        direction = input("Do you wish to go Left or Right? (L/R) ").upper()
        if direction == 'R':
            print("You fell into a valley. You Died!")
            print("Game Over.")
            play_again = input("Do you wish to try again? (Y/N) ").upper()
            if play_again == 'Y':
                continue
            else:
                print("Sorry to see you go.")
                break
        else:
            print("You chose the correct path.")
            print("You arrived at a lake.")
            pass_the_lake = input("Do you wish to wait or swim? (W/S) ").upper()
            if pass_the_lake == 'S':
                print("You were eaten by pirhanas. You Died!")
                print("Game Over.")
                play_again = input("Do you wish to try again? (Y/N) ").upper()
                if play_again == 'Y':
                    continue
                else:
                    print("Sorry to see you go.")
                    break
            else:
                print("You waited for the boat.")
                print("You crossed the lake.")
                print("There are three doors in front of you. Red, Yellow and Blue.")
                gate = input("Which door will you select? (R/Y/B) ").upper()
                if gate == 'R':
                    print("You entered a room full of fire. You died.")
                    print("Game Over.")
                    play_again = input("Do you wish to try again? (Y/N) ").upper()
                    if play_again == 'Y':
                        continue
                    else:
                        print("Sorry to see you go.")
                        break
                elif gate == 'B':
                    print("You entered a room full of poison. You died.")
                    print("Game Over.")
                    play_again = input("Do you wish to try again? (Y/N) ").upper()
                    if play_again == 'Y':
                        continue
                    else:
                        print("Sorry to see you go.")
                        break
                else:
                    print("Congratulation! You have won.")
                    print("Game over.")
                    play_again = input("Do you wish to play again? (Y/N) ").upper()
                    if play_again == 'Y':
                        continue
                    else:
                        print("Sorry to see you go.")
                        break
else:
    print("Sorry to see you go.")