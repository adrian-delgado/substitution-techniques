join = lambda charlist: ''.join(charlist)
index = lambda c: ord(c) - 65
tochar = lambda n: chr(n + 65)


def cypher(plaintext, k):
    # return join([ tochar((index(c) + k) % 26) for c in plaintext])
    cyphertext = ''
    for c in plaintext:
        cyphertext += tochar((index(c) + k) % 26)
    return cyphertext

def decypher(cyphertext, k):
    plaintext = ''
    for c in cyphertext:
        plaintext += tochar((index(c) - k) % 26)
    return plaintext

key = 1
plaintext = 'ABC'
cyphertext = cypher(plaintext, key)
print plaintext
print cyphertext
print decypher(cyphertext, key) == plaintext
