# Regular Expressions
log = "July 31 07:51:48 mycomputer bad_process[12345]: Error Performing package upgrade"
index = log.index('[')

# not a great way to do this, very brittle
print(log[index+1:index+6])

# 're' module allows for search function to find regex in strings
import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: Error Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regrex, log)
print(result[1])

# ==========================================================================================

# Basic Regular Expressions
# Simple Matching w/ Python
