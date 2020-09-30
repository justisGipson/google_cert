
def uniq(list):
    if len(list) == len(set(list)):
        print("total items are unique")
    else:
        print("List includes duplicate item")


uniq([0, 2, 4, 6])  # total items are unique

uniq([1, 3, 3, 5])  # List includes duplicate item
