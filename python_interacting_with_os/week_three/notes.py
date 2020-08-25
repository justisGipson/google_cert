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
print(re.search(r'.com', 'welcome'))  # <re.Match object; span=(2, 6), match='lcom'>  - needs escape char to match '.'
print(re.search(r'\.com', 'welcome'))  # None - because no '.com' in the string
print(re.search(r'\.com', 'mydomain.com'))  # <re.Match object; span=(8, 12), match='.com'>

# Use \w to match any alphanumeric character including letters, numbers, and underscores
# Use \d to match digits
# Use \s for matching whitespace characters like space, tab or new line
# Use \b for word boundaries
print(re.search(r'\w*', 'This is an example'))  # <re.Match object; span=(0, 4), match='This'>
print(re.search(r'\w*', 'And_this_is_another'))  # <re.Match object; span=(0, 19), match='And_this_is_another'>

import re


def check_character_groups(text):
  result = re.search(r"^\w+\s", text)
  return result != None


print(check_character_groups("One"))  # False
print(check_character_groups("123  Ready Set GO"))  # True
print(check_character_groups("username user_01"))  # True
print(check_character_groups("shopping_list: milk, bread, eggs."))  # False

# regex101.com

# ==========================================================================================

# Regular Expressions in Action
print(re.search(r'A.*a', 'Argentina'))  # <re.Match object; span=(0, 9), match='Argentina>
# "Azerbaijan" returns "Azerbaija" because we did not specify the end
print(re.search(r'A.*a', 'Azerbaijan'))  # <re.Match object; span=(0, 9), match='Azerbaija'>
print(re.search(r'^A.*a$', 'Azerbaijan'))  # None
print(re.search(r'^A.*a$', 'Australia'))  # <re.Match object; span=(0, 9), match='Australia'>

pattern = r'^[a-zA-z_][a-zA-Z0-9_]*$'
print(re.search(pattern, 'this_is_a_valid_variable_name'))  # <re.Match objectl span=(0, 30), match='this_is_a_valid_variable_name'
print(re.search(pattern, 'this is not a valid variable name'))  # None - spaces aren't included in the pattern
print(re.search(pattern, 'my_variable1'))  # <re.Match object; span=(0, 12), match='my_variable1'>
print(re.search(pattern, '2my_variable1'))  # None - char classes don't include search to start with a number

import re


def check_sentence(text):
  result = re.search(r"^[A-Z][ |a-z]*[\.?!]", text)
  return result != None


print(check_sentence("Is this is a sentence?"))  # True
print(check_sentence("is this is a sentence?"))  # False
print(check_sentence("Hello"))  # False
print(check_sentence("1-2-3-GO!"))  # False
print(check_sentence("A star is born."))  # True

# https://docs.python.org/3/howto/regex.html
# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#greedy-versus-non-greedy

# ==========================================================================================

# Advanced Regular Expressions
# Capturing Groups
# Use parentheses to capture groups which are portions of the pattern that are enclosed in
# Below line defines two separate groups
result = re.search(r'(^\w*), (\w*)$', 'Lovelace, Ada')  # <re.Match object; span=(0, 13), match='Lovelace, Ada'>
print(result)

print(result.groups())  # ('Lovelace', 'Ada')
print(result[0])  # Lovelace, Ada
print(result[2])  # Lovelace
print(result[2])  # Ada

'{} {}'.format(result[2], result[1])  # Ada Lovelace

def rearrange_name(name):
  result = re.search(r'(^\w*), (\w*)$', name)
  if result is None:
    return name
  return "{} {}".format(result[2], result[1])

# Support middle initials
import re


def rearrange_name(name):
  result = re.search(r'^(\w*), (\w*.\w?\.?)$',  name)
  if result == None:
    return name
  return '{} {}'.format(result[2], result[1])


name=rearrange_name('Kennedy, John F.')
print(name)

# ==========================================================================================

# More on Repetition Qualifiers
# Use {}, curly brackets and one or two numbers to specify a range with numeric repetition qualifiers
print(re.search(r'[a-zA-Z]{5}', 'a ghost'))  # <re.Match object; span=(2, 7), match='ghost'>
print(re.search(r'[a-zA-Z]{5}', 'a scary ghost appeared'))  # <re.Match object; span=(2, 7), match='scary'>
print(re.findall(r'[a-zA-Z]{5}', 'a scary ghost appeared'))  # ['scary', 'ghost', 'appea']

