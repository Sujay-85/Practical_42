def caesar_cipher(text, shift):
    result = "" 
    for char in text: 
        if char.isalpha(): 
            shift_base = 65 if char.isupper() else 97 
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else: 
            result += char 
    return result 
# Example usage: 
text = "Hello1, World!" 
shift = 3 
cipher_text = caesar_cipher(text, shift)
print("Ciphered Text:", cipher_text) 


# Character: 'H'

# It's an uppercase letter.
# ASCII of 'H' = 72.
# Shift base = 65 (for 'A').
# Normalized value = 72 - 65 = 7.
# After shifting: (7 + 3) % 26 = 10.
# New character: 10 + 65 = 75 ('K').