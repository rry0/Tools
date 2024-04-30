alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Questions
task = input('Encrypt (E) // Decrypt (D): ')
text = input('Enter text: ')
key = int(input('How many to shift by?: '))

ciphertext = '' # Set to null

if task.lower() == 'e':
    for char in text:  # for each character in the text
        if char in alphabet:  # If the character is in the alphabet
            position = alphabet.find(char)  # Find its position
            newpos = (position + key) % 26  # Shift it via the key using total amount
            newchar = alphabet[newpos]  # Set as newpos  
            ciphertext += newchar  # go to next character
        else:
            ciphertext += char  # If the character is not in the alphabet, keep it as it is
elif task.lower() == 'd':
    for char in text:  # for each character in the text
        if char in alphabet:  # If the character is in the alphabet
            position = alphabet.find(char)  # Find its position
            newpos = (position - key) % 26  # Shift it via the key using total amount
            newchar = alphabet[newpos]  # Set as newpos  
            ciphertext += newchar  # go to next character
        else:
            ciphertext += char  # If the character is not in the alphabet, keep it as it is

print('Encoded/Decoded text:', ciphertext)  # Print ciphertext
