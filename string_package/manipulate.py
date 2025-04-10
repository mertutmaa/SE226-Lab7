import string
from string import capwords


def reverse_string(s):
    return s[:: -1]

def capitalize_words(s):
    return capwords(s)

def remove_punctuation(s):
    n = ''
    for x in s:
        if(char in string.punctuation for char in x): x = n

    return s
