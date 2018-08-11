from caesar import cipher_single_char
from helpers import index_in_alphabet, join

def get_key(plaintext, keyword):
    plaintext_key_ratio = len(plaintext) / len(keyword)
    key = keyword * (plaintext_key_ratio + 1)
    return key[:len(plaintext)]

def cipher(plaintext, keyword):
    key = get_key(plaintext, keyword)

    ciphered = [cipher_single_char(p, index_in_alphabet(k)) for p, k in zip(plaintext, key)]

    return join(ciphered)

def decipher(ciphertext, keyword):
    key = get_key(ciphertext, keyword)

    plain = [cipher_single_char(p, -index_in_alphabet(k)) for p, k in zip(ciphertext, key)]

    return join(plain)

if __name__ == "__main__":
    # plaintext = 'wearediscoveredsaveyourself'.upper()
    plaintext = 'deceptive'.upper()
    key = 'deceptive'.upper()
    ciphertext = cipher(plaintext, key)
    print plaintext
    print ciphertext
    print plaintext == decipher(ciphertext, key)
