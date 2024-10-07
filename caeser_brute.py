def caesar_decrypt(ciphertext, shift):
    decrypted_text = []
    for char in ciphertext:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
                decrypted_char = chr(start + (ord(char) - start - shift_amount) % 26)
            elif char.isupper():
                start = ord('A')
                decrypted_char = chr(start + (ord(char) - start - shift_amount) % 26)
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

def score_text(text):
    common_words = ["the", "and", "of", "to", "a", "in", "is", "it", "that", "with"]
    score = sum(text.lower().count(word) for word in common_words)
    return score

def brute_force_caesar(ciphertext):
    results = []
    for shift in range(1, 26):
        decrypted_text = caesar_decrypt(ciphertext, shift)
        score = score_text(decrypted_text)
        results.append((shift, decrypted_text, score))
    
    results.sort(key=lambda x: x[2], reverse=True)
    
    for shift, text, score in results:
        print(f"🠞 {shift} (🠜 {26 - shift})\t{text}")

ciphertext = "wpjvJAM{jhlzhy_k3jy9wa3k_m0212758}"
brute_force_caesar(ciphertext)