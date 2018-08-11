ASCII_OFFSET = 65

def index_in_alphabet(char):
    return ord(char) - ASCII_OFFSET

def to_letter(index):
    return chr(index + ASCII_OFFSET)

def join(charlist):
    return ''.join(charlist)
