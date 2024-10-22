def create_matrix(key):
    key = key.upper().replace('J', 'I')  # Replace 'J' with 'I'
    key = ''.join(dict.fromkeys(key))  # Remove duplicates
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Excludes 'J'
    matrix = [char for char in key if char in alphabet] + [char for char in alphabet if char not in key]
    return [matrix[i:i + 5] for i in range(0, 25, 5)]  # 5x5 matrix

def find_position(matrix, char):
    for r, row in enumerate(matrix):
        if char in row:
            return r, row.index(char)

def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")  # Replace 'J' with 'I', remove spaces
    prepared_text = ""
    i = 0

    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'  # If odd length, add 'X' at the end

        if a == b:  # If both letters are the same, add filler 'X' between them
            prepared_text += a + 'X'
            i += 1  # Move only one step ahead
        else:
            prepared_text += a + b
            i += 2  # Move two steps ahead

    if len(prepared_text) % 2 != 0:  # If odd length after all, add 'X' at the end
        prepared_text += 'X'

    return prepared_text

def playfair_cipher(text, key):
    matrix = create_matrix(key)
    text = prepare_text(text)  # Prepare the text to handle duplicates and odd length
    
    cipher = ''
    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)

        if row_a == row_b:  # Same row
            cipher += matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:  # Same column
            cipher += matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
        else:  # Rectangle swap
            cipher += matrix[row_a][col_b] + matrix[row_b][col_a]
    
    return cipher

# Example run
key = "playfair example"
text = "mass"
print("Ciphered Text:", playfair_cipher(text, key))
