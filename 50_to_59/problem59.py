"""
Each character on a computer is assigned a unique code and the preferred standard is ASCII
(American Standard Code for Information Interchange). For example, uppercase A = 65,
asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte
with a given value, taken from a secret key. The advantage with the XOR function is that using the
same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then
107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made
up of random bytes. The user would keep the encrypted message and the encryption key in different
locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password
as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically
throughout the message. The balance for this method is using a sufficiently long password key for
security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using
cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and
the knowledge that the plain text must contain common English words, decrypt the message and find the
sum of the ASCII values in the original text.
"""

import requests
from collections import Counter

rstr = requests.get('https://projecteuler.net/project/resources/p059_cipher.txt').text
cipher = [int(i) for i in rstr.split(',')]
frequent_words = [' the ', ' be ', ' to ', ' of ', ' and ', ' a ', ' in ', ' that ',
                  ' have ', ' I ', ' it ', ' for ', ' not ', ' on ', ' with ', ' as ']

def decode(cipher, secret):
    secret_str_extended = (len(cipher) / len(secret)) * secret + secret[:len(cipher) % len(secret)]
    secret_ord = [ord(s) for s in secret_str_extended]
    return ''.join([chr(num^secret_ord[idx]) for idx, num in enumerate(cipher)])

max_words = 0
message = ''
for a in range(ord('a'), ord('z')+1):
    for b in range(ord('a'), ord('z')+1):
        for c in range(ord('a'), ord('z')+1):
            key = ''.join([chr(n) for n in [a, b, c]])
            decoded_str = decode(cipher, key)
            num_words_found = sum([1 for word in frequent_words if word in decoded_str])
            if num_words_found > max_words:
                max_words = num_words_found
                message = decoded_str

print sum([ord(s) for s in message])
