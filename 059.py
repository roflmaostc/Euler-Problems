#!/usr/bin/env python


"""
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
"""

def get_numbers():
    f = open('files/p059_cipher.txt', 'r')
    return f.readline().split(",")


def convert(l):
    return [chr(x) for x in l]

def to_string(l):
    str = ""
    for e in l:
        str += chr(e)
    return str


def iterate(n):
    decrypted = n.copy()
    for a in range(97,123):
        for b in range(97,123):
            for c in range(97,123):
                for i in range(0, len(n)//3):
                    decrypted[3*i] = n[3*i] ^ a 
                    decrypted[3*i+1] = n[3*i+1] ^ b 
                    decrypted[3*i+2] = n[3*i+2] ^ c 
                if "going" in to_string(decrypted):
                    return a,b,c
    return 0,0,0

def solve_problem():
    n = [int(x) for x in get_numbers()]
    decrypted = n.copy()
    a,b,c = iterate(n[:-1])
    for i in range(0, len(n)//3):
        decrypted[3*i] = n[3*i] ^ a 
        decrypted[3*i+1] = n[3*i+1] ^ b 
        decrypted[3*i+2] = n[3*i+2] ^ c 

    decrypted[-1] = n[-1]^a     
    decrypted_text = convert(decrypted)
    
    # print(to_string(decrypted))

    return sum(decrypted)

print(solve_problem())
