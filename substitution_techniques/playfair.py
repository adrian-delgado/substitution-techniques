from helpers import index_in_alphabet, to_letter

def two_at_once(iterable, filler):
    if len(iterable) % 2 == 1:
        iterable += filler
    return iter(zip(iterable[0 :: 2], iterable[1 :: 2]))

def empty_matrix(n, m):
    return [ [None] * m for _ in range(n) ]

def print_matrix(matrix):
    for row in matrix:
        print row

def find_coords_in_matrix(matrix, x):
    for i, row in enumerate(matrix):
        for j, item in enumerate(row):
            if item == x:
                return i, j
    return -1, -1


def generate_matrix(keyword, use_I):
    used_letters = [False] * 26 # keeps track of letters already added to matrix
    matrix = empty_matrix(5, 5) # 5 x 5 matrix
    i = 0 # index in the matrix
    for c in keyword:
        matrix[i / 5][i % 5] = c
        used_letters[index_in_alphabet(c)] = True
        i += 1
    for j in range(26): # iterate over alphabet
        char = to_letter(j)
        skip_char = (char == 'J') if use_I else (char == 'I')
        if not used_letters[j]:
            if not skip_char:
                matrix[i / 5][i % 5] = char
                used_letters[j] = True
                i += 1
    return matrix

def cipher_char_pair(matrix, c1, c2):
    i1, j1 = find_coords_in_matrix(matrix, c1)
    i2, j2 = find_coords_in_matrix(matrix, c2)

    if i1 == i2: # both letters on same row
        c1 = matrix[i1][(j1 + 1) % 5]
        c2 = matrix[i2][(j2 + 1) % 5]
    elif j1 == j2: # both letters on same column
        c1 = matrix[(i1 + 1) % 5][j1]
        c2 = matrix[(i2 + 1) % 5][j2]
    else:
        c1 = matrix[i1][j2]
        c2 = matrix[i2][j1]

    return c1 + c2

def cipher(plaintext, keyword, use_I = True, filler = 'X'):
    matrix = generate_matrix(keyword, use_I) # generate playfair matrix
    # print_matrix(matrix)

    ciphertext = ''
    i = 0
    while i < len(plaintext):
        c1 = plaintext[i]
        c2 = plaintext[i + 1] if i + 1 < len(plaintext) else 'X'

        if c1 == c2:
            ciphertext += cipher_char_pair(matrix, c1, 'X')
            i += 1
        else:
            ciphertext += cipher_char_pair(matrix, c1, c2)
            i += 2

    return ciphertext

if __name__ == "__main__":
    plaintext = 'THEQUICKBROWNFOXIUMPSOVERTHELAZYDOGA'
    keyword = 'MONARCHY'
    ciphertext = cipher(plaintext, keyword)
    print plaintext
    print ciphertext
