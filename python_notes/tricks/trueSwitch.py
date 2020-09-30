def aswitch(a):
    return aswitch._system_dic.get(a, None)


aswitch._system_dic = {'mangoes': 4, 'apples': 6, 'oranges': 8}

print(aswitch('default'))
print(aswitch('oranges'))

'''OUTPUT
None
8
'''
