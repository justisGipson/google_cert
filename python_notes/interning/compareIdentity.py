import timeit


def compare_with_identity(n_times):
    import sys

    str1 = sys.intern('natural_language_processing' * 2000)
    str2 = sys.intern('natural_language_processing' * 2000)

    for i in range(n_times):
        if str1 == str2:
            pass


timeit.Timer(compare_with_identity(1000000))
