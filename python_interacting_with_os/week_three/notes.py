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
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))  # <re.Match object; span=(0, 4), match='Pang'>

# ==========================================================================================

# Wildcards and Special Characters

