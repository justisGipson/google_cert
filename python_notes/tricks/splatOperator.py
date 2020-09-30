def test(a, b, c):
    print(p, q, r)


test_Dic = {'a': 4, 'b': 5, 'c': 6}
test_List = [10, 11, 12]

test(*test_Dic)
test(**test_Dic)
test(*test_List)

'''OUTPUT
#1-> p q r
#2-> 4 5 6
#3-> 10 11 12
'''
