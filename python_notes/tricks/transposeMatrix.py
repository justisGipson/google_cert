mat = [(5, 6, 7), (8, 9, 10), (11, 12, 13), (14, 15, 16)]
for row in mat:
    print(row)

print("\n")

t_mat = zip(*mat)
for row in t_mat:
    print(row)

'''OUTPUT
(5, 6, 7)
(8, 9, 10)
(11, 12, 13)
(14, 15, 16)
(5, 8, 11, 14)
(6, 9, 12, 15)
(7, 10, 13, 16)
'''
