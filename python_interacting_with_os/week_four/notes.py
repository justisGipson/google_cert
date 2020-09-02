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

import subprocess
subprocess.run(['date'])  # Wed Sep  2 14:34:53 EDT 2020  CompletedProcess(args=['date'], returncode=0)
subprocess.run(['sleep', '2'])  # CompletedProcess(args=['sleep', '2'], returncode=0)

# any command following program name are the command line arguments passed

# ==========================================================================================

# Obtaining the output of a system command

# The "host" command converts a host name to an IP address and vice versa
# Stores the result in a variable by passing the capture_output=True so that the result can be accessed

result = subprocess.run(['host', '8.8.8.8'], capture_output=True)
print(result.returncode)  # 0
print(result.stdout)  # b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'
# b' indicates that the output is an array of bytes
# python isn't aware of what encoding to use, so it represents it as a series of bytes

# Decode function applies an encoding to transform the bytes into a string
# It uses a UTF-8 encoding by default
print(result.stdout.decode().split())  # ['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.']

# Executes the rm command to remove file that doesn't exist
result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)  # 1
# stdout prints empty value since there is an error
print(result.stdout)  # b''
# stderr prints error value as the value can be accessed through the stderr attribute
print(result.stderr)  # b"rm: cannot remove 'does_not_exist': No such file or directory\n"

# Good example of how STDOUT and STDERR are different

# ==========================================================================================

# Advances Subprocess Management

# The copy method creates a new dictionary that can be changed as needed without modifying the original environment
my_env = os.environ.copy()

# The path variable indicates where the operating system will look for the executable programs
# Joins /opt/myapp and the old value of the path variable to the path separator
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

# Calls the myapp command, setting the end parameter to the new environment
result = subprocess.run(["myapp"], env=my_env)

# https://docs.python.org/3/library/subprocess.html

# ==========================================================================================

# Filtering Log Files with Regular Expressions

# check_cron.py
import re

logfile = sys.argv[1]
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            # continue keyword tells the loop to go to the next element
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        print(result)

# ==========================================================================================

import re
def show_time_of_pid(line):
  pattern = r"([a-zA-Z]+ \d+ \d+:\d+:\d+).*\[(\d+)\]\:"
  result = re.search(pattern, line)
  return '{} pid:{}'.format(result.group(1), result.group(2))

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440

# ==========================================================================================

usernames = {}
name = 'good_user'
usernames[name] = usernames.get(name, 0) + 1
print(usernames)  # {'good_user': 1}

# ==========================================================================================

import re

logfile = sys.argv[1]
usernames = {}
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            # continue keyword tells the loop to go to the next element
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) + 1
print(usernames)
