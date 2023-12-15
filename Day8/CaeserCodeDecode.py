from CaeserAlphabet import alphabet

def caeser(text, shift, direction):
    end_text = ""
    if shift > len(alphabet):
        shift = shift % 26
    if direction == 'decode':
        shift *= -1
    
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            if (position + shift) > len(alphabet):
                new_position = position + shift - 26
                end_text += alphabet[new_position]
            else:
                new_position = position + shift
                end_text += alphabet[new_position]
        else:
            end_text += char
    
    print(f"Your {direction}d message is {end_text}")



