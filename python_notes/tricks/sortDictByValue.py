def dict():
    pass


keyval = {3: 48, 2: 6, 5: 10, 1: 22, 6: 15, 4: 245}

'''
original was replaced with a dict literal
keyval = {}


# Initializing the value
keyval[3] = 48
keyval[2] = 6
keyval[5] = 10
keyval[1] = 22
keyval[6] = 15
keyval[4] = 245
'''

# Initializing the value
print("Task 3:-\nKeys and Values sorted",
      "in alphabetical order by the value")

# Remember this would arrange in aphabetical sequence
# Convert it to float to mathematical purposes

print(sorted(keyval.items(), key=
lambda k_val: (k_val[1], k_val[0])))


def main():
    dict()


if __name__ == "__main__":
    main()

'''OUTPUT
[(2, 6), (5, 10), (6, 15), (1, 22), (3, 48), (4, 245)]
'''
