join = lambda charlist: ''.join(charlist)
index = lambda c: ord(c) - 65
tochar = lambda n: chr(n + 65)

def cipher_single_char(c, k):
    new_index = index(c) + k
    new_char = tochar(new_index % 26)
    return new_char

def cipher(plaintext, k):
    return join([ cipher_single_char(c, k) for c in plaintext])

def decipher(ciphertext, k):
    return join([ cipher_single_char(c, -k) for c in ciphertext])

if __name__ == "__main__":
    key = 1
    plaintext = 'ABC'
    ciphertext = cipher(plaintext, key)
    print plaintext
    print ciphertext
    print decipher(ciphertext, key) == plaintext
