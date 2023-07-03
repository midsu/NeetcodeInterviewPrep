def caesar_cipher(message, key):
    result = ""
    
    # Iterate through each character in the message
    for char in message:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Shift the character by the key positions and wrap around to the start of the alphabet if necessary
            shifted_char = chr((ord(char) + key - 65) % 26 + 65)
            result += shifted_char
        # Check if the character is a lowercase letter
        elif char.islower():
            # Shift the character by the key positions and wrap around to the start of the alphabet if necessary
            shifted_char = chr((ord(char) + key - 97) % 26 + 97)
            result += shifted_char
        # If the character is not a letter, just add it to the result without shifting
        else:
            result += char
    
    return result

# Shift message by 3 positions
message = "HELLO"
key = 3
encrypted_message = caesar_cipher(message, key)
print(encrypted_message) # Output: KHOOR

# Shift message by 7 positions
message = "the quick brown fox jumps over the lazy dog"
key = 7
encrypted_message = caesar_cipher(message, key)
print(encrypted_message) # Output: aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn

