
import functools

fact = (lambda i: functools.reduce(int.__mul__(), range(1, i + 1), 1)(4))

print(fact)

'''OUTPUT
24
'''
