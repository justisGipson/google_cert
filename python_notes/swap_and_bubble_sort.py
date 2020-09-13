nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("PRE SORT: {0}".format(nums))


def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp


def bubble_sort_unoptimized(arr):
    iteration_count = 0
    for e in arr:
        for i in range(len(arr) - 1):
            iteration_count += 1
            if arr[i] > arr[i + 1]:
                swap(arr, i, i + 1)

    print("PRE-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))


def bubble_sort(arr):
    iteration_count = 0
    for e in range(len(arr)):
        # iterate through unplaced elements
        for i in range(len(arr) - e - 1):
            iteration_count += 1
            if arr[i] > arr[i + 1]:
                # replacement for swap function
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    print("POST-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))


bubble_sort_unoptimized(nums.copy())
bubble_sort(nums)
print("POST SORT: {0}".format(nums))
