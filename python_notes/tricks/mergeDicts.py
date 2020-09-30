dic1 = {'men': 6, 'boy': 5}
dic2 = {'boy': 3, 'girl': 5}

merged_dict = {**dic1, **dic2}
print(merged_dict)

'''OUTPUT
{'men': 6, 'boy': 3, 'girl': 5}
'''
