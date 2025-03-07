import re

def generate_matrix(keyword):
    keyword = keyword.upper().replace("J", "I")
    key_set = []
    for char in keyword:
        if char not in key_set and char.isalpha():
            key_set.append(char)
    
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in key_set:
            key_set.append(char)
    
    matrix = [key_set[i:i+5] for i in range(0, 25, 5)]
    print("\nGenerated Playfair Matrix:")
    for row in matrix:
        print(" ".join(row))
    return matrix

def format_text(text):
    text = re.sub(r'[^A-Za-z]', '', text).upper().replace("J", "I")
    formatted = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            formatted += a + 'X'
            i += 1
        else:
            formatted += a + b
            i += 2
    if len(formatted) % 2 != 0:
        formatted += 'X'
    return formatted

def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col

def encrypt(text, matrix):
    formatted_text = format_text(text)
    result = ""
    for i in range(0, len(formatted_text), 2):
        a, b = formatted_text[i], formatted_text[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        
        if row1 == row2:
            col1 = (col1 + 1) % 5
            col2 = (col2 + 1) % 5
        elif col1 == col2:
            row1 = (row1 + 1) % 5
            row2 = (row2 + 1) % 5
        else:
            col1, col2 = col2, col1
        
        result += matrix[row1][col1] + matrix[row2][col2]
    return result

def decrypt(text, matrix):
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        
        if row1 == row2:
            col1 = (col1 - 1) % 5 if col1 > 0 else 4
            col2 = (col2 - 1) % 5 if col2 > 0 else 4
        elif col1 == col2:
            row1 = (row1 - 1) % 5 if row1 > 0 else 4
            row2 = (row2 - 1) % 5 if row2 > 0 else 4
        else:
            col1, col2 = col2, col1
        
        result += matrix[row1][col1] + matrix[row2][col2]
    return result

def main():
    keyword = input("Enter the keyword: ")
    matrix = generate_matrix(keyword)
    
    while True:
        choice = input("\nDo you want to encrypt or decrypt? (e/d, q to quit): ").lower()
        if choice == 'q':
            break
        text = input("Enter the text: ")
        if choice == 'e':
            print("Encrypted text:", encrypt(text, matrix))
        elif choice == 'd':
            print("Decrypted text:", decrypt(text, matrix))
        else:
            print("Invalid choice! Please enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit.")

if __name__ == "__main__":
    main()
