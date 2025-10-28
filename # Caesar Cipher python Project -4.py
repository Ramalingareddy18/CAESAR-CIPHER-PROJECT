# Caesar Cipher Project

alphabet = [chr(i) for i in range(97, 123)]  # ['a', 'b', ..., 'z']

def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"Here is the text after encryption: {cipher_text}")

def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print(f"Here is the text after decryption: {plain_text}")

# Main loop
wanna_end = False
while not wanna_end:
    what_to_do = input("Type 'encrypt' for encryption, type 'decrypt' for decryption:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Enter shift key:\n"))

    if what_to_do == "encrypt":
        encryption(plain_text=text, shift_key=shift)
    elif what_to_do == "decrypt":
        decryption(cipher_text=text, shift_key=shift)
    else:
        print("Invalid option. Please type 'encrypt' or 'decrypt'.")

    play_again = input("Type 'yes' to continue, type 'no' to exit:\n").lower()
    if play_again == 'no':
        wanna_end = True
        print("Have a nice day! Bye :)")