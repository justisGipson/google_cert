def binary_search(key, list):
    """Returns position of key in list if found,
    otherwise returns -1

    LIST MUST BE SORTED"""
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            return  middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1
