import itertools
import string

def decrypt(ciphertext, key_mapping):
    return "".join(key_mapping.get(char, char) for char in ciphertext)

def brute_force_monoalphabetic(ciphertext):
    alphabet = string.ascii_lowercase
    permutations = itertools.permutations(alphabet)
    
    for perm in permutations:
        key_mapping = dict(zip(alphabet, perm))
        decrypted_text = decrypt(ciphertext.lower(), key_mapping)
        print(f"Possible decryption: {decrypted_text}")

if __name__ == "__main__":
    encrypted_message = input("Enter the encrypted message: ")
    brute_force_monoalphabetic(encrypted_message)
