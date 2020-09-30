
number = 2468

# with map
digit_list = list(map(int, str(number)))
print(digit_list)

'''OUTPUT
[2, 4, 6, 8]
'''

# with list comprehension
digit_list = [int(a) for a in str(number)]
print(digit_list)

'''OUTPUT
[2, 4, 6, 8]
'''

# Even simpler approach
digit_list = list(str(number))
print(digit_list)

'''OUTPUT
[2, 4, 6, 8]
'''
