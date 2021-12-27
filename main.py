import ascii_art as aa

# List off all the alphabets to be used in cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Caesar Cypher to encrypt and decrypt the given text string by the provided number of positions.


def caesar(start_text, shift_amount, cipher_type):
    end_text = ""
    if cipher_type == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_type}d result: {end_text}")


# Print the ascii logo of the Caesar Cypher onto the console.
print(aa.logo)

# While loop control variable.
end = False

# Continue the loop till the user doesn't want to exit the program.
while not end:
    # Direction - Method encode/decode
    # Text - Message to be encoded/decoded
    # Shift - Number of positions to be shifted in the alphabet list
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Take modulo with 26 to keep the index within the required range.
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_type=direction)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if restart == 'no':
        end = True
        print("Exiting.......")
