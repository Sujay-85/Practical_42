from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Function to encrypt plaintext using DES
def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext.encode(), DES.block_size)  # Pad the text to the block size
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

# Function to decrypt ciphertext using DES
def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_padded_text = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_padded_text, DES.block_size).decode()
    return plaintext

# Example usage
key = get_random_bytes(8)  # DES uses a 64-bit (8 bytes) key
plaintext = "Hello DES Encryption!"

ciphertext = des_encrypt(plaintext, key)
print("Ciphertext:", ciphertext.hex())

decrypted_text = des_decrypt(ciphertext, key)
print("Decrypted text:", decrypted_text)
