from CaeserCodeDecode import caeser
import CaeserArt

start_again = True
while start_again:
    print(CaeserArt.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text=text, shift=shift, direction=direction)
    again = input("Type 'yes' is you want to go again. Otherwise type 'no'\n").lower()
    if again == 'no':
        start_again = False
        print("Goodbye.")
        