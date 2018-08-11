from helpers import index_in_alphabet, to_letter

def empty_matrix(n, m):
    return [ [None] * m for _ in range(n) ]

def print_matrix(matrix):
    for row in matrix:
        print row

class PlayFair:
    """
        generate playfair matrix using keyword
    """
    def __init__(self, keyword, use_I = True):
        used_letters = [False] * 26 # keeps track of letters already added to matrix
        self.matrix = empty_matrix(5, 5) # 5 x 5 matrix
        i = 0 # index in the matrix
        for c in keyword:
            self.matrix[i / 5][i % 5] = c
            used_letters[index_in_alphabet(c)] = True
            i += 1
        for j in range(26): # iterate over alphabet
            char = to_letter(j)
            skip_char = (char == 'J') if use_I else (char == 'I')
            if not used_letters[j]:
                if not skip_char:
                    self.matrix[i / 5][i % 5] = char
                    used_letters[j] = True
                    i += 1

    def find_coords_in_matrix(self, x):
        for i, row in enumerate(self.matrix):
            for j, item in enumerate(row):
                if item == x:
                    return i, j
        return None

    def cipher_char_pair(self, c1, c2):
        i1, j1 = self.find_coords_in_matrix(c1)
        i2, j2 = self.find_coords_in_matrix(c2)

        if i1 == i2: # both letters on same row
            c1 = self.matrix[i1][(j1 + 1) % 5]
            c2 = self.matrix[i2][(j2 + 1) % 5]
        elif j1 == j2: # both letters on isame column
            c1 = self.matrix[(i1 + 1) % 5][j1]
            c2 = self.matrix[(i2 + 1) % 5][j2]
        else:
            c1 = self.matrix[i1][j2]
            c2 = self.matrix[i2][j1]

        return c1 + c2

    def cipher(self, plaintext, filler = 'X'):
        ciphertext = ''
        pos = 0
        while pos < len(plaintext):
            c1 = plaintext[pos]
            c2 = plaintext[pos + 1] if pos + 1 < len(plaintext) else filler

            if c1 == c2:
                ciphertext += self.cipher_char_pair(c1, filler)
                pos += 1
            else:
                ciphertext += self.cipher_char_pair(c1, c2)
                pos += 2

        return ciphertext

if __name__ == "__main__":
    plaintext = 'THEQUICKBROWNFOXIUMPSOVERTHELAZYDOGA'
    keyword = 'MONARCHY'
    cipher = PlayFair(keyword)
    ciphertext = cipher.cipher(plaintext)
    print plaintext
    print ciphertext
