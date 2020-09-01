#Standard Streams

# STDIN - the standard input stream which is a channel between a program and a source of input
# STDOUT - the standard output stream which is a pathway between a program and a target of output
# SDTERR - the standard error stream which displays output like standard out, but is used specifically as a channel to show error messages and diagnostics from the program

data = input("This comes from STDIN: ")
print("Writing to STDOUT: " + data)
# print("We are generating an error to STDERR: " + data + 1)

# ==========================================================================================

# Environment Variables

# `env` command outputs all currently set environ variables

import os
# environ variables allow us to access variables set by/for the environment
# get function specifies a default value when the key we are looking isn't in the dictionary
print('HOME: ' + os.environ.get('HOME', ''))
print('SHELL: ' + os.environ.get('SHELL', ''))
# export FRUIT=pineapple
print('FRUIT: ' + os.environ.get('FRUIT', ''))

# ==========================================================================================

# Command Line Arguments and Exit Status

import sys
print(sys.argv)

import os

# Receives a file name as a command line argument
# filename = sys.argv[0]

# Checks whether the file name exist or not
# When the file doesn't exist, it creates it by writing a line to it
# if not os.path.exists(filename):
#      with open(filename, "w") as f:
#          f.write("New file created\n")
# When the file exist, our script print an error message and exits with an exit value of one
# else:
#     print("Error, the file {} already exists!".format(filename))
#     sys.exit(1)

# Standard Library Docs:

# https://docs.python.org/2/library/functions.html#input
# https://docs.python.org/2/library/functions.html#raw_input
# https://docs.python.org/2/library/functions.html#eval

# In Python 3

# Input handles string as a generic string. It does not evaluate the string as a string expression.
# raw_input doesn’t exist, but with some tricky techniques, it can be supported.
# eval() can be used the same as Python 2.
# Standard Library Docs:

# https://docs.python.org/3/library/functions.html#input
# https://docs.python.org/3/library/functions.html#eval

# ==========================================================================================

# Python Subprocesses


