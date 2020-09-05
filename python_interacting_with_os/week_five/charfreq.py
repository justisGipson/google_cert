#!/usr/bin/env python3

def character_frequency(filename):
    '''Counts the frequency of each character in a given file'''
    # first try to open the file
    try:
        f = open(filename)
    except OSError:
        return None

    # now process file
    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    f.close()
    return characters
