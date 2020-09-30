from collections import Counter


def anagram(string_1, string_2):
    return Counter(string_1) == Counter(string_2)


anagram('pqrs', 'rqsp')  # True

anagram('pqrs', 'rqqs')  # False
