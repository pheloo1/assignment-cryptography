from collections import Counter

def frequency_analysis(ciphertext):
    letter_counts = Counter(ciphertext)
    sorted_letters = [char for char, _ in letter_counts.most_common() if char.isalpha()]
    return sorted_letters

def decrypt_with_frequency(ciphertext):
    english_freq_order = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    cipher_freq_order = frequency_analysis(ciphertext)
    substitution_map = {cipher_letter: eng_letter.lower() for cipher_letter, eng_letter in zip(cipher_freq_order, english_freq_order)}
    decrypted_text = "".join(substitution_map.get(char, char) for char in ciphertext)
    return decrypted_text

if __name__ == "__main__":
    ciphertext = input("Enter the encrypted text: ")
    print("Most likely decrypted text:")
    print(decrypt_with_frequency(ciphertext))
