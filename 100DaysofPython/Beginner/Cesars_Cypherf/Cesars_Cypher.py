import cesar_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift_amount, direction_ch):
    cipher_text = ""
    
    for letter in plain_text:
        position =  alphabet.index(letter)
        if direction_ch == "encode":
            new_position = position + shift_amount
            if new_position >= len(alphabet):
                new_position -= (len(alphabet))
            new_letter = alphabet[new_position]
        elif direction_ch == "decode":
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The {direction_ch}d text is {cipher_text}")



print(cesar_art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if shift > len(alphabet):
    shift %= len(alphabet)

caesar(text, shift, direction)
