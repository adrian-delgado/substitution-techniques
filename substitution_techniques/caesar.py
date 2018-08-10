join = lambda charlist: ''.join(charlist)
index = lambda c: ord(c) - 65
tochar = lambda n: chr(n + 65)

def cypher_single_char(c, k):
    new_index = index(c) + k
    new_char = tochar(new_index % 26)
    return new_char

def cypher(plaintext, k):
    return join([ cypher_single_char(c, k) for c in plaintext])

def decypher(cyphertext, k):
    return join([ cypher_single_char(c, -k) for c in cyphertext])

if __name__ == "__main__":
    key = 1
    plaintext = 'ABC'
    cyphertext = cypher(plaintext, key)
    print plaintext
    print cyphertext
    print decypher(cyphertext, key) == plaintext
