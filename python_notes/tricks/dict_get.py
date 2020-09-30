"""
Traditional way of accessing value for key

dict = {"P":1, "Q":2}
print(dict["P"])
print(dict["R"])

concern is that the third line of the code yields a key error:

Traceback (most recent call last):
  File ".\dict.py", line 3, in
    print (dict["R"])
KeyError: 'R'

Prevent these cases, the get() function is used. This technique provides the value for a specific key when available
in the dictionary. When it isn’t, None will be returned (if only one argument is used with get()).
"""

dict = {"P": 1, "Q": 2}
print(dict.get("P"))
print(dict.get("R"))
print(dict.get("R", "Unavailable! "))

'''OUTPUT
1
None
Unavailable!
'''