# Use \b, which matches word limits at the beginning and end of the pattern, to match full words
print(re.findall(r'\b[a-zA-Z]{5}\b', 'A scary ghost appeared'))  # ['scary', 'ghost']
print(re.findall(r'\w{5,10}', 'I really like strawberries'))  # ['really', 'strawberri']
print(re.findall(r'\w{5,}', 'I really like strawberries'))  # ['really', 'strawberries']
print(re.search(r's\w{,20}', 'I really like strawberries'))  # <re.Match object; span=(14, 26), match='strawberries'>


import re


def long_words(text):
  pattern = r'\w{7,}'
  result = re.findall(pattern, text)
  return result


print(long_words("I like to drink coffee in the morning."))  # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon."))  # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night."))  # []

# ==========================================================================================
# Extracting PID using regex

import re
log = 'July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade'
regex = r'\[(\d+)\]'
result = re.search((regex, log))
print(result[1])  # 12345

result = re.search(regex, 'a completely different string that also has numbers [34567]')
print(result[1])  # 34567

def extract_pid(log_line):
  regex = r'\[(\d+)\]'
  result = re.search(regex, log_line)
  if result is None:
    return ''
  return result[1]


print(extract_pid(log))  # 12345
print(extract_pid("99 elephants in a [cage]"))  # ' '


import re


def extract_pid(log_line):
    regex = r"\[(\d+)\]\: (\w+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])


print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"))  # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]"))  # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message"))  # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup"))  # 67890 (RUNNING)

# ==========================================================================================

# Splitting and Replacing
# Split function from the re module works by taking any regular expression as a separator
# Use capturing parentheses to split list to include the elements that is used to split the values
print(re.split(r'[.?!]', 'One sentence. Another one? And a last one!'))  # ['One sentence', ' Another one',
# 'And a last one', '']

print(re.split(r'([.?!])', 'One sentence. Another one? And the last one!'))  # ['One sentence', '.', ' Another one', '?', ' And the last one', '!', '']

# Sub function from the re module is used for creating new strings by substituting all or part of them for a different string
# It uses regular expressions for both the matching and the replacing
print(re.sub(r'[\w.%+-]+@[\w.-]+', '[REDACTED]', 'Received an email for go_nuts95@my.example.com'))  #Received an email for [REDACTED]

print(re.sub(r'^([\w .-]*), ([\w .-]*)$', r'\2 \1', 'Lovelace, Ada'))  # Ada Lovelace

re.split(r"the|a", "One sentence. Another one? And the last one!")  # ['One sentence. Ano', 'r one? And ', ' l', 'st one!']

# https://regexcrossword.com/

# ==========================================================================================

import re


def transform_record(record):
  new_record = re.sub(r',(\d{3})', r',+1-\1', record)
  return new_record


print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
# Sabrina Green,+1-802-867-5309,System Administrator
print(transform_record("Eli Jones,684-3481127,IT specialist"))
# Eli Jones,+1-684-3481127,IT specialist
print(transform_record("Melody Daniels,846-687-7436,Programmer"))
# Melody Daniels,+1-846-687-7436,Programmer
print(transform_record("Charlie Rivera,698-746-3357,Web Developer"))
# Charlie Rivera,+1-698-746-3357,Web Developer

# ==========================================================================================
import re


def multi_vowel_words(text):
  pattern = r'(\w+[a,e,i,o,u]{3,}\w+)'
  result = re.findall(pattern, text)
  return result


print(multi_vowel_words("Life is beautiful"))
# ['beautiful']
print(multi_vowel_words("Obviously, the queen is courageous and gracious."))
# ['Obviously', 'queen', 'courageous', 'gracious']
print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner."))
# ['rambunctious', 'quietly', 'delicious']
print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)"))
# ['queue']
print(multi_vowel_words("Hello world!"))
# []

# ==========================================================================================
import re


def transform_comments(line_of_code):
  result = re.sub(r'[\#]{1,}', '//', line_of_code)
  return result


print(transform_comments("### Start of program"))
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable"))
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable"))
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)"))
# Should be "  return(number)"

# ==========================================================================================
import re


def convert_phone_number(phone):
  result = re.sub(r'\b(\d{3})-(\d{3})-(\d{4})\b', r'(\1) \2-\3', phone)
  return result


print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300
