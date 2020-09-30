"""
Assume we need to test:

p < q < r

operator chaining

if p < q < r:
    {...}

Comparisons return True or False
"""

# chaining comparison
a = 3
print(1 < a < 10)
print(5 < a < 15)
print(a < 7 < a * 7 < 49)
print(8 > a <= 6)
print(3 == a > 2)

'''OUTPUT
True
False
True
True
True
'''
