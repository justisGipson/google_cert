#!/usr/bin/env python3

def to_seconds(hours, minutes, seconds):
    return hours*3600+minutes*60+seconds

print('Welcome to the time converter')

cont = 'y'
while (cont.lower() == 'y'):
    hours = int(input('Number of hours: '))
    minutes = int(input('Number of minutes: '))
    seconds = int(input('Number of seconds: '))

    print('That is {} seconds'.format(to_seconds(hours, minutes, seconds)))
    print()
    cont = input('Do you want to do more conversions? [y to continue]')

print('Bye')
