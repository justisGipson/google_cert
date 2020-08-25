# Regular Expressions
log = "July 31 07:51:48 mycomputer bad_process[12345]: Error Performing package upgrade"
index = log.index('[')

# not a great way to do this, very brittle
print(log[index + 1:index + 6])

# 're' module allows for search function to find regex in strings
import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: Error Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

# ==========================================================================================

# Basic Regular Expressions
# Simple Matching w/ Python
# Always a good idea to use rawstrings for python regex
# 'r' at the beginning of the pattern indicates this is a rawstring
import re

result = re.search(r'aza', 'plaza')
print(result)  # <re.Match object; span=(2, 5), match='aza>

result = re.search(r'aza', 'bazaar')
print(result)  # <re.Match object; span=(1, 4), match='aza>

# None is a special value that Python uses that show that there's none actual value there
result = re.search(r'aza', 'maze')
print(result)  # None

# The match attribute always has a value of the actual sub string that match the search pattern
# The span attribute indicates the range where the sub string can be found in the string
print(re.search(r"^x", "xenon"))  # <re.Match object; span=(0, 1), match='x'>
print(re.search(r"p.ng", "penguin"))  # <re.Match object; span=(0, 4), match='peng'>
print(re.search(r"p.ng", "sponge"))  # <re.Match object; span=(1, 5), match='pong'>

import re


def check_aei(text):
  result = re.search(r"a.e.i", text)
  return result != None


print(check_aei("academia"))  # True
print(check_aei("aerial"))  # False
print(check_aei("paramedic"))  # True

# Additional options to the search function can be added as a third parameter
# The re.IGNORECASE option returns a match that is case insensitive
print(re.search(r'p.ng', 'Pangaea', re.IGNORECASE))  # <re.Match object; span=(0, 4), match='Pang'>

# ==========================================================================================

# Wildcards and Special Characters
# Character classes are written in square brackets
# It lists the characters to match in the brackets
print(re.search(r'[Pp]ython', 'Python'))  # <re.Match object; span=(0, 6), match='Python

# A range of characters can be defined with a dash '-'
print(re.search(r'[a-z]way', 'The end of the highway'))  # <re.Match object; span=(18, 22), match='hway'>

print(re.search(r'[a-z]way', 'What a way to go'))  # None - because 'way' is preceded by whitespace

# Can combine as many character classes as needed
print(re.search(r'cloud[a-zA-z0-9]', 'cloudy'))  # <re.Match object; span=(0, 6), match='cloudy>
print(re.search(r'cloud[a-zA-z0-9]', 'cloud9'))  # <re.Match object; span=(0, 6), match='cloud9>

import re


def check_punctuation (text):
  result = re.search(r'[,.:;?!]', text)
  return result != None


print(check_punctuation("This is a sentence that ends with a period."))  # True
print(check_punctuation("This is a sentence fragment without a period"))  # False
print(check_punctuation("Aren't regular expressions awesome?"))  # True
print(check_punctuation("Wow! We're really picking up some steam now!"))  # True
print(check_punctuation("End of the line"))  # False

# Use a ^, circumflex, inside the square brackets to match any characters that aren't in a group
print(re.search(r'[^a-zA-Z]', 'This is a sentence with spaces.'))  # <re.Match object; span=(4, 5), match=' '>
print(re.search(r'[^a-zA-Z ]', 'This is a sentence with spaces.')) # <re.Match object; span=(30, 31), match='.'>

# Use a |, pipe symbol to match either one expression or another
# The search function returns the first matching string only when there are multiple matches
print(re.search(r'cat|dog', 'I like cats.'))  # <re.Match object; span=(7, 10), match='cat'>
print(re.search(r'cat|dog', 'I like dogs.'))  # <re.Match object; span=(7, 10), match='dog'>

# Since we have more than one match, the 'search' method finds the first match and returns that
print(re.search(r'cat|dog', 'I like both cats and dogs.'))  # <re.Match object; span=(12, 15), match='dog'>

# Use 're.findall' to return all possible matches
print(re.findall(r'cat|dog', 'I like both cats and dogs.'))  # ['dog', 'cat']

# ==========================================================================================

# Repetition Qualifiers
# Repeated matches is a common expressions that include a . followed by a *
# It matches any character repeated as many times as possible including zero - greedy behavior
print(re.search(r'Py.*n', 'Pygmalion'))  # <re.Match object; span=(0, 9), match='Pygmalion'>
print(re.search(r'Py.*n', 'Python Programming'))  # <re.Match object; span=(0, 17), match='Python Programmin'>
print(re.search(r'Py[a-z]*n', 'Python Programming'))  # <re.Match object; span=(0, 6), match='Python'>
print(re.search(r'Py[a-z]*n', 'Pyn'))  # <re.Match object; span=(0, 3), match='Pyn'>

# Use a +, plus character, to match one or more occurrences of the character that comes before it
print(re.search(r'o+l+', 'goldfish'))  # <re.Match objectl span=(1, 3), match='ol'>
print(re.search(r'o+l+', 'woolly'))  # <re.Match object; span=(1, 5), match='ooll'>
print(re.search(r'o+l+', 'boil'))  # None - because there's another character between the 'o' and 'l'

import re


def repeating_letter_a(text):
  result = re.search(r"[aA].*[aA]", text)
  return result != None


print(repeating_letter_a("banana"))  # True
print(repeating_letter_a("pineapple"))  # False
print(repeating_letter_a("Animal Kingdom"))  # True
print(repeating_letter_a("A is for apple"))  # True


# Use a ?, question mark symbol, for either zero or one occurrence of the character before it
# It is used to specified optional characters
print(re.search(r'p?each', 'To each their own'))  # <re.Match object; span=(3, 7), match='each'>
print(re.search(r'p?each', 'I like peaches'))  # <re.Match object; span=(7, 12), match='peach'>

# ==========================================================================================

# Escape Characters
# A pattern that includes a \ could be escaping a special regex character or a special string character
# Use a \, escape character, to match one of the special characters

